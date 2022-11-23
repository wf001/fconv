from fconv.formats.json import Json
from fconv.formats.toml import Toml
from fconv.formats.yaml import Yaml
from fconv.formats.xml import Xml

SUPPORTED_FORMATS = {"json": Json, "yaml": Yaml, "toml": Toml, "xml": Xml}


def get_supported_formats():
    return [k for k in SUPPORTED_FORMATS.keys()]
