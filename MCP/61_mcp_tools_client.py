import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    params = StdioServerParameters(
        command="python",
        args=["61_mcp_tools_server.py"]
    )

    async with Client(params) as client:

        tools_result = await client.list_tools()

        print("Available tools:")

        for tool in tools_result.tools:
            print("-", tool.name)

        result = await client.call_tool(
            "multiply_numbers",
            {
                "a": 10,
                "b": 5
            }
        )

        print("\nResult:")
        print(result)


asyncio.run(main())