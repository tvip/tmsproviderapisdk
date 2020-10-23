from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsAccountSubscription(TmsExtendedModel):
    _path_url = "/account_subscriptions/"

    def __init__(self, account, start, tarif, id=None, stop=None):
        """

        :param account: int
        :param start: string
        :param tarif: int
        :param id: int
        :param stop: string
        """
        self.account = account
        self.start = start
        self.tarif = tarif
        self.id = id
        self.stop = stop

    @staticmethod
    def _dict_to_object(as_dict):
        account_subscription = TmsAccountSubscription(
            account=as_dict["account"],
            id=as_dict["id"],
            start=as_dict["start"],
            stop=as_dict["stop"],
            tarif=as_dict["tarif"]
        )
        return account_subscription

    @classmethod
    def get_list(cls, start=0, limit=50, sort="", account=None, tarif=None, quick_search=""):
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
