import asyncio
from datetime import date
from typing import Any, Dict, List
from urllib.parse import urlparse

import aiohttp
import pandas as pd
from loguru import logger

BASE_URL = "https://datasets.cbs.nl/odata/v1/CBS"
OUTPUT_FILE = "woningwaardering/data/corop/corop.generated.csv"

jaar = date.today().year

DATASETNAAM_WOONPLAATSEN = f"Woonplaatsen in Nederland {jaar}"
DATASETNAAM_GEBIEDEN = f"Gebieden in Nederland {jaar}"


async def fetch_data(
    endpoint: str, session: aiohttp.ClientSession, params: Dict[str, str] | None = None
) -> List[Dict[str, Any]]:
    url = f"{endpoint}"
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        json = await response.json()
        value: List[Dict[str, Any]] = json["value"]
        return value


async def get_odata_url(datasetnaam: str, session: aiohttp.ClientSession) -> str:
    datasets = await fetch_data(
        f"{BASE_URL}/Datasets",
        session,
        {
            "$filter": f"Title eq '{datasetnaam}'",
            "$format": "json",
        },
    )

    if len(datasets) == 0:
        raise ValueError(f"Geen dataset gevonden met de titel {datasetnaam}")

    distributions = datasets[0].get("Distributions")

    if (
        distributions is None
        or not isinstance(distributions, list)
        or len(distributions) == 0
    ):
        raise ValueError(f"Geen distributies gevonden voor {datasetnaam}")

    odata_distribution = next(
        (
            distribution
            for distribution in distributions
            if distribution is not None and distribution["Format"] == "odata"
        ),
        None,
    )

    if odata_distribution is None:
        raise ValueError(f"Geen odata distributie gevonden voor {datasetnaam}")

    odata_url = str(odata_distribution.get("DownloadUrl"))

    parse_result = urlparse(odata_url)
    if parse_result.scheme and parse_result.netloc:
        return odata_url
    else:
        raise ValueError(f"{odata_url} is geen geldige url")


async def get_woonplaats_data(session: aiohttp.ClientSession) -> pd.DataFrame:
    odata_url = await get_odata_url(DATASETNAAM_WOONPLAATSEN, session)

    woonplaatsen_task = fetch_data(f"{odata_url}/WoonplaatsenCodes", session)
    observations_task = fetch_data(
        f"{odata_url}/Observations",
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
    odata_url = await get_odata_url(DATASETNAAM_GEBIEDEN, session)

    observations = await fetch_data(
        f"{odata_url}/Observations",
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

    return df_pivot[["Gemeentecode", "Gemeente", "COROP-gebiedcode", "COROP-gebied"]]


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        woonplaatsen_task = get_woonplaats_data(session)
        gemeenten_task = get_gemeente_corop_data(session)

        woonplaatsen, gemeenten = await asyncio.gather(
            woonplaatsen_task, gemeenten_task
        )

        data = pd.merge(woonplaatsen, gemeenten, on="Gemeentecode")

        data["Woonplaatscode"] = data["Woonplaatscode"].str.lstrip("WP")
        data["Gemeentecode"] = data["Gemeentecode"].str.lstrip("GM")
        data["COROP-gebiedcode"] = data["COROP-gebiedcode"].str.lstrip("CR")

        data.to_csv(OUTPUT_FILE, index=False)
        logger.info(f"COROP-gebieden:\n{data}")
        logger.info(f"COROP-gebieden opgeslagen in {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
