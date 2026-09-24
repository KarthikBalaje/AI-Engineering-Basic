import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with Client(params) as client:

        print("Connected to MCP Server")

        # -------------------------------
        # Discover Tools
        # -------------------------------

        tools = await client.list_tools()

        print("\nTOOLS")

        for tool in tools.tools:
            print(
                "-",
                tool.name,
                ":",
                tool.description
            )

        # -------------------------------
        # Discover Resources
        # -------------------------------

        resources = await client.list_resources()

        print("\nRESOURCES")

        for resource in resources.resources:
            print(
                "-",
                resource.uri
            )

        # -------------------------------
        # Discover Prompts
        # -------------------------------

        prompts = await client.list_prompts()

        print("\nPROMPTS")

        for prompt in prompts.prompts:
            print(
                "-",
                prompt.name,
                ":",
                prompt.description
            )


asyncio.run(main())