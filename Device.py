import requests
from config import BASE_URL, headers
import json
from Exceptions import DeviceIdEmptyError


class Device:

    def __init__(self, unique_id, device_id=None, ipaddr=None, mac=None, remote_custom_field=None, comment=None,
                 last_online=None, last_fw_ver=None, first_online=None, use_nat=False, operation_system=None,
                 udpxy_addr=None, device_type=None, provider=None, account=None):

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

    def create(self):
        device = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "devices", headers=headers, data=device)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print(r.text)
            print("http status code: {}, text: {}".format(r.status_code, r.text))
            return None

        resp = json.loads(r.text)
        d = Device._dict_to_object(resp)

        return d

    def update(self):
        if self.id is None:
            raise DeviceIdEmptyError("Device id can\'t be empty")

        device = json.dumps(self.__dict__)

        try:
            r = requests.put(BASE_URL + "devices/" + str(self.id), headers=headers, data=device)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        d = Device._dict_to_object(resp)

        return d

    def delete(self):
        if self.id is None:
            raise DeviceIdEmptyError("Device id can\'t be empty")

        try:
            r = requests.delete(BASE_URL + "devices/" + str(self.id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        return r.status_code

    @staticmethod
    def get_device(device_id):
        try:
            r = requests.get(BASE_URL + "devices/" + str(device_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        d = Device._dict_to_object(resp)

        return d

    @staticmethod
    def _dict_to_object(device_dict):
        device = Device(
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

    @staticmethod
    def get_devices(account=None, device_type=None, limit=50, provider=None, quick_search=None,
                    remote_custom_field=None, sort=None, start=0, unique_id=None):

        devices = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if account:
            query += "&provider={}".format(account)
        if device_type:
            query += "&enabled={}".format(device_type)
        if provider:
            query += "&login={}".format(provider)
        if quick_search:
            query += "&quick_search={}".format(quick_search)
        if remote_custom_field:
            query += "&remote_custom_field={}".format(remote_custom_field)
        if unique_id:
            query += "&unique_id={}".format(unique_id)

        try:
            r = requests.get(BASE_URL + "devices" + query, headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        try:
            resp = json.loads(r.text)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if not resp.get("data"):
            # Fixme: add to logging
            print("Responce not have data, responce: {}".format(r.text))
            return None

        for ra in resp["data"]:
            d = Device._dict_to_object(ra)
            devices.append(d)

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
