from fconv.formats.json import Json
from fconv.formats.yaml import Yaml

SUPPORTED_FORMATS = {"json": Json, "yaml": Yaml}


def get_supported_formats():
    return [k for k in SUPPORTED_FORMATS.keys()]
