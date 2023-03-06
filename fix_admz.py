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

        await client.set_value_by_xpath('Device/Services/BellNetworkCfg/AdvancedDMZ/Enable', False)
        await client.set_value_by_xpath('Device/Services/BellNetworkCfg/AdvancedDMZ/AdvancedDMZhost', ADMZ_MAC)
        await client.set_value_by_xpath('Device/Services/BellNetworkCfg/AdvancedDMZ/Enable', True)

asyncio.run(main())
