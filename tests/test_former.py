import datetime
import json
import os

import yaml

from fconv.core import Former
from fconv.formats.json import Json
from fconv.formats.yaml import Yaml

from .fixtures import JSON_FILE_PATH, YAML_FILE_PATH

################
# JSON -> YAML
################


def test_form_json_file_to_yaml_file():
    """
    Confirm converting json file to yaml file
    """
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.yaml"

    Former(
        src_format=Json,
        target_format=Yaml,
        src_path=JSON_FILE_PATH,
        target_path=out_name,
    ).form()

    # testing
    with open(out_name) as f:
        act = yaml.safe_load(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)


def test_form_json_file_to_yaml_str():
    """
    Confirm converting json file to yaml string
    """

    r = Former(
        src_format=Json,
        target_format=Yaml,
        src_path=JSON_FILE_PATH,
    ).form()

    # testing
    assert type(r) is str
    act = yaml.safe_load(r)
    assert act["country"] == "Japan"
    assert act["user"][0]["age"] == 10
    assert act["user"][1]["name"] == "Hanako"
    assert act["user"][1]["phone"][0] == "555-666-777"


def test_form_json_str_to_yaml_file():
    """
    Confirm converting json string to yaml file
    """
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.yaml"

    src_ctx = None
    with open(JSON_FILE_PATH) as f:
        src_ctx = f.read()

    Former(
        src_format=Json,
        target_format=Yaml,
        target_path=out_name,
    ).form(src_ctx)

    # testing
    with open(out_name) as f:
        act = yaml.safe_load(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)


def test_form_json_str_to_yaml_str():
    """
    Confirm converting json string to yaml file
    """
    src_ctx = None
    with open(JSON_FILE_PATH) as f:
        src_ctx = f.read()

    r = Former(
        src_format=Json,
        target_format=Yaml,
    ).form(src_ctx)

    assert type(r) is str
    act = yaml.safe_load(r)
    # testing
    assert act["country"] == "Japan"
    assert act["user"][0]["age"] == 10
    assert act["user"][1]["name"] == "Hanako"
    assert act["user"][1]["phone"][0] == "555-666-777"


def test_form_json_file_to_yaml_file_with_opt():
    """
    json to yaml
    """
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.yaml"

    Former(
        src_format=Json,
        target_format=Yaml,
        src_path=JSON_FILE_PATH,
        target_path=out_name,
        in_opt={"parse_int": float},
        out_opt={"indent": 2},
    ).form()

    # testing
    with open(out_name) as f:
        act = yaml.safe_load(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)


################
# YAML -> JSON
################


def test_form_yaml_file_to_json_file():
    """
    yaml to json
    """
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.json"

    Former(Yaml, Json, src_path=YAML_FILE_PATH, target_path=out_name).form()

    # testing
    with open(out_name) as f:
        act = json.loads(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)


def test_form_yaml_file_to_json_str():
    """
    Confirm converting yaml file to json string
    """

    r = Former(Yaml, Json, src_path=YAML_FILE_PATH).form()

    act = json.loads(r)

    # testing
    assert act["country"] == "Japan"
    assert act["user"][0]["age"] == 10
    assert act["user"][1]["name"] == "Hanako"
    assert act["user"][1]["phone"][0] == "555-666-777"


def test_form_yaml_str_to_json_file():
    """
    Confirm converting yaml string to json file
    """

    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.json"
    src_ctx = None

    with open(YAML_FILE_PATH) as f:
        src_ctx = f.read()

    Former(Yaml, Json, target_path=out_name).form(src_ctx)

    # testing
    with open(out_name) as f:
        act = json.loads(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)


def test_form_yaml_str_to_json_str():
    """
    Confirm converting yaml string to json string
    """

    src_ctx = None

    with open(YAML_FILE_PATH) as f:
        src_ctx = f.read()

    r = Former(Yaml, Json).form(src_ctx)

    act = json.loads(r)

    # testing
    assert act["country"] == "Japan"
    assert act["user"][0]["age"] == 10
    assert act["user"][1]["name"] == "Hanako"
    assert act["user"][1]["phone"][0] == "555-666-777"


def test_form_yaml_file_to_json_file_with_opt():
    """
    yaml to json
    """
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    out_name = f"{dt}.json"

    Former(
        Yaml,
        Json,
        src_path=YAML_FILE_PATH,
        target_path=out_name,
        out_opt={"indent": 3},
    ).form()

    # testing
    with open(out_name) as f:
        act = json.loads(f.read())
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"
    os.remove(out_name)
