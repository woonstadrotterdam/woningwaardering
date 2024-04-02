from woningwaardering.stelsels.utils import vind_yaml_bestanden


def test_vind_yaml_bestanden():
    directory = "./woningwaardering/stelsels/config/"
    gevonden_yaml_bestanden = vind_yaml_bestanden(directory)
    assert len(gevonden_yaml_bestanden) > 0
