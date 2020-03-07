import os
import base64
import uuid
import json


def generate_random_bytes(size):
    return os.urandom(size)


def generate_uuid():
    return uuid.uuid4()


def get_base64(bytes):
    return base64.b64encode(bytes).decode('utf-8')


if __name__ == "__main__":

    key_id = generate_uuid()
    key = generate_random_bytes(16)

    data = {}
    data['key_id_guid'] = str(key_id)
    data['key_id_hex'] = key_id.hex
    data['key_id_b64'] = get_base64(key_id.bytes)
    data['key_hex'] = key.hex()
    data['key_b64'] = get_base64(key)

    with open('key.txt', 'w') as outfile:
        json.dump(data, outfile, indent=1)

    print(json.dumps(data, indent=1))
