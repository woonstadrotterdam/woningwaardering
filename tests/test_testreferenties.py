from pathlib import Path

from tests.testreferenties import MAP, verweesde_testreferenties

TESTS_MAP = Path(__file__).parent


def test_geen_verweesde_testreferenties():
    """Bij elke testreferentie hoort een test.

    Is een test bewust verwijderd of hernoemd, verwijder dan ook zijn
    testreferentie.
    """
    assert verweesde_testreferenties(TESTS_MAP) == []


def test_verweesde_testreferenties(tmp_path):
    (tmp_path / "test_voorbeeld.py").write_text(
        "import pytest\n"
        "\n"
        "\n"
        "def test_enkel():\n"
        "    pass\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "waarde", [pytest.param(1, id="een"), pytest.param(2, id="twee")]\n'
        ")\n"
        "def test_tabel(waarde):\n"
        "    pass\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "pad", [pytest.param(pad, id=pad.stem) for pad in MODELLEN]\n'
        ")\n"
        "def test_model(pad):\n"
        "    pass\n"
    )
    testreferenties = tmp_path / MAP
    testreferenties.mkdir()
    # Bij test_model staan de id's niet letterlijk in de code; elk geval telt.
    bij_een_test = [
        "test_enkel.md",
        "test_tabel[een].md",
        "test_tabel[twee].md",
        "test_model[12006000004].md",
    ]
    verweesd = [
        "test_verwijderd.md",
        "test_tabel[drie].md",
        "test_tabel.md",
        "test_enkel[een].md",
        "test_enkel.txt",
    ]
    for naam in bij_een_test + verweesd:
        (testreferenties / naam).write_text("")

    assert [pad.name for pad in verweesde_testreferenties(tmp_path)] == sorted(verweesd)
