import { FormData } from '../types';

export interface WoningTemplate {
  id: string;
  naam: string;
  beschrijving: string;
  data: FormData;
}

export const woningTemplates: WoningTemplate[] = [
  {
    id: 'studio',
    naam: 'Studio Appartement',
    beschrijving: 'Compact studio appartement van ongeveer 35m² met keuken en badkamer',
    data: {
      id: 'STUDIO-001',
      bouwjaar: 2015,
      adres: {
        straatnaam: 'Voorbeeldstraat',
        huisnummer: '1',
        postcode: '1234AB',
      },
      ruimten: [
        {
          id: 'R1',
          naam: 'Woon/slaapkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'WOO' },
          oppervlakte: 25.5,
          verwarmd: true,
        },
        {
          id: 'R2',
          naam: 'Keuken',
          soort: { code: 'VTK' },
          detailSoort: { code: 'KEU' },
          oppervlakte: 6.0,
          verwarmd: true,
        },
        {
          id: 'R3',
          naam: 'Badkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'BAD' },
          oppervlakte: 3.5,
          verwarmd: true,
        },
      ],
      energieprestaties: [
        {
          label: 'A',
          soort: { code: 'EP2' },
          status: { code: 'DEF' },
          begindatum: '2015-06-01',
        },
      ],
      wozEenheden: [
        {
          vastgesteldeWaarde: 180000,
          waardepeildatum: '2023-01-01',
        },
      ],
    },
  },
  {
    id: 'appartement',
    naam: '2-Kamer Appartement',
    beschrijving: 'Standaard 2-kamer appartement van ongeveer 60m² met balkon',
    data: {
      id: 'APP-002',
      bouwjaar: 2000,
      adres: {
        straatnaam: 'Hoofdstraat',
        huisnummer: '25',
        postcode: '3000AA',
      },
      ruimten: [
        {
          id: 'R1',
          naam: 'Woonkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'WOO' },
          oppervlakte: 28.0,
          verwarmd: true,
        },
        {
          id: 'R2',
          naam: 'Slaapkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 14.0,
          verwarmd: true,
        },
        {
          id: 'R3',
          naam: 'Keuken',
          soort: { code: 'VTK' },
          detailSoort: { code: 'KEU' },
          oppervlakte: 8.5,
          verwarmd: true,
        },
        {
          id: 'R4',
          naam: 'Badkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'BAD' },
          oppervlakte: 5.0,
          verwarmd: true,
        },
        {
          id: 'R5',
          naam: 'Berging',
          soort: { code: 'OVR' },
          detailSoort: { code: 'BER' },
          oppervlakte: 4.5,
          verwarmd: false,
        },
      ],
      energieprestaties: [
        {
          label: 'B',
          soort: { code: 'EP2' },
          status: { code: 'DEF' },
          begindatum: '2020-03-15',
        },
      ],
      wozEenheden: [
        {
          vastgesteldeWaarde: 240000,
          waardepeildatum: '2023-01-01',
        },
      ],
    },
  },
  {
    id: 'gezinswoning',
    naam: 'Gezinswoning',
    beschrijving: 'Ruime gezinswoning van ongeveer 120m² met tuin en 3 slaapkamers',
    data: {
      id: 'WONING-003',
      bouwjaar: 1985,
      adres: {
        straatnaam: 'Tuinlaan',
        huisnummer: '42',
        postcode: '2500XY',
      },
      ruimten: [
        {
          id: 'R1',
          naam: 'Woonkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'WOO' },
          oppervlakte: 35.0,
          verwarmd: true,
        },
        {
          id: 'R2',
          naam: 'Keuken',
          soort: { code: 'VTK' },
          detailSoort: { code: 'KEU' },
          oppervlakte: 12.0,
          verwarmd: true,
        },
        {
          id: 'R3',
          naam: 'Slaapkamer 1',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 18.0,
          verwarmd: true,
        },
        {
          id: 'R4',
          naam: 'Slaapkamer 2',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 15.0,
          verwarmd: true,
        },
        {
          id: 'R5',
          naam: 'Slaapkamer 3',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 12.0,
          verwarmd: true,
        },
        {
          id: 'R6',
          naam: 'Badkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'BAD' },
          oppervlakte: 8.0,
          verwarmd: true,
        },
        {
          id: 'R7',
          naam: 'Zolder',
          soort: { code: 'OVR' },
          detailSoort: { code: 'ZOL' },
          oppervlakte: 15.0,
          verwarmd: false,
        },
        {
          id: 'R8',
          naam: 'Berging',
          soort: { code: 'OVR' },
          detailSoort: { code: 'BER' },
          oppervlakte: 5.0,
          verwarmd: false,
        },
      ],
      energieprestaties: [
        {
          label: 'C',
          soort: { code: 'EP2' },
          status: { code: 'DEF' },
          begindatum: '2022-08-10',
        },
      ],
      wozEenheden: [
        {
          vastgesteldeWaarde: 320000,
          waardepeildatum: '2023-01-01',
        },
      ],
    },
  },
  {
    id: 'nieuwbouw',
    naam: 'Nieuwbouw Appartement',
    beschrijving: 'Modern nieuwbouw appartement van 75m² met hoog energielabel',
    data: {
      id: 'NIEUW-004',
      bouwjaar: 2023,
      adres: {
        straatnaam: 'Nieuwstraat',
        huisnummer: '10',
        huisnummerToevoeging: 'B',
        postcode: '1000AB',
      },
      ruimten: [
        {
          id: 'R1',
          naam: 'Woonkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'WOO' },
          oppervlakte: 32.0,
          verwarmd: true,
        },
        {
          id: 'R2',
          naam: 'Slaapkamer 1',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 16.0,
          verwarmd: true,
        },
        {
          id: 'R3',
          naam: 'Slaapkamer 2',
          soort: { code: 'VTK' },
          detailSoort: { code: 'SLA' },
          oppervlakte: 12.0,
          verwarmd: true,
        },
        {
          id: 'R4',
          naam: 'Keuken',
          soort: { code: 'VTK' },
          detailSoort: { code: 'KEU' },
          oppervlakte: 9.0,
          verwarmd: true,
        },
        {
          id: 'R5',
          naam: 'Badkamer',
          soort: { code: 'VTK' },
          detailSoort: { code: 'BAD' },
          oppervlakte: 6.0,
          verwarmd: true,
        },
      ],
      energieprestaties: [
        {
          label: 'A++++',
          soort: { code: 'EP3' },
          status: { code: 'DEF' },
          begindatum: '2023-01-15',
        },
      ],
      wozEenheden: [
        {
          vastgesteldeWaarde: 380000,
          waardepeildatum: '2024-01-01',
        },
      ],
    },
  },
];
