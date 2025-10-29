# Woningwaardering Frontend

React + TypeScript frontend voor de Woningwaardering Calculator.

## Features

- 📝 **Multi-step formulier** voor het invoeren van woninggegevens
- 🏠 **Sjablonen** met voorbeeldwoningen (studio, appartement, gezinswoning)
- 🎨 **Modern UI** met Tailwind CSS
- 📊 **Gedetailleerde resultaten** met breakdown per stelselgroep
- 💾 **JSON export** van berekeningen
- ♿ **Toegankelijk** en gebruiksvriendelijk

## Vereisten

- Node.js 18+
- npm of yarn

## Installatie

```bash
# Installeer dependencies
npm install
```

## Ontwikkeling

Start de development server:

```bash
npm run dev
```

De applicatie is nu beschikbaar op [http://localhost:5173](http://localhost:5173)

**Let op:** Zorg dat de backend draait op poort 8000 voordat je de frontend start!

## Build voor Productie

```bash
npm run build
```

De gebouwde bestanden komen in de `dist/` folder.

Preview de productie build:

```bash
npm run preview
```

## Project Structuur

```
src/
├── components/          # React componenten
│   ├── WoningForm.tsx          # Hoofd formulier component
│   ├── ResultaatDisplay.tsx    # Resultaat weergave
│   └── steps/                  # Formulier stappen
│       ├── BasisInfoStep.tsx
│       ├── RuimtesStep.tsx
│       ├── EnergieprestatieStep.tsx
│       ├── WOZStep.tsx
│       └── OverzichtStep.tsx
├── services/            # API communicatie
│   └── api.ts
├── templates/           # Voorbeeld woningen
│   └── examples.ts
├── types/              # TypeScript type definities
│   └── index.ts
├── App.tsx             # Root component
├── main.tsx            # Entry point
└── index.css           # Global styles (Tailwind)
```

## Formulier Stappen

1. **Basis Info** - ID, bouwjaar, adres, BAG ID
2. **Ruimtes** - Toevoegen van kamers met oppervlakte en type
3. **Energieprestatie** - Energielabel en certificaat info
4. **WOZ Waarde** - Vastgestelde waarde en peildatum
5. **Overzicht** - Controle en berekening

## API Integratie

De frontend communiceert met de FastAPI backend via `/api` endpoints:

- `POST /api/bereken` - Bereken woningwaardering
- `GET /api/health` - Health check
- `GET /api/referentiedata/*` - Haal referentiedata op

## Customization

### Kleuren aanpassen

Pas de primary kleur aan in `tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        // Pas hier de kleuren aan
      }
    }
  }
}
```

### Sjablonen toevoegen

Voeg nieuwe sjablonen toe in `src/templates/examples.ts`:

```typescript
export const woningTemplates: WoningTemplate[] = [
  {
    id: 'mijn-template',
    naam: 'Mijn Woning',
    beschrijving: 'Beschrijving...',
    data: {
      // Woninggegevens
    }
  }
];
```

## Troubleshooting

### Backend niet bereikbaar

Zorg dat de backend draait:
```bash
cd ../backend
python -m uvicorn app.main:app --reload
```

### CORS errors

De backend moet CORS toestaan voor `http://localhost:5173`.
Dit is al geconfigureerd in `backend/app/main.py`.

### Build errors

Verwijder node_modules en installeer opnieuw:
```bash
rm -rf node_modules package-lock.json
npm install
```

## License

Zie het hoofd README.md bestand voor licentie informatie.
