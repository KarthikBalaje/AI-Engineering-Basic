# Agents

## Overview

This directory contains agent-based AI projects that demonstrate how to create and use AI agents with LangChain. Agents can perform tasks by using tools and making decisions based on the context.

## Key Concepts

1. **Agents**: AI systems that can perform tasks by using tools and making decisions.
2. **Tools**: Functions that agents can use to perform specific tasks.
3. **LangChain Agents**: Framework for creating agents that can use tools and make decisions.

## How It Works

The code in `37_agent.py` demonstrates:

1. **Loading Environment Variables**: Uses `.env` file to load API keys and model configurations.
2. **Creating an LLM**: Uses `ChatOpenAI` from LangChain with specified model and temperature.
3. **Defining Tools**: Uses the `@tool` decorator to define two tools: `add_numbers` and `multiply_numbers`.
4. **Creating an Agent**: Uses `create_agent` to create an agent with the LLM and tools.
5. **Invoking the Agent**: Uses the agent to process a user query and return the result.

## Example

The agent is invoked with a user query: "Calculate (10 + 20) * 5." The agent:
- Uses the `add_numbers` tool to calculate 10 + 20 = 30
- Uses the `multiply_numbers` tool to calculate 30 * 5 = 150
- Returns the final answer: "150"

## Files in This Directory

- `37_agent.py`: Basic agent implementation with two tools
- `38_agent_loop.py`: Agent with loop functionality
- `39_agent_vs_chain.py`: Comparison between agent and chain approaches

## Usage

To use this agent:
1. Set up your environment variables in `.env`
2. Run the script
3. The agent will process user queries and return results

This implementation shows how to create a simple agent that can perform mathematical operations using predefined tools.