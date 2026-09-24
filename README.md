# AI Engineering Basics

This repository is a set of focused Python examples for learning LLM application development. Each numbered script demonstrates one concept and can generally be run directly from its own directory after installing that directory's `requirements.txt`.

## Setup

Several examples load configuration from a local `.env` file. Start with the adjacent `.env.example` file where available and provide the variables required by that folder. The OpenRouter examples use `OPENROUTER_API_KEY`; the LangChain and LangGraph examples usually use `BASE_URL`, `MODEL`, `API_KEY`, and `TEMPERATURE`.

```powershell
cd "LLM Basic\01_basic_llm"
pip install -r requirements.txt
python main.py
```

## Script guide

### Agents

| Script | What it demonstrates |
| --- | --- |
| [37_agent.py](<Agents/37_agent.py>) | Creates a LangChain agent with `add_numbers` and `multiply_numbers` tools, then asks it to solve an arithmetic task. |
| [38_agent_loop.py](<Agents/38_agent_loop.py>) | Runs the arithmetic agent and prints each message in its execution loop, including tool calls and arguments. |
| [39_agent_vs_chain.py](<Agents/39_agent_vs_chain.py>) | Builds a fixed prompt → model → string parser chain to contrast a deterministic chain with an agent workflow. |

### LangChain Fundamentals

| Script | What it demonstrates |
| --- | --- |
| [15_chat_model.py](<LangChain Fundamentals/15_chat_model.py>) | Instantiates `ChatOpenAI` and sends a single prompt. |
| [16_messages.py](<LangChain Fundamentals/16_messages.py>) | Sends explicit system and human message objects to a chat model. |
| [17_prompt_template.py](<LangChain Fundamentals/17_prompt_template.py>) | Uses `ChatPromptTemplate` to fill a topic variable before invoking the model. |
| [18_lcel.py](<LangChain Fundamentals/18_lcel.py>) | Connects a prompt and model with LangChain Expression Language (LCEL). |
| [19_parser.py](<LangChain Fundamentals/19_parser.py>) | Shows string, JSON, comma-separated list, and Pydantic output parsers. |
| [20_runnables.py](<LangChain Fundamentals/20_runnables.py>) | Composes two sequential runnables: explain a topic, then summarize the explanation. |
| [20_runnable_parallel.py](<LangChain Fundamentals/20_runnable_parallel.py>) | Uses `RunnableParallel` to produce an explanation and an interview question at the same time. |
| [20_runnable_branch.py](<LangChain Fundamentals/20_runnable_branch.py>) | Uses `RunnableBranch` to choose an interview-answer chain or an explanatory chain from the question text. |

### LangGraph Fundamentals

| Script | What it demonstrates |
| --- | --- |
| [40_state.py](<LangGraph Fundamentals/40_state.py>) | Defines a typed graph state and passes it through explain and summarize nodes. |
| [41_nodes.py](<LangGraph Fundamentals/41_nodes.py>) | Combines LLM nodes with a normal Python node that counts the words in an explanation. |
| [42_edges.py](<LangGraph Fundamentals/42_edges.py>) | Builds a simple linear graph with explicit `START`, intermediate, and `END` edges. |
| [43_conditional_routing.py](<LangGraph Fundamentals/43_conditional_routing.py>) | Classifies a question and conditionally routes it to a technical or beginner-friendly answer node. |
| [44_memory_checkpoint.py](<LangGraph Fundamentals/44_memory_checkpoint.py>) | Compiles a chatbot graph with `MemorySaver` and a thread ID for checkpointed state. |
| [45_human_in_the_loop.py](<LangGraph Fundamentals/45_human_in_the_loop.py>) | Pauses a graph for a human approval decision, then resumes it with `Command`. |
| [47_model_routing.py](<LangGraph Fundamentals/47_model_routing.py>) | Classifies a request as simple or complex and selects a faster or more capable model. |
| [48_model_fallback.py](<LangGraph Fundamentals/48_model_fallback.py>) | Demonstrates a primary-model call with a backup model in an exception handler. |
| [49_multi_agent_system.py](<LangGraph Fundamentals/49_multi_agent_system.py>) | Chains research, coding, and supervisor nodes to produce a final response. |

