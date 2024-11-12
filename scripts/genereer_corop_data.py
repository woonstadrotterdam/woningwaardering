import asyncio
from typing import Any, Dict, List

import aiohttp
import pandas as pd
from loguru import logger

BASE_URL = "https://datasets.cbs.nl/odata/v1/CBS"
OUTPUT_FILE = "woningwaardering/data/corop/corop.generated.csv"


async def fetch_data(
    endpoint: str, session: aiohttp.ClientSession, params: Dict[str, str] | None = None
) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/{endpoint}"
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        json = await response.json()
        value: List[Dict[str, Any]] = json["value"]
        return value


async def get_woonplaats_data(session: aiohttp.ClientSession) -> pd.DataFrame:
    woonplaatsen_task = fetch_data("85877NED/WoonplaatsenCodes", session)
    observations_task = fetch_data(
        "85877NED/Observations",
        session,
        {
            "$filter": "Measure eq 'GM000B'",
            "$select": "Woonplaatsen,Measure,StringValue",
            "$format": "json",
        },
    )

    woonplaatsen, observations = await asyncio.gather(
        woonplaatsen_task, observations_task
    )

    df_woonplaatsen = pd.DataFrame(woonplaatsen).rename(columns={"Title": "Woonplaats"})
    df_observations = pd.DataFrame(observations)
    df_observations["StringValue"] = df_observations["StringValue"].str.strip()

    df_pivot = df_observations.pivot(
        index="Woonplaatsen", columns="Measure", values="StringValue"
    )
    df_pivot.columns = ["Gemeentecode"]
    df_pivot = df_pivot.reset_index()

    return pd.merge(
        df_pivot, df_woonplaatsen, left_on="Woonplaatsen", right_on="Identifier"
    ).rename(columns={"Woonplaatsen": "Woonplaatscode"})[
        ["Woonplaatscode", "Woonplaats", "Gemeentecode"]
    ]


async def get_gemeente_corop_data(session: aiohttp.ClientSession) -> pd.DataFrame:
    observations = await fetch_data(
        "85755NED/Observations",
        session,
        {
            "$filter": "Measure in ('CR0001', 'CR0002', 'GM000C_1', 'GM000B')",
            "$select": "RegioS,Measure,StringValue",
            "$format": "json",
        },
    )

    df_observations = pd.DataFrame(observations)
    df_observations["StringValue"] = df_observations["StringValue"].str.strip()

    df_pivot = df_observations.pivot(
        index="RegioS", columns="Measure", values="StringValue"
    )
    df_pivot.columns = ["COROP-gebiedcode", "COROP-gebied", "Gemeentecode", "Gemeente"]

    return df_pivot.reset_index()[
        ["Gemeentecode", "Gemeente", "COROP-gebiedcode", "COROP-gebied"]
    ]


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        woonplaatsen_task = get_woonplaats_data(session)
        gemeenten_task = get_gemeente_corop_data(session)

        woonplaatsen, gemeenten = await asyncio.gather(
            woonplaatsen_task, gemeenten_task
        )

        data = pd.merge(woonplaatsen, gemeenten, on="Gemeentecode")
        data.to_csv(OUTPUT_FILE, index=False)
        logger.info(f"COROP-gebieden:\n{data}")
        logger.info(f"COROP-gebieden opgeslagen in {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
