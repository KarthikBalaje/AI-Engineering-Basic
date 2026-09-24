import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["58_mcp_architecture_server.py"]
    )

    async with Client(server_params) as client:

        print("Connected")

        tools_result = await client.list_tools()

        print("\nServer capabilities:")

        for tool in tools_result.tools:
            print(
                tool.name,
                "-",
                tool.description
            )

        result = await client.call_tool(
            "get_customer",
            {
                "customer_id": 101
            }
        )

        print("\nCustomer:")
        print(result)


asyncio.run(main())