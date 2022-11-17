from src.former import Former, Format
import yaml
import json
import os
import datetime


class TestFormer:
    def test_form_json_file_to_yaml_file(self):
        # covert job
        in_name = 'assets/sample01.json'
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out_name = f'assets/{dt}.yaml'

        f = Former(
            Format.Json,
            Format.Yaml,
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
        # covert job
        in_name = 'assets/sample02.yaml'
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out_name = f'assets/{dt}.json'

        f = Former(
            Format.Json,
            Format.Yaml,
            src_path=in_name,
            target_path=out_name
        )
        f.form()

        # testing
        with open(out_name) as f:
            act = json.loads(f.read())
            assert act['country'] == 'Japan'
        os.remove(out_name)
