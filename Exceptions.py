class Error(Exception):
    pass


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
