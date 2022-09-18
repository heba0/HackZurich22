from matchmaking.location import Location
from matchmaking.node import Node
from matchmaking.node_type import NodeType
from typing import Any, List, Union


class Ngo(Node):
    def __init__(self, about='', category_list=None, name='', website='', location=None, fan_count=0, ngo_id='',
                 voluntary_vaccancy_keys=None):
        if category_list is None:
            category_list = []
        if voluntary_vaccancy_keys is None:
            voluntary_vaccancy_keys = []
        self.about: str = about
        self.category_list: List[Any] = category_list
        self.name: str = name
        self.website: str = website
        self.location: Union[Location, None] = location
        self.fan_count: int = fan_count
        self.id: str = ngo_id
        self.vv_keys: List[str] = voluntary_vaccancy_keys
        super().__init__(node_id=ngo_id, node_type=NodeType.NGO)

    @staticmethod
    def read_from_dict(list_of_objs):
        return [Ngo(**{k: elem.get(k, '') for k in elem.keys()}) for elem in list_of_objs]
