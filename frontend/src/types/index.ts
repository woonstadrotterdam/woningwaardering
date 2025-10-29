// TypeScript types voor Woningwaardering data modellen

export interface Ruimte {
  id: string;
  naam: string;
  soort: {
    code: 'VTK' | 'OVR'; // VTK = Vertrek, OVR = Overige ruimte
  };
  detailSoort?: {
    code: string; // WOO, SLA, KEU, BAD, BER, etc.
  };
  oppervlakte: number; // in m²
  verwarmd?: boolean;
  verkoeld?: boolean;
}

export interface BouwkundigElement {
  id: string;
  naam: string;
  soort?: {
    code: string;
  };
  detailSoort?: {
    code: string;
  };
  lengte?: number; // Voor aanrechtlengte
}

export interface Energieprestatie {
  soort?: {
    code: string; // EP1, EP2, EP3
  };
  label?: string; // A+++++, A++++, A+++, A++, A+, A, B, C, D, E, F, G
  status?: {
    code: string; // DEF = Definitief
  };
  begindatum?: string;
  einddatum?: string;
  waarde?: number;
}

export interface WOZEenheid {
  vastgesteldeWaarde: number; // in EUR
  waardepeildatum: string; // ISO datum
}

export interface Adres {
  huisnummer?: string;
  postcode?: string;
  straatnaam?: string;
  huisnummerToevoeging?: string;
}

export interface EenhedenEenheid {
  id: string;
  bouwjaar?: number;
  adres?: Adres;
  adresseerbaarObjectBasisregistratie?: {
    bagIdentificatie?: string;
  };
  ruimten?: Ruimte[];
  energieprestaties?: Energieprestatie[];
  wozEenheden?: WOZEenheid[];
}

export interface WoningwaarderingCriterium {
  naam: string;
  meeteenheid?: {
    code: string;
    naam: string;
  };
}

export interface WoningwaarderingItem {
  aantal?: number;
  punten?: number;
  criterium?: WoningwaarderingCriterium;
}

export interface WoningwaarderingGroep {
  criteriumGroep?: {
    stelsel?: {
      code: string;
      naam: string;
    };
    stelselgroep?: {
      code: string;
      naam: string;
    };
  };
  punten?: number;
  woningwaarderingen?: WoningwaarderingItem[];
}

export interface WoningwaarderingResultaat {
  stelsel?: {
    code: string;
    naam: string;
  };
  groepen?: WoningwaarderingGroep[];
  punten?: number;
  maximale_huur?: number;
  opslagpercentage?: number;
  huurprijsopslag?: number;
  maximale_huur_inclusief_opslag?: number;
}

export interface FormData extends EenhedenEenheid {
  peildatum?: string;
}
