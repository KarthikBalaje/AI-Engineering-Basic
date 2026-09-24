import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with Client(params) as client:

        result = await client.call_tool(
            "get_customer_status",
            {
                "customer_id": 102
            }
        )

        print("Tool result:")
        print(result)


asyncio.run(main())