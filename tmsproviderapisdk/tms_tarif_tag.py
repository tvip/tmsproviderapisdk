from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsTarifTag(TmsExtendedModel):
    _path_url = "/tarif_tags/"

    def __init__(self, enabled: bool, name: str, provider: int, id: int = None, position: int = None):

        self.enabled = enabled
        self.name = name
        self.provider = provider
        self.id = id
        self.position = position

    @staticmethod
    def _dict_to_object(tarif_tag_dict: dict) -> object:
        tarif_tag = TmsTarifTag(
            id=tarif_tag_dict["id"],
            name=tarif_tag_dict["name"],
            enabled=tarif_tag_dict["enabled"],
            provider=tarif_tag_dict["provider"],
            position=tarif_tag_dict["position"]
        )

        return tarif_tag

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", enabled: bool = None, provider: int = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:

        tarif_tags = super().get_list(start=start, limit=limit, sort=sort, enabled=enabled, provider=provider,
                                      quick_search=quick_search)

        return tarif_tags

    def __str__(self):
        return """id: {}, name: {}, enabled: {}, provider: {}, position: {}""".format(
            self.id,
            self.name,
            self.enabled,
            self.provider,
            self.position
        )
