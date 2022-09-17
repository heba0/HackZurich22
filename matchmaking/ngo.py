from matchmaking.location import Location
from matchmaking.voluntary_vaccancy import VoluntaryVaccancy
from typing import Any, List, Union


class Ngo:
    def __init__(self, about='', category_list=None, name='', website='', location=None, fan_count=0, ngo_id='',
                 voluntary_vaccancies=None):
        if category_list is None:
            category_list = []
        if voluntary_vaccancies is None:
            voluntary_vaccancies = []
        self.about: str = about
        self.category_list: List[Any] = category_list
        self.name: str = name
        self.website: str = website
        self.location: Union[Location, None] = location
        self.fan_count: int = fan_count
        self.id: str = ngo_id
        self.vv: List[VoluntaryVaccancy] = voluntary_vaccancies
