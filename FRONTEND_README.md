# Woningwaardering Frontend Applicatie

Complete webapplicatie voor het berekenen van WWS (Woningwaarderingsstelsel) punten en maximale huurprijzen.

## 📋 Overzicht

Dit project bestaat uit twee onderdelen:
1. **Backend** - FastAPI server die de woningwaardering library wraps
2. **Frontend** - React + TypeScript applicatie met gebruiksvriendelijk formulier

## 🚀 Snelstart

### Stap 1: Backend starten

```bash
# Ga naar backend directory
cd backend

# Maak virtual environment (eerste keer)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# of: venv\Scripts\activate  # Windows

# Installeer dependencies
pip install -r requirements.txt
pip install -e ..  # Installeer woningwaardering library

# Start backend server
python -m uvicorn app.main:app --reload
```

De backend draait nu op [http://localhost:8000](http://localhost:8000)

### Stap 2: Frontend starten

Open een **nieuwe terminal**:

```bash
# Ga naar frontend directory
cd frontend

# Installeer dependencies (eerste keer)
npm install

# Start development server
npm run dev
```

De frontend is nu beschikbaar op [http://localhost:5173](http://localhost:5173)

## 🎯 Features

### Frontend
- ✅ Multi-step formulier met 5 stappen
- ✅ Sjablonen voor verschillende woningtypes
- ✅ Real-time validatie
- ✅ Gedetailleerde resultaat weergave
- ✅ JSON export functionaliteit
- ✅ Responsive design met Tailwind CSS
- ✅ Gebruiksvriendelijke UI met icons

### Backend
- ✅ RESTful API met FastAPI
- ✅ Volledige integratie met woningwaardering library
- ✅ Auto-generated API documentatie
- ✅ CORS support voor lokale development
- ✅ Error handling en logging

## 📱 Gebruik

### 1. Kies een Sjabloon of Start Leeg

Bij het openen van de applicatie kun je kiezen uit:
- **Studio Appartement** - ~35m²
- **2-Kamer Appartement** - ~60m²
- **Gezinswoning** - ~120m²
- **Nieuwbouw Appartement** - ~75m² met hoog energielabel
- **Lege Woning** - Start vanaf nul

### 2. Vul het Formulier In

Het formulier bestaat uit 5 stappen:

**Stap 1: Basis Informatie**
- Woning ID
- Bouwjaar
- Adresgegevens
- BAG Identificatie (optioneel)
- Peildatum (optioneel)

**Stap 2: Ruimtes**
- Voeg kamers toe met:
  - Naam
  - Oppervlakte (m²)
  - Type (Vertrek of Overige ruimte)
  - Detail type (Woonkamer, Slaapkamer, etc.)
  - Verwarmd/verkoeld

**Stap 3: Energieprestatie**
- Energielabel (A+++++ tot G)
- Type energieprestatie (EP1/EP2/EP3)
- Waarde en datums

**Stap 4: WOZ Waarde**
- Vastgestelde waarde in euro's
- Waardepeildatum

**Stap 5: Overzicht**
- Controleer alle ingevoerde gegevens
- Klik op "Bereken Woningwaardering"

### 3. Bekijk Resultaten

Het resultaat toont:
- **Totaal aantal WWS punten**
- **Maximale huurprijs** (basis en inclusief opslag)
- **Details per stelselgroep** (uitklapbaar):
  - Oppervlakte van vertrekken
  - Oppervlakte van overige ruimten
  - Verkoeling en verwarming
  - Energieprestatie
  - WOZ waarde
  - etc.

Je kunt:
- ✅ De resultaten exporteren als JSON
- ✅ Een nieuwe berekening starten

## 🏗️ Project Structuur

```
woningwaardering/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py            # API endpoints
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                   # React + TypeScript frontend
│   ├── src/
│   │   ├── components/        # React componenten
│   │   │   ├── WoningForm.tsx
│   │   │   ├── ResultaatDisplay.tsx
│   │   │   └── steps/         # Formulier stappen
│   │   ├── services/          # API client
│   │   ├── templates/         # Voorbeeld woningen
│   │   ├── types/            # TypeScript types
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── README.md
│
├── woningwaardering/          # Python library (bestaand)
├── tests/                     # Tests (bestaand)
└── FRONTEND_README.md         # Deze file
```

## 🔧 Development

### Backend Development

```bash
cd backend

# Activeer virtual environment
source venv/bin/activate

# Start met auto-reload
python -m uvicorn app.main:app --reload

# API documentatie beschikbaar op:
# - http://localhost:8000/docs (Swagger UI)
# - http://localhost:8000/redoc (ReDoc)
```

### Frontend Development

```bash
cd frontend

# Start development server
npm run dev

# Build voor productie
npm run build

# Preview productie build
npm run preview

# Linting
npm run lint
```

### Test API Endpoints

```bash
# Health check
curl http://localhost:8000/api/health

# Bereken woningwaardering
curl -X POST http://localhost:8000/api/bereken \
  -H "Content-Type: application/json" \
  -d '{
    "id": "TEST-001",
    "ruimten": [
      {
        "id": "R1",
        "naam": "Woonkamer",
        "soort": {"code": "VTK"},
        "oppervlakte": 25.5,
        "verwarmd": true
      }
    ]
  }'
```

## 🐛 Troubleshooting

### Backend start niet

```bash
# Controleer of Python 3.10+ is geïnstalleerd
python --version

# Installeer dependencies opnieuw
pip install -r backend/requirements.txt
pip install -e .
```

### Frontend start niet

```bash
# Controleer Node.js versie (18+)
node --version

# Verwijder node_modules en installeer opnieuw
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### CORS errors

Zorg dat:
1. Backend draait op poort 8000
2. Frontend draait op poort 5173
3. CORS is geconfigureerd in `backend/app/main.py`

### Port already in use

**Backend (poort 8000):**
```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Frontend (poort 5173):**
```bash
# Linux/Mac
lsof -ti:5173 | xargs kill -9

# Windows
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

## 📊 API Documentatie

### POST /api/bereken

Bereken woningwaardering voor een woning.

**Request Body:** `EenhedenEenheid` (VERA formaat)

**Query Parameters:**
- `peildatum` (optioneel): ISO date string (YYYY-MM-DD)

**Response:** `WoningwaarderingResultaat`

### GET /api/referentiedata/*

Haal referentiedata op:
- `/api/referentiedata/ruimtesoorten` - Ruimte types (VTK, OVR)
- `/api/referentiedata/ruimte-detailsoorten` - Detail types per ruimtesoort
- `/api/referentiedata/energielabels` - Beschikbare energielabels

## 🎨 Customization

### Kleuren aanpassen

Pas `frontend/tailwind.config.js` aan:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        500: '#jouw-kleur',
        // etc.
      }
    }
  }
}
```

### Sjablonen toevoegen

Voeg toe aan `frontend/src/templates/examples.ts`:

```typescript
{
  id: 'mijn-sjabloon',
  naam: 'Mijn Woning Type',
  beschrijving: 'Beschrijving...',
  data: { /* woninggegevens */ }
}
```

## 📦 Deployment

### Backend

Voor productie gebruik Gunicorn:

```bash
pip install gunicorn
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

### Frontend

Build de frontend:

```bash
cd frontend
npm run build
```

De `dist/` folder kan geserveerd worden met nginx, Apache, of via een CDN.

## 📝 Licentie

Zie het hoofd README.md bestand van de woningwaardering library voor licentie informatie.

## 🤝 Bijdragen

Dit is een frontend extensie van de woningwaardering library. Voor de core library, zie:
- Repository: https://github.com/woonstadrotterdam/woningwaardering
- Documentatie: [README.md](../README.md)

## 📞 Support

Voor vragen over:
- **De frontend/backend**: Zie de individuele README.md bestanden in `frontend/` en `backend/`
- **De woningwaardering library**: Zie het hoofd README.md bestand
- **Het WWS stelsel**: Bezoek https://www.huurcommissie.nl

## 🎉 Wat kun je nu doen?

1. ✅ Start beide servers (backend en frontend)
2. ✅ Open [http://localhost:5173](http://localhost:5173) in je browser
3. ✅ Probeer een sjabloon
4. ✅ Pas de gegevens aan
5. ✅ Bereken de woningwaardering
6. ✅ Export de resultaten
7. ✅ Bouw je eigen integraties!

Veel succes! 🚀
