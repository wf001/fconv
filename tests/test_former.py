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

TESTSETS = [
    # src_format, target_format, src_path, target_format_loader
    (Json, Yaml, JSON_FILE_PATH, yaml.safe_load),
    (Json, Toml, JSON_FILE_PATH, toml.loads),
    (Yaml, Json, YAML_FILE_PATH, json.loads),
    (Yaml, Toml, YAML_FILE_PATH, toml.loads),
    (Toml, Json, TOML_FILE_PATH, json.loads),
    (Toml, Yaml, TOML_FILE_PATH, yaml.safe_load),
]

TESTSETS_WITHARGS = [
    # src_format, target_format, src_path, target_format_loader, in_opt, out_opt
    (Json, Yaml, JSON_FILE_PATH, yaml.safe_load, {"parse_int": float}, {"indent": 2}),
    (Json, Toml, JSON_FILE_PATH, toml.loads, {"parse_int": float}, None),
    (Yaml, Json, YAML_FILE_PATH, json.loads, None, {"indent": 2}),
    # (Yaml, Toml, YAML_FILE_PATH, toml.loads, None, None), #skip as is redundant
    (Toml, Json, TOML_FILE_PATH, json.loads, None, {"indent:2"}),
    # (Toml, Yaml, TOML_FILE_PATH, yaml.safe_load, None, None), #skip as is redundant
]


class TestIntegration:
    @pytest.mark.parametrize(
        "src_format, target_format, src_path, target_format_loader", TESTSETS
    )
    def test_form_file_to_file(
        self, src_format, target_format, src_path, target_format_loader
    ):
        """
        Confirm converting json file to yaml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"

        Former(
            src_format=src_format,
            target_format=target_format,
            src_path=src_path,
            target_path=out_name,
        ).form()

        # testing
        with open(out_name) as f:
            act = target_format_loader(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    @pytest.mark.parametrize(
        "src_format, target_format, src_path, target_format_loader", TESTSETS
    )
    def test_form_file_to_str(
        self, src_format, target_format, src_path, target_format_loader
    ):
        """
        Confirm converting json file to yaml string
        """

        r = Former(
            src_format=src_format,
            target_format=target_format,
            src_path=src_path,
        ).form()

        # testing
        assert type(r) is str
        act = target_format_loader(r)
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    @pytest.mark.parametrize(
        "src_format, target_format, src_path, target_format_loader", TESTSETS
    )
    def test_form_str_to_file(
        self, src_format, target_format, src_path, target_format_loader
    ):
        """
        Confirm converting json string to yaml file
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"

        src_ctx = None
        with open(src_path) as f:
            src_ctx = f.read()

        Former(
            src_format=src_format,
            target_format=target_format,
            target_path=out_name,
        ).form(src_ctx)

        # testing
        with open(out_name) as f:
            act = target_format_loader(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)

    @pytest.mark.parametrize(
        "src_format, target_format, src_path, target_format_loader", TESTSETS
    )
    def test_form_str_to_str(
        self, src_format, target_format, src_path, target_format_loader
    ):
        """
        Confirm converting json string to yaml file
        """
        src_ctx = None
        with open(src_path) as f:
            src_ctx = f.read()

        r = Former(
            src_format=src_format,
            target_format=target_format,
        ).form(src_ctx)

        assert type(r) is str
        act = target_format_loader(r)
        # testing
        assert act["country"] == "Japan"
        assert act["user"][0]["age"] == 10
        assert act["user"][1]["name"] == "Hanako"
        assert act["user"][1]["phone"][0] == "555-666-777"

    @pytest.mark.parametrize(
        "src_format, target_format, src_path, target_format_loader, in_opt, out_opt",
        [
            (
                Json,
                Yaml,
                JSON_FILE_PATH,
                yaml.safe_load,
                {"parse_int": int},
                {"indent": 2},
            ),
        ],
    )
    def test_form_file_to_file_with_opt(
        self, src_format, target_format, src_path, target_format_loader, in_opt, out_opt
    ):
        """
        json to yaml
        """
        dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        out_name = f"{dt}.yaml"

        Former(
            src_format=src_format,
            target_format=target_format,
            src_path=src_path,
            target_path=out_name,
            in_opt=in_opt,
            out_opt=out_opt,
        ).form()

        # testing
        with open(out_name) as f:
            act = target_format_loader(f.read())
            assert act["country"] == "Japan"
            assert act["user"][0]["age"] == 10
            assert act["user"][1]["name"] == "Hanako"
            assert act["user"][1]["phone"][0] == "555-666-777"
        os.remove(out_name)
