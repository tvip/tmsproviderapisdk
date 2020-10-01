from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsTarifTag(TmsBaseModel):
    _model_url = "/tarif_tags/"

    def __init__(self, enabled, name, provider, id=None, position=None):
        self.enabled = enabled
        self.name = name
        self.provider = provider
        self.id = id
        self.position = position

    @staticmethod
    def _dict_to_object(tarif_tag_dict):
        tarif_tag = TmsTarifTag(
            id=tarif_tag_dict["id"],
            name=tarif_tag_dict["name"],
            enabled=tarif_tag_dict["enabled"],
            provider=tarif_tag_dict["provider"],
            position=tarif_tag_dict["position"]
        )

        return tarif_tag

    @classmethod
    def get_list(cls, start=0, limit=50, sort="", enabled=None, provider=None, quick_search=""):

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