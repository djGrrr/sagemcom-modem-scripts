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

        custom_command_output = await client.get_value_by_xpath("")
        dump(custom_command_output)


asyncio.run(main())
