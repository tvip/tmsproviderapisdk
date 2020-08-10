import json
import requests
from config import BASE_URL, headers
from Exceptions import TarifIdEmptyError, ApiHTTPError


class Tarif:
    def __init__(self, tarif_name, tarif_tag, enabled, provider=None, tarif_id=None):
        self.id = tarif_id
        self.tarif_name = tarif_name
        self.provider = provider
        self.tarif_tag = tarif_tag
        self.enabled = enabled

    def create(self):
        tarif = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "tarifs", headers=headers, data=tarif)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Create Tarif", r.text)

        resp = json.loads(r.text)
        t = Tarif._dict_to_object(resp)

        return t

    def update(self):
        if self.id is None:
            raise TarifIdEmptyError("Tarif Id cannot be empty")

        tarif = json.dumps(self.__dict__)

        try:
            r = requests.put(BASE_URL + "tarifs/" + str(self.id), headers=headers, data=tarif)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Update Tarif", r.text)

        resp = json.loads(r.text)
        t = Tarif._dict_to_object(resp)

        return t

    def delete(self):
        if self.id is None:
            raise TarifIdEmptyError("Tarif Id can\'t be empty")

        try:
            r = requests.delete(BASE_URL + "tarifs/" + str(self.id), headers=headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Delete Tarif", r.text)

        return r.status_code

    @staticmethod
    def _dict_to_object(tarif_dict):
        tarif = Tarif(
            tarif_id=tarif_dict["id"],
            tarif_name=tarif_dict["tarif_name"],
            provider=tarif_dict["provider"],
            tarif_tag=tarif_dict["tarif_tag"],
            enabled=tarif_dict["enabled"]
        )

        return tarif

    @staticmethod
    def get_tarif(tarif_id):
        try:
            r = requests.get(BASE_URL + "tarifs/" + str(tarif_id), headers=headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get Tarif", r.text)

        resp = json.loads(r.text)
        t = Tarif._dict_to_object(resp)

        return t

    @staticmethod
    def get_tarifs(start=0, limit=50, sort="", channel=None, enabled=None, provider=None,
                   tarif_tag=None, quick_search=""):

        tarifs = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if channel:
            query += "&channel={}".format(channel)
        if enabled:
            query += "&enabled={}".format(enabled)
        if provider:
            query += "&provider={}".format(provider)
        if tarif_tag:
            query += "&tarif_tag={}".format(tarif_tag)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "tarifs" + query, headers=headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get Tarifs", r.text)

        try:
            resp = json.loads(r.text)
        except Exception as e:
            print(e)
            return None

        if not resp.get("data"):
            print("Responce not have data, responce: {}".format(r.text))
            return None

        for ra in resp["data"]:
            tarif = Tarif._dict_to_object(ra)
            tarifs.append(tarif)

        return tarifs

    def __str__(self):
        return """tarif_id: {}, tarif_name:{}, provider:{}, tarif_tag:{}, enabled:{}""".format(
            self.id,
            self.tarif_name,
            self.provider,
            self.tarif_name,
            self.enabled
        )
