#from json.decoder import JSONDecodeError

ID_FILE = 'network_id.json'


def get_id():
    int_id=0000
    try:
        int_id = _try_load_id()
    except (FileNotFoundError,ValueError):
        int_id = _create_id()
        _save_id(int_id)
    return _from_int(int_id)


def _from_int(network_id):
    return network_id.to_bytes(2, byteorder="big")


def _create_id():
    import random
    id = random.randint(0, 65534)
    return id


def _try_load_id():
    import json
    with open(ID_FILE, 'r') as fl:
        js = json.load(fl)
        id = js["network_id_int"]
        return id


def _save_id(int_id):
    import json
    with open(ID_FILE, 'w') as fl:
        json.dump({"network_id_int": int_id},fl)
