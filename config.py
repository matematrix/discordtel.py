import yaml


class Config:
    def __init__(self, json):
        self.__dict__.update(json)

def get_config():
    with open("config.yaml", "r") as config_file:
        try:
            return Config(yaml.load(config_file.read()))
        except Exception as e:
            print(e)
            print("Could not load config")
            exit(1)
