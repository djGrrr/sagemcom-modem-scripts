#!/usr/bin/python3
import asyncio
from sagemcom_api.client import SagemcomClient
from config_modem import *

async def main() -> None:
    async with await modem() as client:
        try:
            await client.login()

        except Exception as exception:  # pylint: disable=broad-except
            print(exception)
            return

        await client.set_value_by_xpath('Device/Services/BellNetworkCfg/VoiceAllowedWANModes', 'ftth,gpon,xgspon')

asyncio.run(main())
