import json

DATA_PATH = r"C:\Users\there\OneDrive\Documents\Scripts\culinary-mcp\data"

# FILE UTILS


def read_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def write_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


# FILE PATH UTILS


def get_file_path(file_name):
    return f"{DATA_PATH}/{file_name}.json"


# LIST UTILS


def get_list(file_name):
    file_path = get_file_path(file_name)
    list = read_file(file_path)
    return ", ".join(list)


def add_to_list(file_name, item):
    file_path = get_file_path(file_name)
    list = read_file(file_path)
    list.append(item)
    list.sort()
    write_file(file_path, list)


def remove_from_list(file_name, item):
    file_path = get_file_path(file_name)
    list = read_file(file_path)
    list.remove(item)
    write_file(file_path, list)
