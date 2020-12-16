from typing import Optional, List, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel
import hashlib


class TmsAccount(TmsExtendedModel):
    _path_url = '/accounts/'

    def __init__(self, login: str, fullname: str, account_desc: str = "", contract_info: str = "",
                 devices_per_account_limit: int = None, enabled: bool = True, main_address: str = "", pin_md5: str = "",
                 remote_custom_field: str = "", provider: int = None, id: int = None, region_tag=None):

        self.login = login
        self.fullname = fullname
        self.account_desc = account_desc
        self.contract_info = contract_info
        self.devices_per_account_limit = devices_per_account_limit
        self.enabled = enabled
        self.main_address = main_address
        self.pin_md5 = pin_md5
        self.remote_custom_field = remote_custom_field
        self.provider = provider
        self.id = id
        self.region_tag = region_tag

    @staticmethod
    def get_md5_pin(clear_text_password: str) -> str:
        hash_password = hashlib.md5(clear_text_password.encode())
        pin_md5 = hash_password.hexdigest()

        return pin_md5

    @staticmethod
    def _dict_to_object(account_dict: dict) -> object:
        a: TmsAccount = TmsAccount(login=account_dict["login"],
                                   account_desc=account_dict["account_desc"],
                                   contract_info=account_dict["contract_info"],
                                   devices_per_account_limit=account_dict["devices_per_account_limit"],
                                   enabled=account_dict["enabled"],
                                   fullname=account_dict["fullname"],
                                   main_address=account_dict["main_address"],
                                   pin_md5=account_dict["pin_md5"],
                                   remote_custom_field=account_dict["remote_custom_field"],
                                   provider=account_dict["provider"],
                                   id=account_dict["id"],
                                   region_tag=account_dict["region_tag"])

        return a

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, sort: str = "", provider: int = None, enabled: bool = None,
                 login: int = None, remote_custom_field: str = "",
                 quick_search: str = "") -> Optional[Tuple[List[object], int]]:

        accounts: Optional[Tuple[List[object], int]] = super().get_list(start, limit, sort=sort, provider=provider,
                                                                        enabled=enabled, login=login,
                                                                        remote_custom_field=remote_custom_field,
                                                                        quick_search=quick_search)

        return accounts

    def __str__(self):
        return """id:{}, login:{}, fullname:{}, remote_custom_field:{}, pin_md5:{}, contract_info:{},\
 main_address:{}, account_desc:{}, provider:{}, enabled:{}, devices_per_account_limit:{}, region_tag:{}""".format(
            self.id,
            self.login,
            self.fullname,
            self.remote_custom_field,
            self.pin_md5,
            self.contract_info,
            self.main_address,
            self.account_desc,
            self.provider,
            self.enabled,
            self.devices_per_account_limit,
            self.region_tag
        )
