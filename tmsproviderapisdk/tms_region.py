from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsRegion(TmsBaseModel):
    _path_url = "/regions/"

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @staticmethod
    def _dict_to_object(region_dict: dict) -> object:
        r = TmsRegion(
            id=region_dict["id"],
            name=region_dict["name"]
        )

        return r

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "",
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:
        regions: Optional[Tuple[List[object], int]] = super().get_list(start=start, limit=limit, sort=sort,
                                                                         quick_search=quick_search)

        return regions

    def __str__(self):
        return """id: {}, name: {}""".format(
            self.id,
            self.name
        )