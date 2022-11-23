from fconv.formats.json import Json
from fconv.formats.toml import Toml
from fconv.formats.xml import Xml
from fconv.formats.yaml import Yaml

SUPPORTED_FORMATS = {"json": Json, "yaml": Yaml, "toml": Toml, "xml": Xml}


def get_supported_formats():
    return [k for k in SUPPORTED_FORMATS.keys()]
