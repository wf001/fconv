import datetime
import json
import os

import pytest
import toml
import yaml

from fconv.core import Former
from fconv.formats.json import Json
from fconv.formats.toml import Toml
from fconv.formats.yaml import Yaml

from .fixtures import JSON_FILE_PATH, TOML_FILE_PATH, YAML_FILE_PATH

################
# JSON -> YAML
################


class TestJsonToYamlIntegration:
    def test_form_json_file_to_yaml_file(self):
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

    def test_form_json_file_to_yaml_str(self):
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

    def test_form_json_str_to_yaml_file(self):
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

    def test_form_json_str_to_yaml_str(self):
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

    def test_form_json_file_to_yaml_file_with_opt(self):
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


class TestYamlToJsonIntegration:
    def test_form_yaml_file_to_json_file(self):
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

    def test_form_yaml_file_to_json_str(self):
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

    def test_form_yaml_str_to_json_file(self):
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

    def test_form_yaml_str_to_json_str(self):
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

    def test_form_yaml_file_to_json_file_with_opt(self):
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


################
# JSON -> TOML
################


class TestJsonToTomlIntegration:
    def test_form_json_file_to_toml_file(self):
        """
        Confirm converting json file to toml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        Former(
            src_format=Json,
            target_format=Toml,
            src_path=JSON_FILE_PATH,
            target_path=out_name,
        ).form()

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_json_file_to_toml_str(self):
        """
        Confirm converting json file to toml string
        """

        r = Former(
            src_format=Json,
            target_format=Toml,
            src_path=JSON_FILE_PATH,
        ).form()

        # testing
        assert type(r) is str
        act = toml.loads(r)
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_json_str_to_toml_file(self):
        """
        Confirm converting json string to toml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        src_ctx = None
        with open(JSON_FILE_PATH) as f:
            src_ctx = f.read()

        Former(
            src_format=Json,
            target_format=Toml,
            target_path=out_name,
        ).form(src_ctx)

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_json_str_to_toml_str(self):
        """
        Confirm converting json string to toml file
        """
        src_ctx = None
        with open(JSON_FILE_PATH) as f:
            src_ctx = f.read()

        r = Former(
            src_format=Json,
            target_format=Toml,
        ).form(src_ctx)

        assert type(r) is str
        act = toml.loads(r)
        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    @pytest.mark.skip(reason="needless")
    def test_form_json_file_to_toml_file_with_opt(self):
        """
        json to toml
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        Former(
            src_format=Json,
            target_format=Toml,
            src_path=JSON_FILE_PATH,
            target_path=out_name,
            in_opt={"parse_int": float},
        ).form()

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)


################
# TOML -> JSON
################
class TestTomlToJsonIntegration:
    def test_form_toml_file_to_json_file(self):
        """
        toml to json
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.json"

        Former(Toml, Json, src_path=TOML_FILE_PATH, target_path=out_name).form()

        # testing
        with open(out_name) as f:
            act = json.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_toml_file_to_json_str(self):
        """
        Confirm converting toml file to json string
        """

        r = Former(Toml, Json, src_path=TOML_FILE_PATH).form()

        act = json.loads(r)

        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_toml_str_to_json_file(self):
        """
        Confirm converting toml string to json file
        """

        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.json"
        src_ctx = None

        with open(TOML_FILE_PATH) as f:
            src_ctx = f.read()

        Former(Toml, Json, target_path=out_name).form(src_ctx)

        # testing
        with open(out_name) as f:
            act = json.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_toml_str_to_json_str(self):
        """
        Confirm converting toml string to json string
        """

        src_ctx = None

        with open(TOML_FILE_PATH) as f:
            src_ctx = f.read()

        r = Former(Toml, Json).form(src_ctx)

        act = json.loads(r)

        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_toml_file_to_json_file_with_opt(self):
        """
        toml to json
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.json"

        Former(
            Toml,
            Json,
            src_path=TOML_FILE_PATH,
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


################
# YAML -> TOML
################
class TestYamlToTomlIntegration:
    def test_form_yaml_file_to_toml_file(self):
        """
        Confirm converting yaml file to toml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        Former(
            src_format=Yaml,
            target_format=Toml,
            src_path=YAML_FILE_PATH,
            target_path=out_name,
        ).form()

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_yaml_file_to_toml_str(self):
        """
        Confirm converting yaml file to toml string
        """

        r = Former(
            src_format=Yaml,
            target_format=Toml,
            src_path=YAML_FILE_PATH,
        ).form()

        # testing
        assert type(r) is str
        act = toml.loads(r)
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_yaml_str_to_toml_file(self):
        """
        Confirm converting yaml string to toml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        src_ctx = None
        with open(YAML_FILE_PATH) as f:
            src_ctx = f.read()

        Former(
            src_format=Yaml,
            target_format=Toml,
            target_path=out_name,
        ).form(src_ctx)

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_yaml_str_to_toml_str(self):
        """
        Confirm converting yaml string to toml file
        """
        src_ctx = None
        with open(YAML_FILE_PATH) as f:
            src_ctx = f.read()

        r = Former(
            src_format=Yaml,
            target_format=Toml,
        ).form(src_ctx)

        assert type(r) is str
        act = toml.loads(r)
        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    @pytest.mark.skip(reason="needless")
    def test_form_yaml_file_to_toml_file_with_opt(self):
        """
        yaml to toml
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.toml"

        Former(
            src_format=Yaml,
            target_format=Toml,
            src_path=YAML_FILE_PATH,
            target_path=out_name,
        ).form()

        # testing
        with open(out_name) as f:
            act = toml.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)


class TestTomlToYamlIntegration:
    def test_form_toml_file_to_yaml_file(self):
        """
        toml to yaml
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"

        Former(Toml, Yaml, src_path=TOML_FILE_PATH, target_path=out_name).form()

        # testing
        with open(out_name) as f:
            act = yaml.safe_load(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_toml_file_to_yaml_str(self):
        """
        Confirm converting toml file to yaml string
        """

        r = Former(Toml, Yaml, src_path=TOML_FILE_PATH).form()

        act = yaml.safe_load(r)

        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_toml_str_to_yaml_file(self):
        """
        Confirm converting toml string to yaml file
        """

        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"
        src_ctx = None

        with open(TOML_FILE_PATH) as f:
            src_ctx = f.read()

        Former(Toml, Yaml, target_path=out_name).form(src_ctx)

        # testing
        with open(out_name) as f:
            act = yaml.safe_load(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_toml_str_to_yaml_str(self):
        """
        Confirm converting toml string to yaml string
        """

        src_ctx = None

        with open(TOML_FILE_PATH) as f:
            src_ctx = f.read()

        r = Former(Toml, Yaml).form(src_ctx)

        act = yaml.safe_load(r)

        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    def test_form_toml_file_to_yaml_file_with_opt(self):
        """
        toml to yaml
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"

        Former(
            Toml,
            Yaml,
            src_path=TOML_FILE_PATH,
            target_path=out_name,
            out_opt={"indent": 3},
        ).form()

        # testing
        with open(out_name) as f:
            act = yaml.safe_load(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)
