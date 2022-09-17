from matchmaking.ngo import Ngo
from matchmaking.volunteer import Volunteer
import networkx as nx
from typing import List, Union


class Matchmaking:
    def __init__(self, ngos=None, volunteers=None, network=None):
        if ngos is None:
            ngos = []
        if volunteers is None:
            volunteers = []
        self.ngos: List[Ngo] = ngos
        self.volunteers: List[Volunteer] = volunteers
        self.network: Union[nx.Graph, None] = network


