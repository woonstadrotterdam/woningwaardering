"""
FastAPI backend voor Woningwaardering (WWS Berekening)

Deze API wraps de woningwaardering Python library en biedt endpoints
voor het berekenen van de WWS punten en maximale huurprijs.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from typing import Optional
import logging

from woningwaardering.stelsels.zelfstandige_woonruimten import ZelfstandigeWoonruimten
from woningwaardering.vera.bvg.generated import EenhedenEenheid

# Configureer logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Maak FastAPI app
app = FastAPI(
    title="Woningwaardering API",
    description="API voor het berekenen van WWS punten en maximale huurprijs",
    version="1.0.0"
)

# CORS configuratie - sta localhost toe voor ontwikkeling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default poort
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "Woningwaardering API",
        "version": "1.0.0"
    }


@app.get("/api/health")
async def health():
    """Uitgebreide health check"""
    return {
        "status": "healthy",
        "timestamp": date.today().isoformat(),
        "stelsels": ["zelfstandige_woonruimten"]
    }


@app.post("/api/bereken")
async def bereken_woningwaardering(
    eenheid: EenhedenEenheid,
    peildatum: Optional[str] = None
):
    """
    Bereken de WWS punten en maximale huurprijs voor een woning.

    Args:
        eenheid: De woning eenheid met alle benodigde data (VERA formaat)
        peildatum: De datum waarop berekend wordt (optioneel, default: vandaag)

    Returns:
        WoningwaarderingResultaat met punten, maximale huur en details per groep
    """
    try:
        # Parse peildatum of gebruik vandaag
        if peildatum:
            peil_datum = date.fromisoformat(peildatum)
        else:
            peil_datum = date.today()

        logger.info(f"Berekening starten voor eenheid {eenheid.id} op peildatum {peil_datum}")

        # Maak calculator aan
        calculator = ZelfstandigeWoonruimten(peildatum=peil_datum)

        # Bereken woningwaardering
        resultaat = calculator.bereken(eenheid)

        logger.info(f"Berekening voltooid: {resultaat.punten} punten, max huur €{resultaat.maximale_huur}")

        # Converteer naar dict voor JSON response
        return resultaat.model_dump(mode='json', exclude_none=True)

    except ValueError as e:
        logger.error(f"Validatie fout: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Validatie fout: {str(e)}")
    except Exception as e:
        logger.error(f"Berekening fout: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Berekening fout: {str(e)}")


@app.get("/api/referentiedata/ruimtesoorten")
async def get_ruimtesoorten():
    """Haal lijst van beschikbare ruimte soorten op"""
    return {
        "VTK": "Vertrek (woonkamer, slaapkamer, keuken, etc.)",
        "OVR": "Overige ruimte (berging, zolder, kelder, etc.)"
    }


@app.get("/api/referentiedata/ruimte-detailsoorten")
async def get_ruimte_detailsoorten():
    """Haal lijst van beschikbare ruimte detail soorten op"""
    return {
        "vertrekken": {
            "WOO": "Woonkamer",
            "SLA": "Slaapkamer",
            "KEU": "Keuken",
            "BAD": "Badkamer"
        },
        "overige_ruimten": {
            "BER": "Berging",
            "ZOL": "Zolder",
            "KEL": "Kelder",
            "GAR": "Garage",
            "STA": "Stalling"
        }
    }


@app.get("/api/referentiedata/energielabels")
async def get_energielabels():
    """Haal lijst van beschikbare energielabels op"""
    return [
        "A+++++",
        "A++++",
        "A+++",
        "A++",
        "A+",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
