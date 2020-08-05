import requests
import json
from config import BASE_URL, headers


class Provider:

    def __init__(self, provider_id=None, region_tag=None, provider_name=None, provider_comment=None,
                 enabled=False, logo_url=None, devices_per_account_limit=None):

        self.id = provider_id
        self.region_tag = region_tag
        self.provider_name = provider_name
        self.provider_comment = provider_comment
        self.enabled = enabled
        self.logo_url = logo_url
        self.devices_per_account_limit = devices_per_account_limit

    @staticmethod
    def _dict_to_object(provider_dict):
        p = Provider(
            provider_id=provider_dict["id"],
            region_tag=provider_dict["region_tag"],
            provider_name=provider_dict["provider_name"],
            provider_comment=provider_dict["provider_comment"],
            enabled=provider_dict["enabled"],
            logo_url=provider_dict["logo_url"],
            devices_per_account_limit=provider_dict["devices_per_account_limit"]
        )

        return p

    @staticmethod
    def get_provider(provider_id):
        try:
            r = requests.get(BASE_URL + "providers/" + str(provider_id), headers=headers)
        except Exception as e:
            # Fixme: add to logging
            print(e)
            return None

        if r.status_code != 200:
            # Fixme: add to logging
            print("http status code: {}".format(r.status_code))
            return None

        resp = json.loads(r.text)
        p = Provider._dict_to_object(resp)

        return p

    @staticmethod
    def get_providers(start=0, limit=50, sort="", enabled=None, quick_search=""):
        providers = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if enabled:
            query += "&enabled={}".format(enabled)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "providers" + query, headers=headers)
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
            p = Provider._dict_to_object(ra)
            providers.append(p)

        return providers

    def __str__(self):
        return """id: {}, region_tag: {}, provider_name: {}, provider_comment:{}, enabled: {},\
logo_url: {}, devices_per_account_limit: {}""".format(
            self.id,
            self.region_tag,
            self.provider_name,
            self.provider_comment,
            self.enabled,
            self.logo_url,
            self.devices_per_account_limit
        )
