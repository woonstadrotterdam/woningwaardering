"""Tests voor criterium-id strategie en invarianten."""

from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    criterium_segment_na_totaal,
    naam_uit_subgroep_criterium_id,
    validate_criterium_ids_in_groep,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class TestCriteriumIdSegmenten:
    def test_blad_ruimte_zonder_totaal(self) -> None:
        cid = str(
            CriteriumId.blad_ruimte(
                Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
                "Space_1",
            )
        )
        assert cid == "oppervlakte_van_vertrekken__Space_1"
        assert "totaal" not in cid

    def test_totaal_deel_prive(self) -> None:
        cid = str(
            CriteriumId.totaal_deel(
                Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 1
            )
        )
        assert cid == "oppervlakte_van_vertrekken__totaal__prive"

    def test_totaal_deel_onzelfstandig(self) -> None:
        cid = str(
            CriteriumId.totaal_deel(
                Woningwaarderingstelselgroep.keuken,
                3,
                GedeeldMetSoort.onzelfstandige_woonruimten,
            )
        )
        assert cid == "keuken__totaal__gedeeld_met__3__onzelfstandige_woonruimten"

    def test_totaal_subgroep_verkoeling_onz_prive(self) -> None:
        cid = str(
            CriteriumId.totaal_subgroep(
                Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                "verwarmde_vertrekken",
                1,
            )
        )
        assert cid == "verkoeling_en_verwarming__totaal__verwarmde_vertrekken__prive"

    def test_totaal_subgroep_verkoeling_zel_zonder_prive(self) -> None:
        cid = str(
            CriteriumId.totaal_subgroep(
                Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                "verwarmde_vertrekken",
                1,
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            )
        )
        assert cid == "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
        assert "prive" not in cid

    def test_totaal_deel_zel_buitenruimten_zonder_prive(self) -> None:
        cid = str(
            CriteriumId.totaal_deel(
                Woningwaarderingstelselgroep.buitenruimten,
                1,
                GedeeldMetSoort.adressen,
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            )
        )
        assert cid == "buitenruimten__totaal"

    def test_totaal_subgroep_zel_gedeeld_adressen(self) -> None:
        cid = str(
            CriteriumId.totaal_subgroep(
                Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
                "verwarmde_vertrekken",
                4,
                GedeeldMetSoort.adressen,
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            )
        )
        assert (
            cid
            == "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__totaal__verwarmde_vertrekken__gedeeld_met__4__adressen"
        )

    def test_totaal_adressen_2d(self) -> None:
        cid = str(
            CriteriumId.totaal_deel(
                Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
                4,
                GedeeldMetSoort.adressen,
            )
        )
        assert (
            cid
            == "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__totaal__gedeeld_met__4__adressen"
        )

    def test_blad_criterium_energie_zonder_totaal(self) -> None:
        cid = str(
            CriteriumId.blad_criterium(
                Woningwaarderingstelselgroep.energieprestatie, "label"
            )
        )
        assert cid == "energieprestatie__label"


class TestNaamEnParse:
    def test_criterium_segment_na_totaal(self) -> None:
        cid = "verkoeling_en_verwarming__totaal__verwarmde_vertrekken__prive"
        assert criterium_segment_na_totaal(cid) == "verwarmde_vertrekken"

    def test_criterium_segment_na_totaal_bucket_only(self) -> None:
        cid = "verkoeling_en_verwarming__totaal__gedeeld_met__2__onzelfstandige_woonruimten"
        assert criterium_segment_na_totaal(cid) is None

    def test_naam_uit_subgroep(self) -> None:
        assert (
            naam_uit_subgroep_criterium_id(
                "verkoeling_en_verwarming__totaal__open_keuken__prive"
            )
            == "Open keuken"
        )


class TestValidateCriteriumIds:
    def _groep_met_twee_niveaus(
        self,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        parent_id = str(
            CriteriumId.totaal_deel(
                Woningwaarderingstelselgroep.buitenruimten,
                2,
                GedeeldMetSoort.adressen,
            )
        )
        child_id = str(
            CriteriumId.blad_ruimte(
                Woningwaarderingstelselgroep.buitenruimten, "Space_1"
            )
        )
        return WoningwaarderingResultatenWoningwaarderingGroep(
            woningwaarderingen=[
                WoningwaarderingResultatenWoningwaardering(
                    punten=5.0,
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=parent_id,
                        naam="Totaal adressen",
                    ),
                ),
                WoningwaarderingResultatenWoningwaardering(
                    punten=1.0,
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=child_id,
                        naam="Balkon",
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=parent_id
                        ),
                    ),
                ),
            ]
        )

    def test_validate_geen_fouten_bij_geldige_groep(self) -> None:
        assert validate_criterium_ids_in_groep(self._groep_met_twee_niveaus()) == []

    def test_validate_dubbel_id(self) -> None:
        groep = self._groep_met_twee_niveaus()
        dup = groep.woningwaarderingen[0].model_copy(deep=True)
        groep.woningwaarderingen.append(dup)
        fouten = validate_criterium_ids_in_groep(groep)
        assert any("Dubbel" in f for f in fouten)

    def test_validate_ontbrekende_parent(self) -> None:
        groep = self._groep_met_twee_niveaus()
        assert groep.woningwaarderingen[1].criterium is not None
        groep.woningwaarderingen[
            1
        ].criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
            id="niet_bestaand__totaal__prive"
        )
        fouten = validate_criterium_ids_in_groep(groep)
        assert any("bestaat niet" in f for f in fouten)


class TestZelGemeenschappelijkeVertrekkenOutput:
    @pytest.fixture
    def groep(self) -> WoningwaarderingResultatenWoningwaarderingGroep:
        from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen import (
            GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
        )
        from woningwaardering.vera.bvg.generated import EenhedenEenheid

        input_path = (
            Path(__file__).resolve().parents[1]
            / "data/zelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen/input/keuken.json"
        )
        eenheid = EenhedenEenheid.model_validate_json(input_path.read_text())

        return GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ).waardeer(eenheid)

    def test_validate_geen_fouten(
        self, groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> None:
        assert validate_criterium_ids_in_groep(groep) == []

    def test_groep_punten_is_som_roots(
        self, groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> None:
        roots = [
            w
            for w in groep.woningwaarderingen or []
            if w.criterium and w.criterium.bovenliggende_criterium is None
        ]
        som_roots = float(
            utils.rond_af_op_kwart(Decimal(str(sum(w.punten or 0 for w in roots))))
        )
        assert groep.punten == pytest.approx(som_roots, abs=0.01)

    def test_blad_naam_zonder_gedeeld_met_suffix(
        self, groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> None:
        for w in groep.woningwaarderingen or []:
            if w.criterium and w.criterium.bovenliggende_criterium is not None:
                assert "(gedeeld met" not in (w.criterium.naam or "")

    def test_adressen_totaal_id_op_blad(
        self, groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> None:
        parent_ids = {
            w.criterium.bovenliggende_criterium.id
            for w in groep.woningwaarderingen or []
            if w.criterium
            and w.criterium.bovenliggende_criterium
            and w.criterium.bovenliggende_criterium.id
            and w.criterium.bovenliggende_criterium.id.endswith("__adressen")
        }
        assert (
            "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__totaal__gedeeld_met__5__adressen"
            in parent_ids
        )
