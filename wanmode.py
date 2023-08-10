#!/usr/bin/env python3

import asyncclick as click
from enum import Enum
from sagemcom_api.client import SagemcomClient
from sagemcom_api.enums import EncryptionMethod


XPATH_DEVICE_SERVICES_BELLNETWORKCFG_WANMODE = 'Device/Services/BellNetworkCfg/WanMode'


class EnumChoice(click.Choice):
    def __init__(self, enum: Enum, case_sensitive=False):
        self.__enum = enum
        super().__init__(choices=[item.value for item in enum], case_sensitive=case_sensitive)

    def convert(self, value, param, ctx):
        if value is None or isinstance(value, Enum):
            return value

        converted_str = super().convert(value, param, ctx)
        return self.__enum(converted_str)


@click.command()
@click.option('-H', '--host', default='192.168.2.1', help='Hostname or host IP')
@click.option('-u', '--username', default='admin', help='Administrator username')
@click.option('-p', '--password', required=True, help='Administrator password')
@click.option('-a', '--authentication-method',
              default=EncryptionMethod.SHA512, type=EnumChoice(EncryptionMethod),
              help='Authentication method')
async def main(host: str, username: str, password: str, authentication_method: EncryptionMethod) -> None:
    async with SagemcomClient(**locals(), ssl=True, keep_keys=True) as client:
        try:
            await client.login()

            wanmode = await client.get_value_by_xpath(XPATH_DEVICE_SERVICES_BELLNETWORKCFG_WANMODE)
        except Exception as e:
            print(e)
        else:
            print(f"WAN Mode: {wanmode}")

if __name__ == '__main__':
    main(_anyio_backend='asyncio')

