import json
import requests
from tmsproviderapisdk.tms_config import TmsConfigHolder
from tmsproviderapisdk.tms_exceptions import ApiHTTPError, IdEmptyError, NotJsonDataError
from tmsproviderapisdk.tms_base_model import TmsBaseModel


class TmsExtendedModel(TmsBaseModel):

    def create(self) -> object:
        json_data = json.dumps(self.__dict__)

        try:
            r = requests.post(TmsConfigHolder.config().base_url + self._path_url,
                              headers=TmsConfigHolder.config().headers,
                              data=json_data)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Create {}".format(self.__class__.__name__), r.status_code, r.text)

        try:
            resp = json.loads(r.text)
        except Exception:
            raise NotJsonDataError("Received non json data")

        o = self._dict_to_object(resp)

        return o

    def update(self) -> object:
        if self.id is None:
            raise IdEmptyError("{} Id cannot be empty".format(self.__class__.__name__))

        model = json.dumps(self.__dict__)

        try:
            r = requests.put(TmsConfigHolder.config().base_url + self._path_url + str(self.id),
                             headers=TmsConfigHolder.config().headers, data=model)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Update {}".format(self.__class__.__name__), r.status_code, r.text)

        try:
            resp = json.loads(r.text)
        except Exception:
            raise NotJsonDataError("Received non json data")

        o = self._dict_to_object(resp)

        return o

    def delete(self) -> int:
        if self.id is None:
            raise IdEmptyError("{} Id cannot be empty".format(self.__class__.__name__))

        try:
            r = requests.delete(TmsConfigHolder.config().base_url + self._path_url + str(self.id),
                                headers=TmsConfigHolder.config().headers)
        except Exception as e:
            print(e)
            return None

        if r.status_code != 200:
            raise ApiHTTPError("Delete {}".format(self.__class__.__name__), r.status_code, r.text)

        return r.status_code
