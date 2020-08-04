from config import BASE_URL, headers
import requests
import json


class Channels:

    def __init__(self, channel_id, name="", text_name="", display_number="", logo_url="", enabled=False,
                 time_shift_depth=None):
        self.id = channel_id
        self.name = name
        self.text_name = text_name
        self.display_number = display_number
        self.logo_url = logo_url
        self.enabled = enabled
        self.time_shift_depth = time_shift_depth

    @staticmethod
    def _dict_to_object(channel_dict):
        channel = Channels(
            channel_id=channel_dict["id"],
            name=channel_dict["name"],
            text_name=channel_dict["text_name"],
            display_number=channel_dict["display_number"],
            logo_url=channel_dict["logo_url"],
            enabled=channel_dict["enabled"],
            time_shift_depth=channel_dict["time_shift_depth"]
        )
        return channel

    @staticmethod
    def get_channel(channel_id):
        try:
            r = requests.get(BASE_URL + "channels/" + str(channel_id), headers=headers)
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
        c = Channels._dict_to_object(resp)

        return c

    @staticmethod
    def get_channels(start=0, limit=50, sort="", tarif=None, quick_search=""):
        channels = []

        query = "?start={}&limit={}".format(start, limit)

        if sort:
            query += "&sort={}".format(sort)
        if tarif:
            query += "&tarif={}".format(tarif)
        if quick_search:
            query += "&quick_search={}".format(quick_search)

        try:
            r = requests.get(BASE_URL + "channels", headers=headers)
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
            channel = Channels._dict_to_object(ra)
            channels.append(channel)

        return channels

    def __str__(self):
        return """id:{}, name:{}, text_name:{}, display_number:{}, logo_url:{}, \
            enabled: {}, time_shift_depth: {}""".format(
                self.id,
                self.name,
                self.text_name,
                self.display_number,
                self.logo_url,
                self.enabled,
                self.time_shift_depth
            )
