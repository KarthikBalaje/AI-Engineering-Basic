import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["57_mcp_fundamentals_server.py"]
    )

    async with Client(server_params) as client:

        print("Connected to MCP server")

        tools_result = await client.list_tools()

        print("\nAvailable tools:")

        for tool in tools_result.tools:
            print(
                "-",
                tool.name,
                ":",
                tool.description
            )

        result = await client.call_tool(
            "get_customer_status",
            {
                "customer_id": 102
            }
        )

        print("\nTool result:")
        print(result)


asyncio.run(main())