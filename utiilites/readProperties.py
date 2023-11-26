import configparser


def getConfig(path):
    config = configparser.RawConfigParser()
    config.read(path)
    return config
