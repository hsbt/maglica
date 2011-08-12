import os
import sys
import json

class Config(dict):

    def __getitem__(self, key):
        value = dict.__getitem__(self, key)
        if isinstance(value, dict):
            return self.__class__(value)
        return value

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __repr__(self):
        return '<Config ' + dict.__repr__(self) + '>'


def load():
    config_file = os.path.dirname(sys.argv[0]) + '/../etc/maglica.conf'
    if not os.path.exists(config_file):
        config_file = '/etc/maglica.conf'
        
    config = json.load(file(config_file))
    if config is None:
        config = {}
    config = Config(config)
    return config

