from matchmaking.ai21 import compare_job_titles
from matchmaking.ngo import Ngo
from matchmaking.node_type import NodeType
from matchmaking.volunteer import Volunteer
from matchmaking.voluntary_vaccancy import VoluntaryVaccancy
import networkx as nx
from typing import List, Union
from matchmaking.gpt3 import label_score, get_embedding

class Matchmaking:
    def __init__(self, ngos=None, volunteer_vaccancies=None, volunteers=None, network=None,
                 weight_of_interest_match: float = 0.5, weight_of_job_title_match: float = 0.2):
        if ngos is None:
            ngos = []
        if volunteers is None:
            volunteers = []
        if volunteer_vaccancies is None:
            volunteer_vaccancies = []
        self.ngos: List[Ngo] = Ngo.read_from_dict(ngos)
        self.vvs: List[VoluntaryVaccancy] = VoluntaryVaccancy.read_from_dict(volunteer_vaccancies)
        self.volunteers: List[Volunteer] = Volunteer.read_from_dict(volunteers)
        self.network: Union[nx.Graph, None] = network
        self.weight_of_interest_match = weight_of_interest_match
        self.weight_of_job_title_match = weight_of_job_title_match

    def init_network_nodes(self) -> None:
        if self.network is None:
            self.network = nx.Graph()
        for vv in self.vvs:
            self.add_node_to_network(node_type=NodeType.VV, node=VoluntaryVaccancy(vv_id=vv.id))
        for volunteer in self.volunteers:
            self.add_node_to_network(node_type=NodeType.VOLUNTEER, node=Volunteer(volunteer_id=volunteer.id))

    def add_edge_to_network(self, vv_id: str, volunteer_id: str) -> None:
        assert vv_id in list(self.network.nodes)
        assert self.network.nodes[vv_id]['node_type'] == NodeType.VV
        assert volunteer_id in list(self.network.nodes)
        assert self.network.nodes[volunteer_id]['node_type'] == NodeType.VOLUNTEER
        self.network.add_edge(u_of_edge=volunteer_id, v_of_edge=vv_id)

    def add_node_to_network(self, node_type: NodeType, node: Union[Ngo, Volunteer, VoluntaryVaccancy]) -> None:
        assert node_type in [NodeType.VOLUNTEER, NodeType.VV]
        assert isinstance(node, Volunteer) if node_type == NodeType.VOLUNTEER else True
        assert isinstance(node, VoluntaryVaccancy) if node_type == NodeType.VV else True
        assert node.id not in self.network.nodes
        self.network.add_node(node.id, **node.__dict__)

    def find_ngo_parent(self, vv_id) -> Union[None, Ngo]:
        for ngo in self.ngos:
            if vv_id in ngo.vv_keys:
                return ngo
        return None

    def interest_match(self, v_likes, v_groups, ngo_parent) -> float:
        for like in v_likes:
            if like['name'] == ngo_parent.name:
                return 1
        for group in v_groups:
            if group['name'] == ngo_parent.name:
                return 1
        return 0

    def job_title_match(self, v_job_title, vv_job_title) -> float:
        if len(v_job_title) == 0:
            return 0
        if len(vv_job_title) == 0:
            return 0
        return (compare_job_titles(v_job_title, vv_job_title) - 1) / 3

    @staticmethod
    def similarity_match(ngo_description, v_description, vv_description) -> float:
        opportunity_description = ngo_description + vv_description
        opportunity_embedding = get_embedding(opportunity_description)
        v_embedding = get_embedding(v_description)
        return (label_score(opportunity_embedding, v_embedding) + 1.0) / 2.0

    def calculate_similarity(self, vv: VoluntaryVaccancy, volunteer: Volunteer) -> float:
        vv_description = vv.description
        ngo_parent = self.find_ngo_parent(vv_id=vv.id)
        ngo_description = ngo_parent.about
        v_description = volunteer.about
        v_job_title = volunteer.job_title
        vv_job_title = vv.job_title
        v_likes = volunteer.likes
        v_groups = volunteer.groups
        score_part1 = self.weight_of_interest_match * self.interest_match(v_likes, v_groups, ngo_parent)
        score_part2 = (1 - self.weight_of_interest_match) * self.weight_of_job_title_match \
            * self.job_title_match(v_job_title, vv_job_title)
        score_part3 = (1 - self.weight_of_interest_match) * (1 - self.weight_of_job_title_match) \
            * self.similarity_match(ngo_description, v_description, vv_description)
        return score_part1 + score_part2 + score_part3
