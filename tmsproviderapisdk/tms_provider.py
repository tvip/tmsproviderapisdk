from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsProvider(TmsBaseModel):

    _path_url = "/providers/"

    def __init__(self, id: int = None, region_tag: int = None, provider_name: str = None, provider_comment: str = None,
                 enabled: bool = False, logo_url: str = None, devices_per_account_limit: int = None):

        self.id = id
        self.region_tag = region_tag
        self.provider_name = provider_name
        self.provider_comment = provider_comment
        self.enabled = enabled
        self.logo_url = logo_url
        self.devices_per_account_limit = devices_per_account_limit

    @staticmethod
    def _dict_to_object(provider_dict: dict) -> object:
        p = TmsProvider(
            id=provider_dict["id"],
            region_tag=provider_dict["region_tag"],
            provider_name=provider_dict["provider_name"],
            provider_comment=provider_dict["provider_comment"],
            enabled=provider_dict["enabled"],
            logo_url=provider_dict["logo_url"],
            devices_per_account_limit=provider_dict["devices_per_account_limit"]
        )

        return p

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", enabled: bool = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:
        providers: Optional[Tuple[List[object], int]] = super().get_list(start=start, limit=limit, sort=sort,
                                                                         enabled=enabled, quick_search=quick_search)

        return providers

    def __str__(self):
        return """id: {}, region_tag: {}, provider_name: {}, provider_comment:{}, enabled: {},\
logo_url: {}, devices_per_account_limit: {}""".format(
            self.id,
            self.region_tag,
            self.provider_name,
            self.provider_comment,
            self.enabled,
            self.logo_url,
            self.devices_per_account_limit
        )
