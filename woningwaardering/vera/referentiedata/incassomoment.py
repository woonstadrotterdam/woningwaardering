from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Incassomoment(Enum):
    incassomoment_1e_dag_van_de_maand = Referentiedata(
        code="001",
        naam="1e dag van de maand",
    )
    """
    1e dag van de maand
    """

    incassomoment_2e_dag_van_de_maand = Referentiedata(
        code="002",
        naam="2e dag van de maand",
    )
    """
    2e dag van de maand
    """

    incassomoment_3e_dag_van_de_maand = Referentiedata(
        code="003",
        naam="3e dag van de maand",
    )
    """
    3e dag van de maand
    """

    incassomoment_4e_dag_van_de_maand = Referentiedata(
        code="004",
        naam="4e dag van de maand",
    )
    """
    4e dag van de maand
    """

    incassomoment_5e_dag_van_de_maand = Referentiedata(
        code="005",
        naam="5e dag van de maand",
    )
    """
    5e dag van de maand
    """

    incassomoment_6e_dag_van_de_maand = Referentiedata(
        code="006",
        naam="6e dag van de maand",
    )
    """
    6e dag van de maand
    """

    incassomoment_7e_dag_van_de_maand = Referentiedata(
        code="007",
        naam="7e dag van de maand",
    )
    """
    7e dag van de maand
    """

    incassomoment_8e_dag_van_de_maand = Referentiedata(
        code="008",
        naam="8e dag van de maand",
    )
    """
    8e dag van de maand
    """

    incassomoment_9e_dag_van_de_maand = Referentiedata(
        code="009",
        naam="9e dag van de maand",
    )
    """
    9e dag van de maand
    """

    incassomoment_10e_dag_van_de_maand = Referentiedata(
        code="010",
        naam="10e dag van de maand",
    )
    """
    10e dag van de maand
    """

    incassomoment_11e_dag_van_de_maand = Referentiedata(
        code="011",
        naam="11e dag van de maand",
    )
    """
    11e dag van de maand
    """

    incassomoment_12e_dag_van_de_maand = Referentiedata(
        code="012",
        naam="12e dag van de maand",
    )
    """
    12e dag van de maand
    """

    incassomoment_13e_dag_van_de_maand = Referentiedata(
        code="013",
        naam="13e dag van de maand",
    )
    """
    13e dag van de maand
    """

    incassomoment_14e_dag_van_de_maand = Referentiedata(
        code="014",
        naam="14e dag van de maand",
    )
    """
    14e dag van de maand
    """

    incassomoment_15e_dag_van_de_maand = Referentiedata(
        code="015",
        naam="15e dag van de maand",
    )
    """
    15e dag van de maand
    """

    incassomoment_16e_dag_van_de_maand = Referentiedata(
        code="016",
        naam="16e dag van de maand",
    )
    """
    16e dag van de maand
    """

    incassomoment_17e_dag_van_de_maand = Referentiedata(
        code="017",
        naam="17e dag van de maand",
    )
    """
    17e dag van de maand
    """

    incassomoment_18e_dag_van_de_maand = Referentiedata(
        code="018",
        naam="18e dag van de maand",
    )
    """
    18e dag van de maand
    """

    incassomoment_19e_dag_van_de_maand = Referentiedata(
        code="019",
        naam="19e dag van de maand",
    )
    """
    19e dag van de maand
    """

    incassomoment_20e_dag_van_de_maand = Referentiedata(
        code="020",
        naam="20e dag van de maand",
    )
    """
    20e dag van de maand
    """

    incassomoment_21e_dag_van_de_maand = Referentiedata(
        code="021",
        naam="21e dag van de maand",
    )
    """
    21e dag van de maand
    """

    incassomoment_22e_dag_van_de_maand = Referentiedata(
        code="022",
        naam="22e dag van de maand",
    )
    """
    22e dag van de maand
    """

    incassomoment_23e_dag_van_de_maand = Referentiedata(
        code="023",
        naam="23e dag van de maand",
    )
    """
    23e dag van de maand
    """

    incassomoment_24e_dag_van_de_maand = Referentiedata(
        code="024",
        naam="24e dag van de maand",
    )
    """
    24e dag van de maand
    """

    incassomoment_25e_dag_van_de_maand = Referentiedata(
        code="025",
        naam="25e dag van de maand",
    )
    """
    25e dag van de maand
    """

    incassomoment_26e_dag_van_de_maand = Referentiedata(
        code="026",
        naam="26e dag van de maand",
    )
    """
    26e dag van de maand
    """

    incassomoment_27e_dag_van_de_maand = Referentiedata(
        code="027",
        naam="27e dag van de maand",
    )
    """
    27e dag van de maand
    """

    incassomoment_28e_dag_van_de_maand = Referentiedata(
        code="028",
        naam="28e dag van de maand",
    )
    """
    28e dag van de maand
    """

    incassomoment_29e_dag_van_de_maand = Referentiedata(
        code="029",
        naam="29e dag van de maand",
    )
    """
    29e dag van de maand
    """

    incassomoment_30e_dag_van_de_maand = Referentiedata(
        code="030",
        naam="30e dag van de maand",
    )
    """
    30e dag van de maand
    """

    incassomoment_31e_dag_van_de_maand = Referentiedata(
        code="031",
        naam="31e dag van de maand",
    )
    """
    31e dag van de maand
    """

    laatste_dag = Referentiedata(
        code="LAA",
        naam="Laatste dag",
    )
    """
    Laatste dag van de maand, door de verwerkende partij (de bank) te bepalen op basis
    van de kalendermaand (28e, 29e, 30e of 31e dag van de maand)
    """

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
