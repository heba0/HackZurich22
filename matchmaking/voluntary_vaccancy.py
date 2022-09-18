from matchmaking.node import Node
from matchmaking.node_type import NodeType
from typing import List


class VoluntaryVaccancy(Node):
    def __init__(self, vv_id='', job_title='', description='', name='', link='', image='', vv_requirements=None):
        if vv_requirements is None:
            vv_requirements = []
        self.id: str = vv_id
        self.name: str = name
        self.description: str = description
        self.job_title: str = job_title
        self.link: str = link
        self.image: str = image
        self.vv_requirements: List[VoluntaryVaccancyRequirements] = []
        super().__init__(node_id=vv_id, node_type=NodeType.VV)

    @staticmethod
    def read_from_dict(list_of_objs):
        return [VoluntaryVaccancy(**{k: elem.get(k, '') for k in elem.keys()}) for elem in list_of_objs]