### LLM Basic

| Script | What it demonstrates |
| --- | --- |
| [01_basic_llm/main.py](<LLM Basic/01_basic_llm/main.py>) | Makes a minimal OpenRouter chat-completion request through the OpenAI Python client. |
| [01_basic_llm/models.py](<LLM Basic/01_basic_llm/models.py>) | Calls the OpenRouter models endpoint and prints model IDs that begin with `openai/`. |
| [02_messages/main.py](<LLM Basic/02_messages/main.py>) | Uses system and user roles to control a chat-completion response. |
| [03_system_user_prompt/main.py](<LLM Basic/03_system_user_prompt/main.py>) | Shows how a system prompt can adapt an explanation for a ten-year-old reader. |
| [04_temperature/main.py](<LLM Basic/04_temperature/main.py>) | Sets temperature for a creative poetry prompt. |
| [05_token_usage/main.py](<LLM Basic/05_token_usage/main.py>) | Prints a completion and its usage metadata. |
| [06_max_token/main.py](<LLM Basic/06_max_token/main.py>) | Limits a response with `max_tokens`. |
| [07_prompt_template/main.py](<LLM Basic/07_prompt_template/main.py>) | Builds a prompt with a Python f-string topic variable. |
| [08_structured_output/main.py](<LLM Basic/08_structured_output/main.py>) | Requests JSON containing sentiment and confidence fields. |
| [09_few_shot_prompting/main.py](<LLM Basic/09_few_shot_prompting/main.py>) | Uses labelled review examples to demonstrate few-shot classification. |
| [10_conversation_history/main.py](<LLM Basic/10_conversation_history/main.py>) | Includes prior user and assistant messages so the model can answer from conversation context. |
| [11_context_window/main.py](<LLM Basic/11_context_window/main.py>) | Shows that earlier messages inside the request remain available as context. |
| [12_streaming/main.py](<LLM Basic/12_streaming/main.py>) | Streams completion chunks and prints tokens as they arrive. |
| [13_prompt_injection/main.py](<LLM Basic/13_prompt_injection/main.py>) | Tests a customer-support system instruction against a user prompt that tries to override it. |

### MCP

The server scripts use standard input/output transport. Run the matching server from the `MCP` directory; its client script starts and communicates with it.

| Script | What it demonstrates |
| --- | --- |
| [57_mcp_fundamentals_server.py](<MCP/57_mcp_fundamentals_server.py>) | Exposes a `get_customer_status` tool over a minimal MCP server. |
| [57_mcp_fundamentals_client.py](<MCP/57_mcp_fundamentals_client.py>) | Starts the fundamentals server, lists its tools, and calls `get_customer_status`. |
| [58_mcp_architecture_server.py](<MCP/58_mcp_architecture_server.py>) | Provides a customer lookup tool for the architecture example. |
| [58_mcp_architecture_client.py](<MCP/58_mcp_architecture_client.py>) | Connects to the architecture server and invokes its customer lookup tool. |
| [60_mcp_transport_server.py](<MCP/60_mcp_transport_server.py>) | Defines a `hello` tool and runs it through MCP stdio transport. |
| [60_mcp_transport_client.py](<MCP/60_mcp_transport_client.py>) | Connects over stdio transport and calls the `hello` tool. |
| [61_mcp_tools_server.py](<MCP/61_mcp_tools_server.py>) | Registers arithmetic tools for addition and multiplication. |
| [61_mcp_tools_client.py](<MCP/61_mcp_tools_client.py>) | Discovers and invokes the math tools exposed by the matching server. |
| [62_mcp_resources_server.py](<MCP/62_mcp_resources_server.py>) | Publishes a customer-support policy as an MCP resource. |
| [63_mcp_prompts_server.py](<MCP/63_mcp_prompts_server.py>) | Publishes a parameterized customer-support prompt. |
| [66_68_mcp_server.py](<MCP/66_68_mcp_server.py>) | Implements a customer server with read and approved-update tools, a policy resource, validation, and audit logging. |
| [66_68_mcp_client.py](<MCP/66_68_mcp_client.py>) | Exercises the secure customer server's discovery, read, and status-update capabilities. |
| [server.py](<MCP/server.py>) | Combines customer tools, customer and policy resources, and an analysis prompt in one MCP server. |
| [client_discovery.py](<MCP/client_discovery.py>) | Connects to the combined server and lists its available MCP capabilities. |
| [client_tool.py](<MCP/client_tool.py>) | Calls tools on the combined customer-support server. |

