import base64


class TmsConfig:

    def __init__(self, base_url: str, username: str = None, password: str = None, token: str = None):

        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = token
        self.headers = None
        self._configure()

    def _configure(self):
        self.base_url = self.base_url + '/api/provider'

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if self.username and (self.password or self.token):
            if self.password:
                login_password = "{}:{}".format(
                    self.username,
                    self.password
                ).encode()
            if self.token:
                login_password = "{}:{}".format(
                    self.username,
                    self.token
                ).encode()

            key = base64.b64encode(bytes(login_password))
            headers.update({'Authorization': "Basic {}".format(key.decode())})

        self.headers = headers


class TmsConfigHolder:
    _config: object

    @staticmethod
    def config():
        return TmsConfigHolder._config

    @staticmethod
    def apply(config: object):
        TmsConfigHolder._config = config
