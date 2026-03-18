from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectroldetailsoortReferentiedata(Referentiedata):
    pass


class Projectroldetailsoort(Referentiedatasoort):
    aannemer = ProjectroldetailsoortReferentiedata(
        code="AAN",
        naam="Aannemer",
    )
    """
    Uitvoerende partij die verantwoordelijk is voor de realisatie van bouwkundige en
    installatietechnische werkzaamheden binnen het project.
    """

    administratief_medewerker = ProjectroldetailsoortReferentiedata(
        code="ADM",
        naam="Administratief medewerker",
    )
    """
    Ondersteunt het projectteam met administratie, verslaglegging, documentbeheer en
    communicatieve taken.
    """

    architect = ProjectroldetailsoortReferentiedata(
        code="ARC",
        naam="Architect",
    )
    """
    Verantwoordelijk voor ontwerp, vormgeving en esthetische en functionele uitwerking
    van het project, inclusief toetsing in latere fasen.
    """

    beheercoordinator = ProjectroldetailsoortReferentiedata(
        code="BEH",
        naam="Beheercoördinator",
    )
    """
    Coördineert de overgang van projectresultaten naar de beheerorganisatie. Zorgt voor
    borging van processen, overdracht van documentatie, afspraken over onderhoud en
    exploitatie en bewaakt dat systemen, processen en verantwoordelijkheden goed
    aansluiten op de beheerfase.
    """

    bewoner = ProjectroldetailsoortReferentiedata(
        code="BEW",
        naam="Bewoner",
    )
    """
    Stakeholder die als gebruiker of huurder betrokken is bij participatie, communicatie
    en besluitvorming over ingrepen in het woongebouw.
    """

    bouwkundig_inspecteur = ProjectroldetailsoortReferentiedata(
        code="BOU",
        naam="Bouwkundig inspecteur",
    )
    """
    Voert inspecties, opnames en kwaliteitscontroles uit en adviseert over bouwkundige
    risico’s en uitvoeringskwaliteit.
    """

    budgethouder = ProjectroldetailsoortReferentiedata(
        code="BUD",
        naam="Budgethouder",
    )
    """
    Is bevoegd om financiële besluiten te nemen binnen het project en bewaakt de
    budgetruimte.
    """

    constructeur = ProjectroldetailsoortReferentiedata(
        code="CON",
        naam="Constructeur",
    )
    """
    Maakt constructieve berekeningen, beoordeelt draagconstructies en adviseert over
    veiligheid en uitvoerbaarheid.
    """

    directievoerder = ProjectroldetailsoortReferentiedata(
        code="DIR",
        naam="Directievoerder",
    )
    """
    Vertegenwoordigt de opdrachtgever tijdens de uitvoeringsfase, bewaakt contracten,
    kwaliteit en uitvoering van aannemers.
    """

    fiscalist = ProjectroldetailsoortReferentiedata(
        code="FIS",
        naam="Fiscalist",
    )
    """
    Adviseert het projectteam over fiscale wetgeving, subsidies, BTW-aspecten en
    financiële optimalisaties.
    """

    gemeente_ambtenaar = ProjectroldetailsoortReferentiedata(
        code="GEM",
        naam="Gemeente-ambtenaar",
    )
    """
    Ambtenaar die betrokken is bij vergunningen, bestemmingsplannen, toezicht en
    beleidskaders voor het project.
    """

    jurist = ProjectroldetailsoortReferentiedata(
        code="JUR",
        naam="Jurist",
    )
    """
    Adviseert over juridische vraagstukken, contracten, aanbesteding, risico’s en claims
    binnen het project.
    """

    kostendeskundige = ProjectroldetailsoortReferentiedata(
        code="KOS",
        naam="Kostendeskundige",
    )
    """
    Maakt kostenramingen, begrotingen en toetst financiële consequenties van
    ontwerpkeuzes.
    """

    kwaliteitsmanager = ProjectroldetailsoortReferentiedata(
        code="KWA",
        naam="Kwaliteitsmanager",
    )
    """
    Bewaakt kwaliteitsdoelstellingen, voert audits uit en zorgt dat processen en
    producten voldoen aan vastgestelde normen.
    """

    ontwikkelmanager = ProjectroldetailsoortReferentiedata(
        code="ONT",
        naam="Ontwikkelmanager",
    )
    """
    Stuurt de ontwikkelfase aan, waaronder conceptontwikkeling, programma van eisen,
    haalbaarheid en businesscase.
    """

    opdrachtgever = ProjectroldetailsoortReferentiedata(
        code="OPD",
        naam="Opdrachtgever",
    )
    """
    Draagt eindverantwoordelijkheid voor het project, stelt middelen beschikbaar en
    neemt formele besluiten.
    """

    opzichter = ProjectroldetailsoortReferentiedata(
        code="OPZ",
        naam="Opzichter",
    )
    """
    Toezichthouder die namens de organisatie toezicht houdt op de uitvoering, kwaliteit
    en veiligheid op de bouwplaats.
    """

    projectcontroller = ProjectroldetailsoortReferentiedata(
        code="PCO",
        naam="Projectcontroller",
    )
    """
    Verantwoordelijk voor financiële bewaking, prognoses, rapportages en
    risicobeheersing binnen het project.
    """

    projectleider = ProjectroldetailsoortReferentiedata(
        code="PLE",
        naam="Projectleider",
    )
    """
    Stuurt de dagelijkse operationele uitvoering van het project, coördineert teamleden
    en bewaakt voortgang.
    """

    projectmanager = ProjectroldetailsoortReferentiedata(
        code="PMA",
        naam="Projectmanager",
    )
    """
    Verantwoordelijk voor eindresultaat, planning, budget, kwaliteit en integrale
    projectsturing.
    """

    stuurgroeplid = ProjectroldetailsoortReferentiedata(
        code="STU",
        naam="Stuurgroeplid",
    )
    """
    Neemt namens de organisatie deel aan de stuurgroep. Bewaakt de strategische
    doelstellingen, neemt normenstellende besluiten, beoordeelt voortgang en
    risico’s en stuurt op de randvoorwaarden voor succesvolle projectrealisatie.
    """

    vervangend_projectleider = ProjectroldetailsoortReferentiedata(
        code="VPL",
        naam="Vervangend projectleider",
    )
    """
    Neemt de taken van de projectleider over tijdens diens afwezigheid of op onderdelen
    waarvoor vervanging noodzakelijk is.
    """
