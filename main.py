import os
import asyncio
from dotenv import load_dotenv

from click import command
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio


#Define MCP server
mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m","mcp_server_fetch"]
)

# Load environment variables from .env file
load_dotenv()

#Create AI agent
agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    mcp_servers=[mcp_fetch_server]
)

#main async function
async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("extract the content and list the affected products version: https://confluence.atlassian.com/security/security-bulletin-december-11-2025-1689616574.html")
        output = result.output
        return output

#run main function
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)

