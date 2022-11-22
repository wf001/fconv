from fconv.formats.json import Json
from fconv.formats.toml import Toml
from fconv.formats.yaml import Yaml

SUPPORTED_FORMATS = {"json": Json, "yaml": Yaml, "toml": Toml}


def get_supported_formats():
    return [k for k in SUPPORTED_FORMATS.keys()]
