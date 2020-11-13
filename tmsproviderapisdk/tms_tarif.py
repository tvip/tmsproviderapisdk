from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsTarif(TmsExtendedModel):
    _path_url = "/tarifs/"

    def __init__(self, tarif_name: str, tarif_tag: int, enabled: bool, provider: int = None, id: int = None):

        self.id = id
        self.tarif_name = tarif_name
        self.provider = provider
        self.tarif_tag = tarif_tag
        self.enabled = enabled

    @staticmethod
    def _dict_to_object(tarif_dict: dict) -> object:
        tarif = TmsTarif(
            id=tarif_dict["id"],
            tarif_name=tarif_dict["tarif_name"],
            provider=tarif_dict["provider"],
            tarif_tag=tarif_dict["tarif_tag"],
            enabled=tarif_dict["enabled"]
        )

        return tarif

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", channel: int = None, enabled: bool = None,
                 provider: int = None, tarif_tag: int = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:

        tarifs = super().get_list(start=start, limit=limit, sort=sort, channel=channel, enabled=enabled,
                                  provider=provider, tarif_tag=tarif_tag, quick_search=quick_search)

        return tarifs

    def __str__(self):
        return """id: {}, tarif_name:{}, provider:{}, tarif_tag:{}, enabled:{}""".format(
            self.id,
            self.tarif_name,
            self.provider,
            self.tarif_name,
            self.enabled
        )
