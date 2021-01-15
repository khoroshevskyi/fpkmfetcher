import os
import json


def check_dir_exsits(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def open_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def seve_b_file(file_name, content):
    print("saving file ...")
    file = open(file_name, 'wb')
    file.write(content)
    file.close()


def save_file(data, path_name):
    print("Saving file: {}".format(path_name))
    file_object = open(path_name, "w+")
    file_object.write(data)
    file_object.close()
    print("File was saved successfully")