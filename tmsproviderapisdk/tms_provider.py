from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsProvider(TmsBaseModel):

    _path_url = "/providers/"

    def __init__(self, id=None, region_tag=None, provider_name=None, provider_comment=None,
                 enabled=False, logo_url=None, devices_per_account_limit=None):
        """

        :param id: int
        :param region_tag: int
        :param provider_name: str
        :param provider_comment: str
        :param enabled: bool
        :param logo_url: string
        :param devices_per_account_limit: int
        """
        self.id = id
        self.region_tag = region_tag
        self.provider_name = provider_name
        self.provider_comment = provider_comment
        self.enabled = enabled
        self.logo_url = logo_url
        self.devices_per_account_limit = devices_per_account_limit

    @staticmethod
    def _dict_to_object(provider_dict):
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
    def get_list(cls, start=0, limit=50, sort="", enabled=None, quick_search=""):
        providers = super().get_list(start=start, limit=limit, sort=sort, enabled=enabled, quick_search=quick_search)

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
