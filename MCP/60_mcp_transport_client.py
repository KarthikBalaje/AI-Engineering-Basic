import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    params = StdioServerParameters(
        command="python",
        args=["60_mcp_transport_server.py"]
    )

    async with Client(params) as client:

        result = await client.call_tool(
            "hello",
            {
                "name": "Karthik"
            }
        )

        print(result)


asyncio.run(main())