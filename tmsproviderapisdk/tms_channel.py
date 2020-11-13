from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsChannel(TmsBaseModel):
    _path_url = "/channels/"

    def __init__(self, id: int, name: str = "", text_name: str = "", display_number: str = "", logo_url: str = "",
                 enabled: bool = False, time_shift_depth: int = None):

        self.id = id
        self.name = name
        self.text_name = text_name
        self.display_number = display_number
        self.logo_url = logo_url
        self.enabled = enabled
        self.time_shift_depth = time_shift_depth

    @staticmethod
    def _dict_to_object(channel_dict: dict) -> object:
        channel = TmsChannel(
            id=channel_dict["id"],
            name=channel_dict["name"],
            text_name=channel_dict["text_name"],
            display_number=channel_dict["display_number"],
            logo_url=channel_dict["logo_url"],
            enabled=channel_dict["enabled"],
            time_shift_depth=channel_dict["time_shift_depth"]
        )
        return channel

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", tarif: int = None, enabled: bool = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:
        channels = super().get_list(start=start, limit=limit, sort=sort, tarif=tarif, quick_search=quick_search)

        return channels

    def __str__(self):
        return """id:{}, name:{}, text_name:{}, display_number:{}, logo_url:{}, \
            enabled: {}, time_shift_depth: {}""".format(
                self.id,
                self.name,
                self.text_name,
                self.display_number,
                self.logo_url,
                self.enabled,
                self.time_shift_depth
            )
