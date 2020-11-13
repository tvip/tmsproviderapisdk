import json


class Error(Exception):
    pass


class ApiHTTPError(Error):
    def __init__(self, context, status_code, response_text):
        self.context = context
        self.status_code = status_code
        self.response_text = response_text

    def __str__(self):
        message = "Api HTTP Error on {}, http status code: {}".format(
            self.context,
            self.status_code
        )

        if 399 < self.status_code < 500:
            text = json.loads(self.response_text)
            cause = text.get("cause")
            if not cause:
                cause = text.get("error")
            status_code = text.get("statusCode", self.status_code)

            message = "Api HTTP Error on {}, status code: {}, cause: {}".format(
                self.context,
                status_code,
                cause
            )

        return message


class IdEmptyError(Error):

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


class NotJsonDataError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
