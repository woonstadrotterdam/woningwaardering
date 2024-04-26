from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Energieprestatiesoort(Enum):
    compactheid = Referentiedata(
        code="COM",
        naam="Compactheid",
    )
    """
    De geometrieverhouding (Als/Ag) van de woning: Dit is de verhouding tussen het
    totale verliesoppervlak van het gebouw (Als) en het gebruiksoppervlak (Ag). Dit
    is één van de indicatoren die benodigd zijn voor het bepalen van de maximale
    energieprestatievergoeding (EPV). (https://www.rvo.nl/onderwerpen/wetten-en-rege
    ls-gebouwen/standaard-streefwaarden-woningisolatie)
    """

    energie_index = Referentiedata(
        code="EI",
        naam="Energie-index",
    )
    """
    De tussen 1-1-2015 en 1-1-2021 afgegeven Energie-Index. Officieel hoort bij een
    energie-index geen energielabel, maar in de praktijk wordt in de
    energieprestatie meestal ook een energielabel opgenomen. Dat label is dan
    afgeleid op basis van een tabel met bandbreedtes voor de energie-index.
    """

    primair_energieverbruik_woningbouw = Referentiedata(
        code="EP2",
        naam="Primair energieverbruik - woningbouw",
    )
    """
    Het conform NTA8800 berekende jaarlijkse primair (gebouwgebonden) energiegebruik in
    kWh/m2 gebruiksoppervlak, exclusief eventuele energiemaatregelen op
    gebiedsniveau (EMG). Dit is de optelsom van de het energieverbruik voor
    verwarming, koeling, warmtapwaterbereiding, ventilatoren, verlichting en
    bevochtiging. Dit betreft de EP2 EMG forf. score, waarop het afgegeven
    energielabel met ingang van 1-1-2021 is gebaseerd. Tevens één van de indicatoren
    die benodigd zijn voor het bepalen van de maximale energieprestatievergoeding
    (EPV).
    """

    opgewekte_duurzame_elektriciteit = Referentiedata(
        code="OPG",
        naam="Opgewekte duurzame elektriciteit",
    )
    """
    De totale jaarlijkse hoeveelheid opgewekte hoeveelheid duurzame energie door
    zonnepanelen in kWh/jaar die beschikbaar is voor huishoudelijk gebruik,
    uitgedrukt in kWh elektrische energie per jaar (kWh_e/jr). Dit is één van de
    indicatoren die benodigd zijn voor het bepalen van de maximale
    energieprestatievergoeding (EPV).
    """

    voorlopig_energielabel = Referentiedata(
        code="VEL",
        naam="Voorlopig energielabel",
    )
    """
    Het tot 1-1-2015 door de overheid afgegeven &#39;Oude&#39; energielabel. Dit is geen
    officieel energieprestatiecertificaat. Als er een voorlopig energielabel is
    toegekend zal er geen energie-index of andere waarde bij de energieprestatie
    horen.
    """

    warmtebehoefte_ruimteverwarming = Referentiedata(
        code="WAR",
        naam="Warmtebehoefte ruimteverwarming",
    )
    """
    De volgens de NTA8800 berekende warmtebehoefte voor ruimteverwarming, gegeven het
    woningtype (ook wel: warmtevraag), uitgedrukt in kWh thermische energie per m2
    per jaar (kWh_th/m2/jr). Dit is één van de indicatoren die benodigd zijn voor
    het bepalen van de maximale energieprestatievergoeding (EPV).
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
