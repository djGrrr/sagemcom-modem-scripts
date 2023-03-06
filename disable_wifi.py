#!/usr/bin/python3
import asyncio
from sagemcom_api.client import SagemcomClient
from modem_config import *

async def main() -> None:
    async with await modem() as client:
        try:
            await client.login()

        except Exception as exception:  # pylint: disable=broad-except
            print(exception)
            return

        for radio in WIFI_RADIOS:
            await client.set_value_by_xpath("Device/WiFi/Radios/Radio[Alias='" + radio + "']/Enable", False)

asyncio.run(main())