### Production AI Engineering

| Script | What it demonstrates |
| --- | --- |
| [50_evaluation.py](<Production AI Engineering/50_evaluation.py>) | Generates answers for a small context-grounded dataset, uses an LLM judge, and reports aggregate quality metrics. |
| [51_observability.py](<Production AI Engineering/51_observability.py>) | Records a model call's response, latency, usage metadata, and errors. |
| [52_guardrail.py](<Production AI Engineering/52_guardrail.py>) | Applies basic input, action-approval, and output keyword guardrails around an LLM call. |
| [53_security.py](<Production AI Engineering/53_security.py>) | Demonstrates environment-based secret loading, token authentication, role authorization, input validation, and logging. |
| [54_cost_optimization.py](<Production AI Engineering/54_cost_optimization.py>) | Reduces cost through response caching, model routing, short prompts, and a token limit. |
| [55_latency_optimization.py](<Production AI Engineering/55_latency_optimization.py>) | Reduces perceived latency with concurrent async calls and streaming output. |
| [56_deployment.py](<Production AI Engineering/56_deployment.py>) | Exposes a FastAPI service with `/health` and `/ask` endpoints backed by a chat model. |

### RAG

| Script | What it demonstrates |
| --- | --- |
| [21_embeddings.py](<RAG/21_embeddings.py>) | Generates an embedding vector for a single sentence with a Hugging Face embedding model. |
| [22_semantic_similarity.py](<RAG/22_semantic_similarity.py>) | Computes cosine similarity between a query embedding and document embeddings. |
| [24_semantic_search.py](<RAG/24_semantic_search.py>) | Stores short documents in Chroma and retrieves the most similar documents. |
| [25_document_chunking.py](<RAG/25_document_chunking.py>) | Loads a PDF and splits its pages into overlapping character chunks. |
| [28_vector_store.py](<RAG/28_vector_store.py>) | Creates a Chroma vector store from sample TV manual text and performs a similarity search. |
| [29_retrievers.py](<RAG/29_retrievers.py>) | Converts a Chroma store into an MMR retriever and queries it. |
| [30_basic_rag.py](<RAG/30_basic_rag.py>) | Builds a complete retrieve → context → prompt → generate RAG pipeline for TV-support questions. |
| [31_rag_evaluation.py](<RAG/31_rag_evaluation.py>) | Evaluates RAG retrieval hits and a simple word-overlap answer score across a small dataset. |
| [32_agentic_rag.py](<RAG/32_agentic_rag.py>) | Uses a LangGraph decision node to choose whether a question needs retrieval before answering. |

### Tools

| Script | What it demonstrates |
| --- | --- |
| [33_tools.py](<Tools/33_tools.py>) | Defines LangChain tools for addition and customer-status lookup. |
| [34_tool_calling.py](<Tools/34_tool_calling.py>) | Binds an arithmetic tool to a model and prints the model's requested tool call. |
| [35_multiple_tools.py](<Tools/35_multiple_tools.py>) | Binds arithmetic and customer-status tools to a model and examines tool calls for several questions. |
| [36_tool_selection.py](<Tools/36_tool_selection.py>) | Shows model selection among multiple available tools based on the user's request. |

## Folder dependencies

Each major folder includes its own `requirements.txt`, so install dependencies from the folder that contains the script you want to run. Some scripts also require local assets, such as the PDF referenced by `RAG/25_document_chunking.py`. The FastAPI example is an application module; run it with an ASGI server such as `uvicorn 56_deployment:app --reload` from the `Production AI Engineering` directory.
