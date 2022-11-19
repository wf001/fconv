import datetime
import json
import os

import yaml

from former.core import Former
from former.format import Format


class TestFormer:
    def test_form_json_file_to_yaml_file(self):
        """
        json to yaml
        """
        in_name = "tests/assets/sample01.json"
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"tests/assets/{dt}.yaml"

        Former(
            src_format=Format.Json,
            target_format=Format.Yaml,
            src_path=in_name,
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

    def test_form_json_file_to_yaml_file_with_opt(self):
        """
        json to yaml
        """
        in_name = "tests/assets/sample01.json"
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"tests/assets/{dt}.yaml"

        Former(
            src_format=Format.Json,
            target_format=Format.Yaml,
            src_path=in_name,
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

    def test_form_yaml_file_to_json_file(self):
        """
        yaml to json
        """
        in_name = "tests/assets/sample01.yaml"
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"tests/assets/{dt}.json"

        Former(Format.Yaml, Format.Json, src_path=in_name, target_path=out_name).form()

        # testing
        with open(out_name) as f:
            act = json.loads(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    def test_form_yaml_file_to_json_file_with_opt(self):
        """
        yaml to json
        """
        in_name = "tests/assets/sample01.yaml"
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"tests/assets/{dt}.json"

        Former(
            Format.Yaml,
            Format.Json,
            src_path=in_name,
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
