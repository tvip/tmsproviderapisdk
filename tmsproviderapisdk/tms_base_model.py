import json
import requests
from tmsproviderapisdk.tms_config import TmsConfigHolder
from tmsproviderapisdk.tms_exceptions import ApiHTTPError, NotJsonDataError
from typing import List, Optional, Tuple


class TmsBaseModel:
    _path_url: str

    @classmethod
    def get(cls, id):
        """

        :param id: int
        :return: object
        """
        try:
            r = requests.get(TmsConfigHolder.config().base_url + cls._path_url + str(id),
                             headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get {}".format(cls.__name__), r.status_code, r.text)

        try:
            resp = json.loads(r.text)
        except Exception:
            raise NotJsonDataError("Received non json data")

        o = cls._dict_to_object(resp)

        return o

    @classmethod
    def get_list(cls, start: int = 0, limit: int = 50, **kwargs: any) -> Optional[Tuple[List[object], int]]:
        objects = []

        query = "?start={}&limit={}".format(start, limit)

        for name, value in kwargs.items():
            if value != '' and value is not None:
                query += "&{}={}".format(name, value)

        try:
            r = requests.get(
                TmsConfigHolder.config().base_url + cls._path_url + query,
                headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Get {}".format(cls.__name__), r.status_code, r.text)

        try:
            resp = json.loads(r.text)
        except Exception:
            raise NotJsonDataError("Received non json data")

        if not resp.get("data"):
            print("Response not have data, response: {}".format(r.text))
            return None

        for ra in resp["data"]:
            o = cls._dict_to_object(ra)
            objects.append(o)

        total_count = resp["total"]

        return objects, total_count

    @staticmethod
    def _dict_to_object(dict_model: dict) -> object:
        pass
