from src.former import Former
from src.format import Format
import datetime

in_name = 'assets/sample01.json'
dt = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
out_name = f'assets/{dt}.yaml'

res = Former(
    Format.Json,
    Format.Yaml,
    src_path=in_name,
    target_path=out_name,
    out_opt={'indent': 3}
).form()

print(out_name, res, sep="\n")

in_name = 'assets/sample01.yaml'
dt = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
out_name = f'assets/{dt}.json'

res = Former(
    Format.Yaml,
    Format.Json,
    src_path=in_name,
    target_path=out_name,
    out_opt={'indent': 3}
).form()

print(out_name, res, sep="\n")
