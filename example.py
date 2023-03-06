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

        # Print device information of Sagemcom F@st router
#        device_info = await client.get_device_info()
#        print(f"{device_info.id} {device_info.model_name}")

        # Print connected devices
#        devices = await client.get_hosts()

#        for device in devices:
#            if device.active:
#                print(f"{device.id} - {device.name}")

        # Retrieve values via XPath notation, output is a dict
        custom_command_output = await client.get_value_by_xpath('Device/Services/BellNetworkCfg')
       
        dump(custom_command_output)

#        await client.set_value_by_xpath("Device/Services/BellNetworkCfg/SetBridgeMode", "on")


asyncio.run(main())
