from typing import List, Optional, Tuple
from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsDevice(TmsExtendedModel):
    _path_url = "/devices/"

    def __init__(self, unique_id: str, account: int, device_id: int = None, ipaddr: str = None, mac: str = None,
                 remote_custom_field: str = None, comment: str = None, last_online: str = None, last_fw_ver: str = None,
                 first_online: str = None, use_nat: bool = False, operation_system: str = None, udpxy_addr: str = None,
                 device_type: int = None, provider: int = None):

        self.unique_id = unique_id
        self.account = account
        self.id = device_id
        self.ipaddr = ipaddr
        self.mac = mac
        self.remote_custom_field = remote_custom_field
        self.comment = comment
        self.last_online = last_online
        self.last_fw_ver = last_fw_ver
        self.first_online = first_online
        self.use_nat = use_nat
        self.operation_system = operation_system
        self.udpxy_addr = udpxy_addr
        self.device_type = device_type
        self.provider = provider

    @staticmethod
    def _dict_to_object(device_dict: dict) -> object:
        device = TmsDevice(
            unique_id=device_dict["unique_id"],
            device_id=device_dict["id"],
            ipaddr=device_dict["ipaddr"],
            mac=device_dict["mac"],
            remote_custom_field=device_dict["remote_custom_field"],
            comment=device_dict["comment"],
            last_online=device_dict["last_online"],
            last_fw_ver=device_dict["last_fw_ver"],
            first_online=device_dict["first_online"],
            use_nat=device_dict["use_nat"],
            operation_system=device_dict["operation_system"],
            udpxy_addr=device_dict["udpxy_addr"],
            device_type=device_dict["device_type"],
            provider=device_dict["provider"],
            account=device_dict["account"]
        )

        return device

    @classmethod
    def get_list(cls, account: int = None, device_type: int = None, limit: int = 50, provider: int = None,
                 quick_search: str = "", remote_custom_field: str = None, sort: str = "", start: int = 0,
                 unique_id: str = "") -> Optional[Tuple[List[object], int]]:

        devices = super().get_list(start=start, limit=limit, account=account, device_type=device_type,
                                   provider=provider, quick_search=quick_search,
                                   remote_custom_field=remote_custom_field, sort=sort, unique_id=unique_id)

        return devices

    def __str__(self):
        return """id:{}, ipaddr:{}, mac:{}, unique_id:{}, remote_custom_field: {}, comment: {}, last_online: {}, \
        last_fw_ver: {}, first_online: {}, use_nat: {}, operation_system: {}, \
        udpxy_addr: {}, device_type: {}, provider: {}, account: {}""".format(
            self.id,
            self.ipaddr,
            self.mac,
            self.unique_id,
            self.remote_custom_field,
            self.comment,
            self.last_online,
            self.last_fw_ver,
            self.first_online,
            self.use_nat,
            self.operation_system,
            self.udpxy_addr,
            self.device_type,
            self.provider,
            self.account
        )
