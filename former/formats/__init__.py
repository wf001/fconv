from former.formats.json import Json
from former.formats.yaml import Yaml

SUPPORTED_FORMATS = {"json": Json, "yaml": Yaml}


def get_supported_formats():
    from . import SUPPORTED_FORMATS

    return [k for k in SUPPORTED_FORMATS.keys()]
