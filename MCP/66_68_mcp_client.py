import asyncio

from mcp import Client
from mcp import StdioServerParameters


async def main():

    # ========================================================
    # MCP SERVER PARAMETERS
    # ========================================================

    server_params = StdioServerParameters(
        command="python",
        args=["66_68_mcp_server.py"]
    )


    # ========================================================
    # CONNECT TO MCP SERVER
    # ========================================================

    async with Client(server_params) as client:

        print(
            "Connected to MCP Server"
        )


        # ====================================================
        # DISCOVER TOOLS
        # ====================================================

        tools = await client.list_tools()

        print(
            "\nAvailable MCP tools:"
        )

        for tool in tools.tools:

            print(
                "-",
                tool.name
            )


        # ====================================================
        # READ MCP RESOURCE
        # ====================================================

        print(
            "\nReading support policy..."
        )

        policy = await client.read_resource(
            "policy://customer-support"
        )

        print(policy)


        # ====================================================
        # CALL SAFE TOOL
        # ====================================================

        print(
            "\nGetting customer 102..."
        )

        customer = await client.call_tool(
            "get_customer",
            {
                "customer_id": 102
            }
        )

        print(
            "Customer result:"
        )

        print(customer)


        # ====================================================
        # TRY SENSITIVE OPERATION WITHOUT APPROVAL
        # ====================================================

        print(
            "\nAttempting status update WITHOUT approval..."
        )

        result = await client.call_tool(
            "update_customer_status",
            {
                "customer_id": 102,
                "status": "Active",
                "approved": False
            }
        )

        print(
            "Result:"
        )

        print(result)


        # ====================================================
        # SENSITIVE OPERATION WITH APPROVAL
        # ====================================================

        print(
            "\nExecuting status update WITH approval..."
        )

        result = await client.call_tool(
            "update_customer_status",
            {
                "customer_id": 102,
                "status": "Active",
                "approved": True
            }
        )

        print(
            "Result:"
        )

        print(result)


asyncio.run(main())