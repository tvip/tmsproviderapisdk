from Exceptions import SubsriptionIdEmptyError
import json
from config import BASE_URL, headers
import requests


class DeviceSubscription:

    def __init__(self, device, start, tarif, subscription_id=None, stop=None):
        self.device = device
        self.start = start
        self.tarif = tarif
        self.id = subscription_id
        self.stop = stop

    def create(self):
        device_subscription = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "device_subscriptions", headers=headers, data=device_subscription)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        print(resp)
        device_s = DeviceSubscription._dict_to_object(resp)

        return device_s

    @staticmethod
    def _dict_to_object(as_dict):
        device_subscription = DeviceSubscription(
            device=as_dict["device"],
            subscription_id=as_dict["id"],
            start=as_dict["start"],
            stop=as_dict["stop"],
            tarif=as_dict["tarif"]
        )
        return device_subscription

    @staticmethod
    def get_device_subscriptions(start=0, limit=50, sort="", device=None, tarif=None, quick_search=""):

        device_subscriptions = []
        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if device:
            query += "&device={}".format(device)
        if tarif:
            query += "&tarif={}".format(tarif)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "device_subscriptions" + query, headers=headers)
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
            device_subscription = DeviceSubscription._dict_to_object(ra)
            device_subscriptions.append(device_subscription)

        return device_subscriptions

    @staticmethod
    def get_device_subscription(subscription_id):
        try:
            r = requests.get(BASE_URL + "device_subscriptions/" + str(subscription_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        device_s = DeviceSubscription._dict_to_object(resp)

        return device_s

    def delete(self):
        if self.id is None:
            raise SubsriptionIdEmptyError("Subsription Id can\'t be empty")
        try:
            r = requests.delete(BASE_URL + "device_subscriptions/" + str(self.id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        return r.status_code

    def __str__(self):
        return """id:{}, device:{}, start:{}, stop:{}, tarif:{}""".format(
            self.id,
            self.device,
            self.start,
            self.stop,
            self.tarif
        )
