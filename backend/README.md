# Woningwaardering Backend

FastAPI backend die de woningwaardering Python library wraps voor gebruik via een REST API.

## Features

- 🚀 **FastAPI** - Modern, snel Python web framework
- 📊 **WWS Berekening** - Volledige integratie met woningwaardering library
- 🔌 **REST API** - Eenvoudige HTTP endpoints
- 📝 **Auto Documentation** - Swagger UI en ReDoc
- 🔄 **CORS Support** - Voor lokale frontend development

## Vereisten

- Python 3.10+
- pip

## Installatie

```bash
# Maak virtual environment (aanbevolen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# of
venv\Scripts\activate  # Windows

# Installeer dependencies (backend + woningwaardering library)
pip install -r requirements.txt
pip install -e ..  # Installeer woningwaardering library vanuit parent directory
```

## Development

Start de development server:

```bash
# Vanuit de backend/ directory
python -m uvicorn app.main:app --reload --port 8000
```

Of direct via Python:

```bash
python app/main.py
```

De API is nu beschikbaar op:
- **API**: [http://localhost:8000](http://localhost:8000)
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### Health Check

```bash
GET /
GET /api/health
```

### Bereken Woningwaardering

```bash
POST /api/bereken
Content-Type: application/json

{
  "id": "WONING-001",
  "bouwjaar": 2000,
  "ruimten": [
    {
      "id": "R1",
      "naam": "Woonkamer",
      "soort": {"code": "VTK"},
      "detailSoort": {"code": "WOO"},
      "oppervlakte": 25.5,
      "verwarmd": true
    }
  ],
  "energieprestaties": [
    {
      "label": "A",
      "status": {"code": "DEF"}
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 250000,
      "waardepeildatum": "2023-01-01"
    }
  ]
}
```

Response:

```json
{
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "punten": 78,
  "maximale_huur": 446.19,
  "groepen": [
    {
      "criteriumGroep": {
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 25.5,
      "woningwaarderingen": [...]
    }
  ]
}
```

### Referentiedata

```bash
GET /api/referentiedata/ruimtesoorten
GET /api/referentiedata/ruimte-detailsoorten
GET /api/referentiedata/energielabels
```

## Project Structuur

```
backend/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI applicatie en endpoints
├── requirements.txt         # Python dependencies
└── README.md               # Deze file
```

## Testing

Test de API met curl:

```bash
# Health check
curl http://localhost:8000/api/health

# Bereken woningwaardering (met example data)
curl -X POST http://localhost:8000/api/bereken \
  -H "Content-Type: application/json" \
  -d @../tests/data/zelfstandige_woonruimten/input/20002000126.json
```

Of gebruik de interactieve Swagger UI op [http://localhost:8000/docs](http://localhost:8000/docs)

## CORS Configuratie

De backend staat CORS toe voor de volgende origins (configureerbaar in `app/main.py`):
- `http://localhost:5173` (Vite default)
- `http://localhost:3000` (React default)

Voor productie moet je dit aanpassen naar je echte frontend URL.

## Deployment

### Development

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production

```bash
# Met Gunicorn (aanbevolen voor productie)
pip install gunicorn
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Of met uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Environment Variables

Optioneel kan je environment variables gebruiken:

```bash
# .env bestand
BACKEND_CORS_ORIGINS=["http://localhost:5173","https://mijn-frontend.nl"]
```

## Error Handling

De API gebruikt standaard HTTP status codes:

- **200** - Success
- **400** - Validation error (ongeldige input)
- **500** - Server error (berekening fout)

Errors worden geretourneerd in het formaat:

```json
{
  "detail": "Foutmelding hier"
}
```

## Logging

De backend logt naar stdout. Configureer logging level in `app/main.py`:

```python
logging.basicConfig(level=logging.INFO)  # DEBUG, INFO, WARNING, ERROR
```

## Troubleshooting

### Import errors

Zorg dat de woningwaardering library geïnstalleerd is:
```bash
pip install -e ..
```

### Port already in use

Gebruik een andere poort:
```bash
uvicorn app.main:app --reload --port 8001
```

Of kill het proces op poort 8000:
```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

## License

Zie het hoofd README.md bestand voor licentie informatie.
