from src.former import Former, Format
import yaml
import json
import os
import datetime
import pytest


class TestFormer:
    def test_form_json_file_to_yaml_file(self):
        """
        json to yaml
        """
        in_name = 'assets/sample01.json'
        dt = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
        out_name = f'assets/{dt}.yaml'

        f = Former(
            src_format=Format.Json,
            target_format=Format.Yaml,
            src_path=in_name,
            target_path=out_name
        )
        f.form()

        # testing
        with open(out_name) as f:
            act = yaml.safe_load(f.read())
            assert act['country'] == 'Japan'
        os.remove(out_name)

    def test_form_yaml_file_to_json_file(self):
        """
        yaml to json
        """
        in_name = 'assets/sample01.yaml'
        dt = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
        out_name = f'assets/{dt}.json'

        g = Former(
            Format.Yaml,
            Format.Json,
            src_path=in_name,
            target_path=out_name
        )
        g.form()

        # testing
        with open(out_name) as f:
            act = json.loads(f.read())
            assert act['country'] == 'Japan'
        os.remove(out_name)
