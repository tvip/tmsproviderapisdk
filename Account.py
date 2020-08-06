from typing import List

import requests
import json
from config import BASE_URL, headers
from Exceptions import ProviderEmptyError, AccountIdEmptyError


class Account:
    def __init__(self, login, account_desc="", contract_info="", devices_per_account_limit=None, enabled=True,
                 fullname="", main_address="", pin_md5="", remote_custom_field="", provider=None, account_id=None):

        self.login = login
        self.fullname = fullname
        self.account_desc = account_desc
        self.contact_info = contract_info
        self.devices_per_account_limit = devices_per_account_limit
        self.enabled = enabled
        self.main_address = main_address
        self.pin_md5 = pin_md5
        self.remote_custom_field = remote_custom_field
        self.provider = provider
        if account_id:
            self.id = account_id

    @staticmethod
    def _dict_to_object(account_dict: dict) -> object:
        # Fixme: change to method get for dict
        a: Account = Account(login=account_dict["login"],
                             account_desc=account_dict["account_desc"],
                             contract_info=account_dict["contract_info"],
                             devices_per_account_limit=account_dict["devices_per_account_limit"],
                             enabled=account_dict["enabled"],
                             fullname=account_dict["fullname"],
                             main_address=account_dict["main_address"],
                             pin_md5=account_dict["pin_md5"],
                             remote_custom_field=account_dict["remote_custom_field"],
                             provider=account_dict["provider"],
                             account_id=account_dict["id"])

        return a

    def create(self):
        account = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "accounts", headers=headers, data=account)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        a = Account._dict_to_object(resp)

        return a

    def update(self):
        if self.id is None:
            raise AccountIdEmptyError("Account Id cannot be empty")
        if self.provider is None:
            raise ProviderEmptyError("Provider cannot be empty")

        account = json.dumps(self.__dict__)

        try:
            r = requests.put(BASE_URL + "accounts/" + str(self.id), headers=headers, data=account)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        a = Account._dict_to_object(resp)

        return a

    def delete(self):
        if self.id is None:
            raise AccountIdEmptyError("Account Id cannot be empty")

        try:
            r = requests.delete(BASE_URL + "accounts/" + str(self.id), headers=headers)
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
    def get_account(account_id):
        try:
            r = requests.get(BASE_URL + "accounts/" + str(account_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        a = Account._dict_to_object(resp)

        return a

    @staticmethod
    def get_accounts(start=0, limit=50, sort="", provider=None, enabled=None, login=None,
                     remote_custom_field="", quick_search=""):
        accounts: List[object] = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if provider:
            query += "&provider={}".format(provider)
        if enabled:
            query += "&enabled={}".format(enabled)
        if login:
            query += "&login={}".format(login)
        if remote_custom_field:
            query += "&remote_custom_field={}".format(remote_custom_field)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "accounts" + query, headers=headers)
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
            a = Account._dict_to_object(ra)
            accounts.append(a)

        return accounts

    def __str__(self):
        return """id:{}, login:{}, fullname{}, remote_custom_field:{}, pin_md5:{}, contract_info:{},\
        main_address:{}, account_desc:{}, provider:{}, enabled:{}, devices_per_account_limit:{}""".format(
            self.id,
            self.login,
            self.fullname,
            self.remote_custom_field,
            self.pin_md5,
            self.contact_info,
            self.main_address,
            self.account_desc,
            self.provider,
            self.enabled,
            self.devices_per_account_limit
        )
