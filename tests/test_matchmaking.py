import json
import unittest
from matchmaking import matchmaking
from matchmaking.voluntary_vaccancy import VoluntaryVaccancy


def get_dummy_volunteer_vaccancies():
    with open('assets/dummy_data/vv.json') as f:
        return json.load(f)['vvs']


def get_dummy_volunteers():
    with open('assets/dummy_data/volunteer.json') as f:
        return json.load(f)['volunteers']


def get_dummy_ngos():
    with open('assets/dummy_data/ngo.json') as f:
        return json.load(f)['ngos']


class MyTestCase(unittest.TestCase):
    def test_adding_edge_with_non_existing_vv_id_throws_error(self):
        m = matchmaking.Matchmaking()
        m.init_network_nodes()
        with self.assertRaises(AssertionError):
            m.add_edge_to_network(vv_id='-1', volunteer_id='-1')

    def test_adding_edge_with_non_existing_volunteer_id_throws_error(self):
        volunteer_vaccancies = get_dummy_volunteer_vaccancies()
        m = matchmaking.Matchmaking(volunteer_vaccancies=volunteer_vaccancies)
        m.init_network_nodes()
        with self.assertRaises(AssertionError):
            m.add_edge_to_network(vv_id='1', volunteer_id='-1')

    def test_calculate_similarity(self):
        vs = get_dummy_volunteers()
        ngos = get_dummy_ngos()
        vvs = get_dummy_volunteer_vaccancies()
        m = matchmaking.Matchmaking(volunteers=vs, volunteer_vaccancies=vvs, ngos=ngos)
        m.init_network_nodes()
        assert m.calculate_similarity(vv=m.vvs[0], volunteer=m.volunteers[0]) > 0.5


if __name__ == '__main__':
    unittest.main()
