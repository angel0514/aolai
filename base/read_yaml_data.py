import yaml
import os


def read_data(filename):
    with open(".\data" + os.sep + filename, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        return data

