import json
import yaml
import datetime
from abc import ABCMeta, abstractmethod


class IFormat(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        raise Exception()

    @abstractmethod
    def parse(self):
        raise Exception()


class Json(IFormat):
    def load(self, str):
        res =  json.loads(str)
        print(type(res))
        return res

    def parse(self):
        pass


class Yaml(IFormat):
    def load(self):
        pass

    def parse(self, data):
        return yaml.dump(data, Dumper=yaml.CDumper)


class Former:
    def __init__(self, src, target):
        self.src = src
        self.target = target
        self.data = None
        self.df = None

    def former(self):
        self._get_input()
        self._to_dict()
        self._from_dict()
        print(self.data)
        self._send_output()

    def _to_dict(self):
        self.data = self.src().load(self.df)
        print(self.data)

    def _from_dict(self):
        self.data = self.target().parse(self.data)

    def _get_input(self):
        with open('assets/sample01.json') as f:
            self.df = f.read()

    def _send_output(self):
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f = open(f'assets/result-{dt}.yaml', 'x+')
        f.write(self.data)


if __name__ == '__main__':
    f = Former(Json, Yaml)
    f.former()
    print(f.data)
