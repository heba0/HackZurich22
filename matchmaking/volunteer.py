from matchmaking.fb_group import FbGroup
from matchmaking.fb_like import FbLike
from matchmaking.node import Node
from typing import List

from matchmaking.node_type import NodeType


class Volunteer(Node):
    def __init__(self, volunteer_id='', fb_id='', name='', likes=None, groups=None, about='', job_title=''):
        if likes is None:
            likes = []
        if groups is None:
            groups = []
        self.name: str = name
        self.id: str = volunteer_id
        self.fb_id: str = fb_id
        self.likes: List[FbLike] = likes
        self.groups: List[FbGroup] = groups
        self.about: str = about
        self.job_title: str = job_title
        super().__init__(node_id=volunteer_id, node_type=NodeType.VOLUNTEER)

    @staticmethod
    def read_from_dict(list_of_objs):
        return [Volunteer(**{k: elem.get(k, '') for k in elem.keys()}) for elem in list_of_objs]
