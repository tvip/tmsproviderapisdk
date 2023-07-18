from tmsproviderapisdk.tms_extended_model import TmsExtendedModel

class TmsDeviceTypes(TmsExtendedModel):
    _path_url = "/device_types/"

    def __init__(self, device_type: str, id: int = None):
        self.device_type = device_type
        self.id = id

    @staticmethod
    def _dict_to_object(device_type_dict: dict) -> object:
        device_type = TmsDeviceTypes(
            device_type=device_type_dict["device_type"],
            id=device_type_dict["id"]
        )

        return device_type

    def __str__(self):
        return """id:{}, device_type:{}""".format(
            self.id,
            self.device_type
        )
