import json
import os

FILE = "usage.json"


def init_usage():

    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({}, f)


def load_usage():

    with open(FILE, "r") as f:
        return json.load(f)


def save_usage(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def can_generate(client_name, limit=5):

    data = load_usage()

    if client_name not in data:
        data[client_name] = 0

    if data[client_name] >= limit:
        return False

    return True


def add_usage(client_name):

    data = load_usage()

    if client_name not in data:
        data[client_name] = 0

    data[client_name] += 1

    save_usage(data)


def get_usage(client_name):

    data = load_usage()

    return data.get(client_name, 0)