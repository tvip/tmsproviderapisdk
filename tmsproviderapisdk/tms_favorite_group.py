from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsFavoriteGroup(TmsBaseModel):
    _path_url = "/favorite_group/"

    def __init__(self, id: int, name: str = "", description: str = "", channels: List = None):

        self.id = id
        self.name = name

    @staticmethod
    def _dict_to_object(favorite_group_dict: dict) -> object:
        favorite_group = TmsFavoriteGroup(
            id=favorite_group_dict["id"],
            name=favorite_group_dict["name"],
        )
        return favorite_group

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", quick_search: str = "") -> Optional[Tuple[List[object], int]]:
        favorite_groups = super().get_list(start=start, limit=limit, sort=sort, quick_search=quick_search)

        return favorite_groups

    def __str__(self):
        return """id:{}, name:{}""".format(
                self.id,
                self.name,
            )