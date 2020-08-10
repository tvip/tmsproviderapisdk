import json


class Error(Exception):
    pass


class ApiHTTPError(Error):
    def __init__(self, context, text):
        self.context = context
        self.text = text

    def __str__(self):
        text = json.loads(self.text)
        cause = text["cause"]
        status_code = text["statusCode"]

        message = "Api HTTP Error on {}, http status code: {}, cause: {}".format(
            self.context,
            status_code,
            cause
        )

        return message


class AccountIdEmptyError(Error):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ProviderEmptyError(Error):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DeviceIdEmptyError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SubsriptionIdEmptyError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class TarifIdEmptyError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class TarifTagIdEmptyError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
