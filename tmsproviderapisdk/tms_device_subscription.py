from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsDeviceSubscription(TmsExtendedModel):
    _path_url = "/device_subscriptions/"

    def __init__(self, device, start, tarif, id=None, stop=None):
        """

        :param device: int
        :param start: string
        :param tarif: int
        :param id: int
        :param stop: string
        """
        self.device = device
        self.start = start
        self.tarif = tarif
        self.id = id
        self.stop = stop

    @staticmethod
    def _dict_to_object(as_dict):
        device_subscription = TmsDeviceSubscription(
            device=as_dict["device"],
            id=as_dict["id"],
            start=as_dict["start"],
            stop=as_dict["stop"],
            tarif=as_dict["tarif"]
        )
        return device_subscription

    @classmethod
    def get_list(cls, start=0, limit=50, sort="", device=None, tarif=None, quick_search=""):

        device_subscriptions = super().get_list(start=start, limit=limit, sort=sort, device=device, tarif=tarif,
                                                quick_search=quick_search)

        return device_subscriptions

    def __str__(self):
        return """id:{}, device:{}, start:{}, stop:{}, tarif:{}""".format(
            self.id,
            self.device,
            self.start,
            self.stop,
            self.tarif
        )
