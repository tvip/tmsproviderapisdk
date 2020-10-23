from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsChannel(TmsBaseModel):
    _path_url = "/channels/"

    def __init__(self, id: int, name: str = "", text_name: str = "", display_number: str = "", logo_url: str = "",
                 enabled: bool = False, time_shift_depth: int = None):
        """
        :type id: int
        :type name: str
        :type text_name: str
        :type display_number: str
        :type logo_url: str
        :type enabled: bool
        :type time_shift_depth: int
        """
        self.id = id
        self.name = name
        self.text_name = text_name
        self.display_number = display_number
        self.logo_url = logo_url
        self.enabled = enabled
        self.time_shift_depth = time_shift_depth

    @staticmethod
    def _dict_to_object(channel_dict):
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
    def get_list(cls, start=0, limit=50, sort="", tarif=None, enabled=None, quick_search=""):
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
