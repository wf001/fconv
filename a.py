
from former import Former, Format
import datetime
import yaml


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
print(f.form())

