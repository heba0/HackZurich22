from matchmaking.fb_group import FbGroup
from matchmaking.fb_like import FbLike
from typing import List


class Volunteer:
    def __init__(self):
        self.name: str
        self.id: str
        self.likes: List[FbLike] = []
        self.groups: List[FbGroup] = []
