from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsDeviceSubscription(TmsExtendedModel):
    _path_url = "/device_subscriptions/"

    def __init__(self, device: int, start: str, tarif: int, id: int = None, stop: str = None,
                 time_shift_depth: int = None):

        self.device = device
        self.start = start
        self.tarif = tarif
        self.id = id
        self.stop = stop
        self.time_shift_depth = time_shift_depth

    @staticmethod
    def _dict_to_object(ds_dict: dict) -> object:
        device_subscription = TmsDeviceSubscription(
            device=ds_dict["device"],
            id=ds_dict["id"],
            start=ds_dict["start"],
            stop=ds_dict["stop"],
            tarif=ds_dict["tarif"],
            time_shift_depth=ds_dict["time_shift_depth"]
        )
        return device_subscription

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", device: int = None, tarif: int = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:

        device_subscriptions = super().get_list(start=start, limit=limit, sort=sort, device=device, tarif=tarif,
                                                quick_search=quick_search)

        return device_subscriptions

    def __str__(self):
        return """id:{}, device:{}, start:{}, stop:{}, tarif:{}, time_shift_depth:{}""".format(
            self.id,
            self.device,
            self.start,
            self.stop,
            self.tarif,
            self.time_shift_depth
        )
