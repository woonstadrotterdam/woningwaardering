#!/usr/bin/env python3
"""
Unit tests voor de voorzieningen correctie functionaliteit.
"""

import pytest

from woningwaardering.stelsels.gedeelde_logica.voorzieningen_correctie import (
    _corrigeer_douche,
    _corrigeer_wastafel,
    _heeft_douche_of_bad,
    _heeft_wastafel,
    corrigeer_eenheid_zonder_aanrecht,
    corrigeer_eenheid_zonder_toilet,
    corrigeer_voorzieningen_eenheid,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
)


class TestVoorzieningenCorrectie:
    """Test class voor voorzieningen correctie functionaliteit."""

    def _maak_ruimte(
        self,
        detail_soort=Ruimtedetailsoort.badkamer,
        installaties=None,
        bouwkundige_elementen=None,
    ):
        return EenhedenRuimte(
            id="test_ruimte",
            naam="Test Ruimte",
            detail_soort=detail_soort,
            installaties=installaties or [],
            bouwkundige_elementen=bouwkundige_elementen or [],
        )

    def _maak_eenheid(self, ruimten):
        return EenhedenEenheid(id="test_eenheid", ruimten=ruimten)

    # Tests voor _heeft_wastafel
    @pytest.mark.parametrize(
        "installaties,expected",
        [
            ([Installatiesoort.wastafel], True),
            ([], False),
            ([Installatiesoort.douche], False),
        ],
    )
    def test_heeft_wastafel_met_installaties(self, installaties, expected):
        """Test dat _heeft_wastafel een wastafel detecteert."""
        ruimte = self._maak_ruimte(installaties=installaties)
        assert _heeft_wastafel(ruimte) is expected

    def test_heeft_wastafel_met_bouwkundig_element(self):
        """Test dat _heeft_wastafel een wastafel als bouwkundig element detecteert."""
        bouwkundige_elementen = [
            BouwkundigElementenBouwkundigElement(
                id="wastafel_1",
                naam="Wastafel",
                detail_soort=Bouwkundigelementdetailsoort.wastafel,
            )
        ]
        ruimte = self._maak_ruimte(bouwkundige_elementen=bouwkundige_elementen)
        assert _heeft_wastafel(ruimte) is True

    # Tests voor _heeft_douche_of_bad
    @pytest.mark.parametrize(
        "installaties,expected",
        [
            ([Installatiesoort.douche], True),
            ([Installatiesoort.bad], True),
            ([Installatiesoort.douche, Installatiesoort.bad], True),
            ([], False),
            ([Installatiesoort.wastafel], False),
        ],
    )
    def test_heeft_douche_of_bad_met_installaties(self, installaties, expected):
        """Test dat _heeft_douche_of_bad een douche of bad detecteert."""
        ruimte = self._maak_ruimte(installaties=installaties)
        assert _heeft_douche_of_bad(ruimte) is expected

    @pytest.mark.parametrize(
        "detail_soort,expected",
        [
            (Bouwkundigelementdetailsoort.douche, True),
            (Bouwkundigelementdetailsoort.bad, True),
        ],
    )
    def test_heeft_douche_of_bad_met_bouwkundig_element(self, detail_soort, expected):
        """Test dat _heeft_douche_of_bad een douche of bad als bouwkundig element detecteert."""
        bouwkundige_elementen = [
            BouwkundigElementenBouwkundigElement(
                id="test_element", naam="Test Element", detail_soort=detail_soort
            )
        ]
        ruimte = self._maak_ruimte(bouwkundige_elementen=bouwkundige_elementen)
        assert _heeft_douche_of_bad(ruimte) is expected

    # Tests voor _corrigeer_wastafel
    def test_corrigeer_wastafel_voegt_toe_wanneer_ontbreekt(self):
        """Test dat _corrigeer_wastafel precies één wastafel toevoegt wanneer deze ontbreekt."""
        ruimte = self._maak_ruimte(installaties=[])
        _corrigeer_wastafel(ruimte)
        assert Installatiesoort.wastafel in ruimte.installaties
        assert ruimte.installaties.count(Installatiesoort.wastafel) == 1

    def test_corrigeer_wastafel_voegt_geen_duplicaat_toe(self):
        """Test dat _corrigeer_wastafel geen duplicaat toevoegt wanneer wastafel al aanwezig is."""
        ruimte = self._maak_ruimte(installaties=[Installatiesoort.wastafel])
        oorspronkelijk_aantal = len(ruimte.installaties)
        _corrigeer_wastafel(ruimte)
        assert len(ruimte.installaties) == oorspronkelijk_aantal
        assert ruimte.installaties.count(Installatiesoort.wastafel) == 1

    # Tests voor _corrigeer_douche
    def test_corrigeer_douche_voegt_toe_wanneer_ontbreekt(self):
        """Test dat _corrigeer_douche precies één douche toevoegt wanneer deze ontbreekt."""
        ruimte = self._maak_ruimte(installaties=[])
        _corrigeer_douche(ruimte)
        assert Installatiesoort.douche in ruimte.installaties
        assert ruimte.installaties.count(Installatiesoort.douche) == 1

    @pytest.mark.parametrize(
        "bestaande_installaties",
        [
            [Installatiesoort.douche],
            [Installatiesoort.bad],
            [Installatiesoort.douche, Installatiesoort.bad],
        ],
    )
    def test_corrigeer_douche_voegt_geen_duplicaat_toe(self, bestaande_installaties):
        """Test dat _corrigeer_douche geen douche toevoegt wanneer douche of bad al aanwezig is."""
        ruimte = self._maak_ruimte(installaties=bestaande_installaties)
        oorspronkelijk_aantal = len(ruimte.installaties)
        oorspronkelijk_douche_count = ruimte.installaties.count(Installatiesoort.douche)
        oorspronkelijk_bad_count = ruimte.installaties.count(Installatiesoort.bad)

        _corrigeer_douche(ruimte)

        assert len(ruimte.installaties) == oorspronkelijk_aantal
        assert (
            ruimte.installaties.count(Installatiesoort.douche)
            == oorspronkelijk_douche_count
        )
        assert (
            ruimte.installaties.count(Installatiesoort.bad) == oorspronkelijk_bad_count
        )

    # Tests voor corrigeer_voorzieningen_eenheid
    @pytest.mark.parametrize(
        "detail_soort",
        [
            Ruimtedetailsoort.badkamer,
            Ruimtedetailsoort.badkamer_met_toilet,
        ],
    )
    def test_corrigeer_voorzieningen_eenheid_badkamer_zonder_voorzieningen(
        self, detail_soort
    ):
        """Test dat corrigeer_voorzieningen_eenheid precies één wastafel en één douche toevoegt aan badkamer zonder voorzieningen."""
        badkamer = self._maak_ruimte(detail_soort=detail_soort, installaties=[])
        eenheid = self._maak_eenheid([badkamer])

        corrigeer_voorzieningen_eenheid(eenheid)

        assert badkamer.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer.installaties.count(Installatiesoort.douche) == 1

    def test_corrigeer_voorzieningen_eenheid_geen_duplicaten_met_bestaande_voorzieningen(
        self,
    ):
        """Test dat corrigeer_voorzieningen_eenheid geen duplicaten toevoegt aan badkamer met bestaande voorzieningen."""
        badkamer = self._maak_ruimte(
            installaties=[
                Installatiesoort.wastafel,
                Installatiesoort.douche,
                Installatiesoort.staand_toilet,
            ]
        )
        eenheid = self._maak_eenheid([badkamer])

        oorspronkelijk_aantal = len(badkamer.installaties)
        corrigeer_voorzieningen_eenheid(eenheid)

        assert len(badkamer.installaties) == oorspronkelijk_aantal
        assert badkamer.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer.installaties.count(Installatiesoort.douche) == 1
        assert badkamer.installaties.count(Installatiesoort.staand_toilet) == 1

    def test_corrigeer_voorzieningen_eenheid_geen_badkamer_ruimten(self):
        """Test dat corrigeer_voorzieningen_eenheid geen voorzieningen toevoegt aan andere ruimten."""
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, installaties=[]
        )
        eenheid = self._maak_eenheid([woonkamer])

        corrigeer_voorzieningen_eenheid(eenheid)
        assert len(woonkamer.installaties) == 0

    # Edge cases
    def test_corrigeer_voorzieningen_eenheid_lege_ruimten_lijst(self):
        """Test dat corrigeer_voorzieningen_eenheid correct omgaat met eenheid zonder ruimten."""
        eenheid = self._maak_eenheid([])
        # Should not raise an exception
        corrigeer_voorzieningen_eenheid(eenheid)

    def test_corrigeer_voorzieningen_eenheid_ruimte_zonder_detail_soort(self):
        """Test dat corrigeer_voorzieningen_eenheid correct omgaat met ruimte zonder detail_soort."""
        ruimte = self._maak_ruimte(detail_soort=None, installaties=[])
        eenheid = self._maak_eenheid([ruimte])

        # Should not raise an exception
        corrigeer_voorzieningen_eenheid(eenheid)
        assert len(ruimte.installaties) == 0

    def test_corrigeer_voorzieningen_eenheid_voegt_geen_dubbele_installaties_toe(self):
        """Test dat corrigeer_voorzieningen_eenheid geen dubbele installaties toevoegt bij meerdere aanroepen."""
        badkamer = self._maak_ruimte(installaties=[])
        eenheid = self._maak_eenheid([badkamer])

        # Eerste aanroep
        corrigeer_voorzieningen_eenheid(eenheid)
        eerste_aantal = len(badkamer.installaties)

        # Tweede aanroep - zou geen extra installaties moeten toevoegen
        corrigeer_voorzieningen_eenheid(eenheid)
        tweede_aantal = len(badkamer.installaties)

        assert eerste_aantal == tweede_aantal
        assert badkamer.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer.installaties.count(Installatiesoort.douche) == 1

    def test_corrigeer_voorzieningen_eenheid_behoudt_bestaande_installaties(self):
        """Test dat corrigeer_voorzieningen_eenheid bestaande installaties behoudt en niet overschrijft."""
        # Test met bestaande installaties die niet gerelateerd zijn aan badkamer
        bestaande_installaties = [
            Installatiesoort.douchewand,
            Installatiesoort.handdoekenradiator,
        ]
        badkamer = self._maak_ruimte(installaties=bestaande_installaties)
        eenheid = self._maak_eenheid([badkamer])

        corrigeer_voorzieningen_eenheid(eenheid)

        # Controleer dat bestaande installaties behouden zijn
        assert Installatiesoort.douchewand in badkamer.installaties
        assert Installatiesoort.handdoekenradiator in badkamer.installaties
        # En dat nieuwe installaties zijn toegevoegd
        assert Installatiesoort.wastafel in badkamer.installaties
        assert Installatiesoort.douche in badkamer.installaties

    def test_corrigeer_voorzieningen_eenheid_werkt_met_meerdere_ruimten(self):
        """Test dat corrigeer_voorzieningen_eenheid correct werkt met meerdere ruimten."""
        badkamer1 = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer, installaties=[]
        )
        badkamer2 = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer_met_toilet, installaties=[]
        )
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, installaties=[]
        )

        eenheid = self._maak_eenheid([badkamer1, badkamer2, woonkamer])

        corrigeer_voorzieningen_eenheid(eenheid)

        # Beide badkamers moeten voorzieningen hebben
        assert badkamer1.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer1.installaties.count(Installatiesoort.douche) == 1
        assert badkamer2.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer2.installaties.count(Installatiesoort.douche) == 1

        # Woonkamer mag geen badkamer voorzieningen hebben
        assert badkamer1.installaties.count(Installatiesoort.wastafel) == 1
        assert badkamer1.installaties.count(Installatiesoort.douche) == 1
        assert woonkamer.installaties.count(Installatiesoort.wastafel) == 0
        assert woonkamer.installaties.count(Installatiesoort.douche) == 0

    # Tests voor corrigeer_eenheid_zonder_toilet
    def test_corrigeer_eenheid_zonder_toilet_voegt_toe_aan_badkamer(self):
        """Test dat corrigeer_eenheid_zonder_toilet staand_toilet toevoegt aan badkamer wanneer eenheid geen toilet heeft."""
        badkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer, installaties=[]
        )
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, installaties=[]
        )
        eenheid = self._maak_eenheid([badkamer, woonkamer])

        corrigeer_eenheid_zonder_toilet(eenheid, Installatiesoort.staand_toilet)

        assert Installatiesoort.staand_toilet in badkamer.installaties
        assert badkamer.installaties.count(Installatiesoort.staand_toilet) == 1

    def test_corrigeer_eenheid_zonder_toilet_voegt_geen_toilet_toe_wanneer_al_aanwezig(
        self,
    ):
        """Test dat corrigeer_eenheid_zonder_toilet geen toilet toevoegt wanneer er al een toilet in een andere ruimte is."""
        badkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer, installaties=[]
        )
        toiletruimte = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.toiletruimte,
            installaties=[Installatiesoort.staand_toilet],
        )
        eenheid = self._maak_eenheid([badkamer, toiletruimte])

        corrigeer_eenheid_zonder_toilet(eenheid, Installatiesoort.staand_toilet)

        assert Installatiesoort.staand_toilet not in badkamer.installaties
        assert len(badkamer.installaties) == 0

    def test_corrigeer_eenheid_zonder_toilet_voegt_geen_toilet_toe_zonder_badkamer(
        self,
    ):
        """Test dat corrigeer_eenheid_zonder_toilet geen toilet toevoegt wanneer er geen badkamer is."""
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, installaties=[]
        )
        eenheid = self._maak_eenheid([woonkamer])

        corrigeer_eenheid_zonder_toilet(eenheid, Installatiesoort.staand_toilet)

        assert len(woonkamer.installaties) == 0

    # Tests voor corrigeer_eenheid_zonder_aanrecht
    def test_corrigeer_eenheid_zonder_aanrecht_voegt_toe_aan_woonkamer(self):
        """Test dat corrigeer_eenheid_zonder_aanrecht aanrecht toevoegt aan woonkamer wanneer eenheid geen aanrecht heeft."""
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, bouwkundige_elementen=[]
        )
        badkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer, bouwkundige_elementen=[]
        )
        eenheid = self._maak_eenheid([woonkamer, badkamer])

        corrigeer_eenheid_zonder_aanrecht(eenheid, 1000)

        assert len(woonkamer.bouwkundige_elementen) == 1
        aanrecht = woonkamer.bouwkundige_elementen[0]
        assert aanrecht.detail_soort == Bouwkundigelementdetailsoort.aanrecht
        assert aanrecht.lengte == 1000

    def test_corrigeer_eenheid_zonder_aanrecht_voegt_geen_aanrecht_toe_wanneer_al_aanwezig(
        self,
    ):
        """Test dat corrigeer_eenheid_zonder_aanrecht geen aanrecht toevoegt wanneer er al een aanrecht in een andere ruimte is."""
        woonkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.woonkamer, bouwkundige_elementen=[]
        )
        keuken = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.keuken,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    id="aanrecht_1",
                    naam="Aanrecht",
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                    lengte=1200,
                )
            ],
        )
        eenheid = self._maak_eenheid([woonkamer, keuken])

        corrigeer_eenheid_zonder_aanrecht(eenheid, 1000)

        assert len(woonkamer.bouwkundige_elementen) == 0

    def test_corrigeer_eenheid_zonder_aanrecht_voegt_geen_aanrecht_toe_zonder_woonkamer(
        self,
    ):
        """Test dat corrigeer_eenheid_zonder_aanrecht geen aanrecht toevoegt wanneer er geen woonkamer is."""
        badkamer = self._maak_ruimte(
            detail_soort=Ruimtedetailsoort.badkamer, bouwkundige_elementen=[]
        )
        eenheid = self._maak_eenheid([badkamer])

        corrigeer_eenheid_zonder_aanrecht(eenheid, 1000)

        assert len(badkamer.bouwkundige_elementen) == 0
