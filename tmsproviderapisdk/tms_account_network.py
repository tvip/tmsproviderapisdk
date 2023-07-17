from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsAccountNetwork(TmsExtendedModel):
    _path_url = "/account_network/"

    def __init__(self, network: str, account: int, id: int = None, description: str = None):
        self.network = network
        self.account = account
        self.id = id
        self.description = description

    @staticmethod
    def _dict_to_object(an_dict: dict) -> object:
        a_n = TmsAccountNetwork(
            network=an_dict["network"],
            account=an_dict["account"],
            id=an_dict["id"],
            description=an_dict["description"]
        )

        return a_n

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", account: int = None, quick_search: str = ""):
        account_networks = super().get_list(start=start, limit=limit, sort=sort, account=account,
                                            quick_search=quick_search)

        return account_networks


    def __str__(self):
        return """id:{}, network:{}, account:{}, description:{}""".format(
            self.id,
            self.network,
            self.account,
            self.description
        )