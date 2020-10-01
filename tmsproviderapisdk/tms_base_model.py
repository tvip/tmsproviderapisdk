import json
import requests
from tmsproviderapisdk.tms_config import TmsConfigHolder
from tmsproviderapisdk.tms_exceptions import ApiHTTPError, IdEmptyError
from typing import List, Optional, Tuple


class TmsBaseModel:
    _model_url: str

    def create(self):
        json_data = json.dumps(self.__dict__)

        try:
            r = requests.post(TmsConfigHolder.config().base_url + self._model_url,
                              headers=TmsConfigHolder.config().headers,
                              data=json_data)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Create {}".format(self.__class__.__name__), r.status_code, r.text)

        resp = json.loads(r.text)

        o = self._dict_to_object(resp)

        return o

    def update(self):

        if self.id is None:
            raise IdEmptyError("{} Id cannot be empty".format(self.__class__.__name__))
        # if self.provider is None:
        #     raise ProviderEmptyError("Provider cannot be empty")

        model = json.dumps(self.__dict__)

        try:
            r = requests.put(TmsConfigHolder.config().base_url + self._model_url + str(self.id),
                             headers=TmsConfigHolder.config().headers, data=model)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Update {}".format(self.__class__.__name__), r.status_code, r.text)

        resp = json.loads(r.text)
        o = self._dict_to_object(resp)

        return o

    def delete(self):
        if self.id is None:
            raise IdEmptyError("{} Id cannot be empty".format(self.__class__.__name__))

        try:
            r = requests.delete(TmsConfigHolder.config().base_url + self._model_url + str(self.id),
                                headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Delete {}".format(self.__class__.__name__), r.status_code, r.text)

        return r.status_code

    @classmethod
    def get(cls, id: int) -> object:
        try:
            r = requests.get(TmsConfigHolder.config().base_url + cls._model_url + str(id),
                             headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get {}".format(cls.__name__), r.status_code, r.text)

        resp = json.loads(r.text)
        o = cls._dict_to_object(resp)

        return o

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, **kwargs: any) -> Optional[Tuple[List[None], int]]:
        objects = []

        query = "?start={}&limit={}".format(start, limit)

        for name, value in kwargs.items():
            if value:
                query += "&{}={}".format(name, value)

        try:
            r = requests.get(
                TmsConfigHolder.config().base_url + cls._model_url + query,
                headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get {}".format(cls.__name__), r.status_code, r.text)

        try:
            resp = json.loads(r.text)
        except Exception as e:
            print(e)
            return None

        if not resp.get("data"):
            print("Response not have data, response: {}".format(r.text))
            return None

        for ra in resp["data"]:
            o = cls._dict_to_object(ra)
            objects.append(o)

        total_count = resp["total"]

        return objects, total_count

    @staticmethod
    def _dict_to_object(dict_model):
        pass
