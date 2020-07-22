import requests
from config import BASE_URL
from config import headers
import json


class AccountSubscription:

    def __init__(self, account, start, tarif, subscription_id=None, stop=None):
        self.account = account
        self.start = start
        self.tarif = tarif
        self.id = subscription_id
        self.stop = stop

    def create(self):
        account_subscription = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "account_subscriptions", headers=headers, data=account_subscription)
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
        account_s = AccountSubscription._dict_to_object(resp)

        return account_s

    @staticmethod
    def _dict_to_object(as_dict):
        account_subscription = AccountSubscription(
            account=as_dict["account"],
            subscription_id=as_dict["id"],
            start=as_dict["start"],
            stop=as_dict["stop"],
            tarif=as_dict["tarif"]
        )
        return account_subscription

    @staticmethod
    def get_account_subscriptions(start=0, limit=50, sort="", account=None, tarif=None, quick_search=""):

        account_subscriptions = []
        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if account:
            query += "&account={}".format(account)
        if tarif:
            query += "&tarif={}".format(tarif)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "account_subscriptions" + query, headers=headers)
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
            account_subscription = AccountSubscription._dict_to_object(ra)
            account_subscriptions.append(account_subscription)

        return account_subscriptions

    @staticmethod
    def get_account_subscription(subscription_id):
        try:
            r = requests.get(BASE_URL + "account_subscriptions/" + str(subscription_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        account_s = AccountSubscription._dict_to_object(resp)

        return account_s

    @staticmethod
    def delete(subscription_id):
        """

        :type subscription_id: int
        :rtype: int
        """

        try:
            r = requests.delete(BASE_URL + "account_subscriptions/" + str(subscription_id), headers=headers)
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
        return """id:{}, account:{}, start:{}, stop:{}, tarif:{}""".format(
            self.id,
            self.account,
            self.start,
            self.stop,
            self.tarif
        )
