from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsTarif(TmsExtendedModel):
    _path_url = "/tarifs/"

    def __init__(self, tarif_name, tarif_tag, enabled, provider=None, id=None):
        """

        :param tarif_name: str
        :param tarif_tag: int
        :param enabled: bool
        :param provider: int
        :param id: int
        """
        self.id = id
        self.tarif_name = tarif_name
        self.provider = provider
        self.tarif_tag = tarif_tag
        self.enabled = enabled

    @staticmethod
    def _dict_to_object(tarif_dict):
        tarif = TmsTarif(
            id=tarif_dict["id"],
            tarif_name=tarif_dict["tarif_name"],
            provider=tarif_dict["provider"],
            tarif_tag=tarif_dict["tarif_tag"],
            enabled=tarif_dict["enabled"]
        )

        return tarif

    @classmethod
    def get_list(cls, start=0, limit=50, sort="", channel=None, enabled=None, provider=None,
                 tarif_tag=None, quick_search=""):

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
