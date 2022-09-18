from matchmaking.node_type import NodeType
from typing import Union


class Node:
    def __init__(self, node_id: str = '', node_type: Union[NodeType, None] = None):
        self.id: str = node_id
        self.node_type: Union[NodeType, None] = node_type
