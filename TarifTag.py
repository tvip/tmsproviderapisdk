import requests
import json
from config import BASE_URL, headers
from Exceptions import TarifTagIdEmptyError


class TarifTag:
    def __init__(self, enabled, name, provider, tag_id=None, position=None):
        self.enabled = enabled
        self.name = name
        self.provider = provider
        self.id = tag_id
        self.position = position

    def create(self):
        tarif_tag = json.dumps(self.__dict__)

        try:
            r = requests.post(BASE_URL + "tarif_tags", headers=headers, data=tarif_tag)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        t = TarifTag._dict_to_object(resp)

        return t

    def update(self):
        if self.id is None:
            raise TarifTagIdEmptyError("Tarif Id can\'t be empty")

        tarif_tag = json.dumps(self.__dict__)

        try:
            r = requests.put(BASE_URL + "tarif_tags/" + str(self.id), headers=headers, data=tarif_tag)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        t = TarifTag._dict_to_object(resp)

        return t

    def delete(self):
        if self.id is None:
            raise TarifTagIdEmptyError("Tarif Id can\'t be empty")

        try:
            r = requests.delete(BASE_URL + "tarif_tags/" + str(self.id), headers=headers)
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
    def _dict_to_object(tarif_tag_dict):
        tarif_tag = TarifTag(
            tag_id=tarif_tag_dict["id"],
            name=tarif_tag_dict["name"],
            enabled=tarif_tag_dict["enabled"],
            provider=tarif_tag_dict["provider"],
            position=tarif_tag_dict["position"]
        )

        return tarif_tag

    @staticmethod
    def get_tarif_tag(tarif_tag_id):
        try:
            r = requests.get(BASE_URL + "tarif_tags/" + str(tarif_tag_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        t = TarifTag._dict_to_object(resp)

        return t

    @staticmethod
    def get_tarif_tags(start=0, limit=50, sort="", enabled=None, provider=None, quick_search=""):

        tarif_tags = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if enabled:
            query += "&enabled={}".format(enabled)
        if provider:
            query += "&provider={}".format(provider)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "tarif_tags" + query, headers=headers)
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
            tarif_tag = TarifTag._dict_to_object(ra)
            tarif_tags.append(tarif_tag)

        return tarif_tags

    def __str__(self):
        return """id: {}, name: {}, enabled: {}, provider: {}, position: {}""".format(
            self.id,
            self.name,
            self.enabled,
            self.provider,
            self.position
        )
