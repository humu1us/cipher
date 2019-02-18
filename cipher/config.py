import json
from cipher.fileio import read


class Config:

    def __init__(self, path, passwd):
        conf = read(path, passwd)

        if not conf:
            raise RuntimeError("Cannot load config")

        dict_conf = json.loads(conf)
        self.__dict__.update(dict_conf)
