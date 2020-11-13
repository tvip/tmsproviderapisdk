from typing import Optional, List, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsAccountSubscription(TmsExtendedModel):
    _path_url = "/account_subscriptions/"

    def __init__(self, account: int, start: str, tarif: int, id: int = None, stop: str = None):
        self.account = account
        self.start = start
        self.tarif = tarif
        self.id = id
        self.stop = stop

    @staticmethod
    def _dict_to_object(as_dict: dict) -> object:
        account_subscription = TmsAccountSubscription(
            account=as_dict["account"],
            id=as_dict["id"],
            start=as_dict["start"],
            stop=as_dict["stop"],
            tarif=as_dict["tarif"]
        )
        return account_subscription

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", account: int = None, tarif: int = None,
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:
        account_subscriptions = super().get_list(start=start, limit=limit, sort=sort, account=account,
                                                 tarif=tarif, quick_search=quick_search)

        return account_subscriptions

    def __str__(self):
        return """id:{}, account:{}, start:{}, stop:{}, tarif:{}""".format(
            self.id,
            self.account,
            self.start,
            self.stop,
            self.tarif
        )
