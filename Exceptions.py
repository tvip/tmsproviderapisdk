class Error(Exception):
    pass


class ProviderEmptyError(Error):

    def __init__(self, message: str) -> object:
        self.message = message

    def __str__(self):
        return self.message


class DeviceIdEmptyError(Error):
    def __init__(self, message: str) -> object:
        self.message = message

    def __str__(self):
        return self.message
