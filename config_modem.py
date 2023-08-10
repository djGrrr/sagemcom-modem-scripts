from sagemcom_api.enums import EncryptionMethod
from sagemcom_api.client import SagemcomClient
import json
import yaml
import os

if os.path.isfile('config.yaml'):
    with open('config.yaml', mode='rb') as file:
        config = yaml.safe_load(file)
        modem = config['modem']
        auth = modem['auth']
        method = str(auth['method']).upper()

        WIFI_RADIOS = modem['wifi_radios'] if 'wifi_radios' in modem else []
        ADMZ_MAC = modem['admz_mac'] if 'admz_mac' in modem else ''


async def modem() -> SagemcomClient:
    return SagemcomClient(
        host = str(auth['host']),
        username = str(auth['user']),
        password = str(auth['pass']),
        authentication_method = EncryptionMethod.SHA512 if method == 'SHA512' else EncryptionMethod.MD5,
        ssl = bool(auth['ssl']),
        keep_keys = True,
    )


def dump(value) -> str:
    print(json.dumps(value, indent = 2))

