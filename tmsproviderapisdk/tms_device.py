from tmsproviderapisdk.tms_extended_model import TmsExtendedModel


class TmsDevice(TmsExtendedModel):
    _path_url = "/devices/"

    def __init__(self, unique_id, device_id=None, ipaddr=None, mac=None, remote_custom_field=None, comment=None,
                 last_online=None, last_fw_ver=None, first_online=None, use_nat=False, operation_system=None,
                 udpxy_addr=None, device_type=None, provider=None, account=None):
        """

        :param unique_id: str
        :param device_id: int
        :param ipaddr: str
        :param mac: str
        :param remote_custom_field: str
        :param comment: str
        :param last_online: str
        :param last_fw_ver: str
        :param first_online: str
        :param use_nat: bool
        :param operation_system: str
        :param udpxy_addr: str
        :param device_type: int
        :param provider: int
        :param account: int
        """
        self.unique_id = unique_id
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
        self.account = account

    @staticmethod
    def _dict_to_object(device_dict):
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
    def get_list(cls, account=None, device_type=None, limit=50, provider=None, quick_search=None,
                 remote_custom_field=None, sort=None, start=0, unique_id=None):

        devices = super().get_list(start=start, limit=limit, account=account, device_type=device_type,
                                   provider=provider, quick_search=quick_search,
                                   remote_custom_field=remote_custom_field, sort=None, unique_id=None)

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
