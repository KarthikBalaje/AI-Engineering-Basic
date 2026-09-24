# OpenAI Models on OpenRouter — Classification & Selection Guide

## 1. Classification Overview

| Category | Cost Tier | Typical Performance | Primary Purpose | Recommended Starting Model |
|---|---|---|---|---|
| **SLM / Small-model tier** | 🟢 Cheap | ⭐⭐⭐–⭐⭐⭐⭐ | Classification, extraction, routing, simple generation | `openai/gpt-5.4-nano` |
| **Optimal LLM** | 🟡 Low–Medium | ⭐⭐⭐⭐–⭐⭐⭐⭐⭐ | General-purpose AI applications, RAG, agents | `openai/gpt-5.4-mini` |
| **High-performance LLM** | 🔴 High | ⭐⭐⭐⭐⭐ | Complex reasoning, advanced coding, complex agents | `openai/gpt-5.4` |
| **Reasoning LLM** | 🔴 High–Very High | ⭐⭐⭐⭐⭐ | Deep reasoning, planning, difficult problems | `openai/o3`, `openai/o3-pro` |
| **Embedding — Optimal** | 🟢 Very Cheap | ⭐⭐⭐⭐ | RAG, semantic search, vector databases | `openai/text-embedding-3-small` |
| **Embedding — High Quality** | 🟡 Medium | ⭐⭐⭐⭐⭐ | Higher-quality retrieval/search | `openai/text-embedding-3-large` |

> **Note:** SLM is a conceptual category. Models named `nano` or `mini` are smaller/cheaper model tiers, but the names alone do not establish a strict technical definition of an SLM.

---

# 2. SLM / Small-model Tier

| Model | Cost Tier | Performance | Best For | Recommendation |
|---|---|---|---|---|
| `openai/gpt-5.4-nano` | 🟢 Very Cheap | ⭐⭐⭐ | Classification, extraction, routing, ranking, high-volume workloads | 🏆 **Best cheap choice** |
| `openai/gpt-5-nano` | 🟢 Very Cheap | ⭐⭐⭐ | Simple generation and high-volume tasks | Good |
| `openai/gpt-4.1-nano` | 🟢 Very Cheap | ⭐⭐⭐ | Lightweight applications | Good for legacy/compatibility |
| `openai/gpt-5.4-mini` | 🟡 Low | ⭐⭐⭐⭐ | General-purpose applications | 🏆 **Best overall small model** |
| `openai/gpt-5-mini` | 🟡 Low | ⭐⭐⭐⭐ | General-purpose generation | Good |
| `openai/gpt-4.1-mini` | 🟡 Low | ⭐⭐⭐⭐ | General applications and coding | Good |

### Typical use cases

| Use Case | Suggested Model |
|---|---|
| Classification | `gpt-5.4-nano` |
| Entity/information extraction | `gpt-5.4-nano` |
| Query routing | `gpt-5.4-nano` |
| Query rewriting | `gpt-5.4-nano` |
| Metadata generation | `gpt-5.4-nano` |
| High-volume processing | `gpt-5.4-nano` |
| General application | `gpt-5.4-mini` |
| Moderate reasoning | `gpt-5.4-mini` |

---

# 3. Optimal LLM — Price/Performance

## ⭐ Recommended: `openai/gpt-5.4-mini`

| Attribute | Recommendation |
|---|---|
| Model | `openai/gpt-5.4-mini` |
| Cost | 🟡 Low–Medium |
| Performance | ⭐⭐⭐⭐½ |
| Speed | ⚡ Fast |
| Reasoning | Strong |
| Coding | Strong |
| Tool Calling | Strong |
| RAG | ⭐⭐⭐⭐⭐ |
| Agents | ⭐⭐⭐⭐⭐ |
| Portfolio Projects | ⭐⭐⭐⭐⭐ |
| Overall | 🏆 **Best price/performance starting point** |

### Recommended use

| Application | Suitability |
|---|---|
| Basic LLM application | ⭐⭐⭐⭐⭐ |
| RAG | ⭐⭐⭐⭐⭐ |
| LangChain | ⭐⭐⭐⭐⭐ |
| LangGraph | ⭐⭐⭐⭐⭐ |
| Tool calling | ⭐⭐⭐⭐⭐ |
| Structured output | ⭐⭐⭐⭐⭐ |
| Agents | ⭐⭐⭐⭐⭐ |
| Simple coding tasks | ⭐⭐⭐⭐ |
| Complex reasoning | ⭐⭐⭐⭐ |

### Other candidates

| Model | Cost | Performance | Use |
|---|---|---|---|
| `openai/gpt-5-mini` | 🟡 Low | ⭐⭐⭐⭐ | General-purpose |
| `openai/gpt-4.1-mini` | 🟡 Low | ⭐⭐⭐⭐ | General/coding |
| `openai/o4-mini` | 🟡–🔴 | ⭐⭐⭐⭐½ | Reasoning-heavy tasks |

---

# 4. High-Performance LLM

| Model | Cost Tier | Performance | Best Use |
|---|---|---|---|
| `openai/gpt-5.4` | 🔴 High | ⭐⭐⭐⭐⭐ | Complex reasoning, advanced RAG, agents, coding |
| `openai/gpt-5.5` | 🔴 High | ⭐⭐⭐⭐⭐ | Frontier general-purpose workloads |
| `openai/gpt-5.5-pro` | 🔴 Very High | ⭐⭐⭐⭐⭐ | Maximum-quality workloads |
| `openai/gpt-5-pro` | 🔴 Very High | ⭐⭐⭐⭐⭐ | High-quality complex tasks |
| `openai/gpt-5.2` | 🔴 High | ⭐⭐⭐⭐⭐ | High-end general purpose |
| `openai/gpt-4.1` | 🟡–🔴 | ⭐⭐⭐⭐ | Strong general-purpose / coding |
| `openai/gpt-4o` | 🟡 | ⭐⭐⭐⭐ | General/multimodal applications |

### When to use

| Requirement | Model Tier |
|---|---|
| Cheapest possible processing | Nano |
| Best price/performance | Mini |
| Complex application | Full |
| Maximum quality | Pro |
| Deep reasoning | Reasoning models |

---

# 5. Reasoning Models

| Model | Cost Tier | Reasoning | Best For |
|---|---|---|---|
| `openai/o3` | 🔴 High | ⭐⭐⭐⭐⭐ | Complex reasoning |
| `openai/o3-pro` | 🔴 Very High | ⭐⭐⭐⭐⭐+ | Maximum reasoning |
| `openai/o4-mini` | 🟡–🔴 | ⭐⭐⭐⭐½ | Cost-conscious reasoning |
| `openai/o4-mini-high` | 🟡–🔴 | ⭐⭐⭐⭐½ | Higher reasoning effort |
| `openai/o1` | 🔴 High | ⭐⭐⭐⭐⭐ | Reasoning / legacy |
| `openai/o1-pro` | 🔴 Very High | ⭐⭐⭐⭐⭐ | High-end reasoning |

> Do not use reasoning models for every task. For simple classification, extraction, or routing, a Nano model can be much more economical.

---

# 6. Embedding Models

## Embeddings are NOT LLMs

Embedding models convert text into vectors.

| Model | Cost Tier | Retrieval Quality | Recommended Use |
|---|---|---|---|
| `openai/text-embedding-3-small` | 🟢 Very Cheap | ⭐⭐⭐⭐ | 🏆 Most RAG projects |
| `openai/text-embedding-3-large` | 🟡 Medium | ⭐⭐⭐⭐⭐ | High-quality retrieval |
| `openai/text-embedding-ada-002` | 🟡/🔴 Legacy | ⭐⭐ | Compatibility only |

### Recommendation

For most portfolio and learning projects:

```text
openai/text-embedding-3-small
```

Use `text-embedding-3-large` when retrieval quality is important enough to justify the additional cost.

---

# 7. RAG Model Selection

| RAG Component | Cheap | Optimal | High Quality |
|---|---|---|---|
| Query classification | `gpt-5.4-nano` | `gpt-5.4-mini` | `gpt-5.4` |
| Query rewriting | `gpt-5.4-nano` | `gpt-5.4-mini` | `gpt-5.4` |
| Embedding | `text-embedding-3-small` | **`text-embedding-3-small`** | `text-embedding-3-large` |
| Answer generation | `gpt-5.4-nano` | **`gpt-5.4-mini`** | `gpt-5.4` |
| Complex reasoning | `gpt-5.4-mini` | `gpt-5.4` | `o3-pro` |

---

# 8. Recommended Portfolio Stack

| Layer | Recommended Model | Why |
|---|---|---|
| Cheap auxiliary LLM | `openai/gpt-5.4-nano` | Low cost and fast |
| Main LLM | **`openai/gpt-5.4-mini`** | Best price/performance |
| High-end LLM | `openai/gpt-5.4` | Strong complex-task performance |
| Reasoning | `openai/o3` | Deep reasoning |
| Embedding | **`openai/text-embedding-3-small`** | Very low cost and strong retrieval |
| High-quality embedding | `openai/text-embedding-3-large` | Better retrieval quality |

---

# 9. Cost vs Performance Matrix

| Tier | Cost | Speed | Performance | Best Application |
|---|---:|---:|---:|---|
| 🟢 Nano | $$$$$ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | High-volume/simple tasks |
| 🟡 Mini | $$$ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐½ | **Most applications** |
| 🔴 Full | $$ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Complex applications |
| 🔴 Pro | $ | ⭐⭐ | ⭐⭐⭐⭐⭐+ | Maximum quality |
| 🧠 Reasoning | $–$$ | ⭐⭐–⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Difficult reasoning |
| 📚 Embedding Small | $$$$$ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | **Most RAG systems** |
| 📚 Embedding Large | $$$ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | High-quality retrieval |

> The number of `$` symbols above represents relative cost tiers, not exact OpenRouter pricing.

---

# 10. Final Decision Table

| If You Need... | Choose |
|---|---|
| 💰 Lowest-cost LLM | **`openai/gpt-5.4-nano`** |
| ⚡ Fast high-volume processing | **`openai/gpt-5.4-nano`** |
| 🏆 Best price/performance | **`openai/gpt-5.4-mini`** |
| 🤖 General-purpose AI application | **`openai/gpt-5.4-mini`** |
| 📚 RAG generation | **`openai/gpt-5.4-mini`** |
| 🔧 LangChain application | **`openai/gpt-5.4-mini`** |
| 🔄 LangGraph/Agent application | **`openai/gpt-5.4-mini`** |
| 🧠 Complex reasoning | `openai/o3` / `openai/o3-pro` |
| 🚀 Maximum general performance | `openai/gpt-5.4` / higher-end models |
| 🔎 RAG embeddings | **`openai/text-embedding-3-small`** |
| 🎯 Maximum embedding quality | `openai/text-embedding-3-large` |

---

# 11. Recommended Learning Path

Instead of learning every model in the OpenRouter catalog, start with four:

| # | Model | Learn This For |
|---|---|---|
| 1 | `openai/gpt-5.4-nano` | Cheap model / classification / extraction |
| 2 | **`openai/gpt-5.4-mini`** | ⭐ Main LLM / LangChain / RAG / agents |
| 3 | `openai/gpt-5.4` | High-performance LLM |
| 4 | **`openai/text-embedding-3-small`** | ⭐ Embeddings / RAG / vector search |

Then compare the same project across:

```text
gpt-5.4-nano
       ↓
gpt-5.4-mini
       ↓
gpt-5.4
```

Measure:

| Metric | What to Compare |
|---|---|
| Quality | Accuracy / helpfulness |
| Cost | Input + output token cost |
| Latency | Response time |
| Context | Maximum context requirements |
| Hallucination | Incorrect/fabricated information |
| Tool calling | Reliability |
| Retrieval | RAG relevance |

This gives you practical model-selection experience that is more valuable than memorizing model names.

---

# 12. Important: `:batch` Models

OpenRouter may return:

```text
openai/gpt-5.4
openai/gpt-5.4:batch
```

Treat these as the same base model for a simple model catalog.

Normalize them with:

```python
model_id = model["id"].replace(":batch", "")
```

Then deduplicate the resulting model IDs.

---

# 13. Quick Cheat Sheet

| Category | 🏆 First Choice |
|---|---|
| Cheap / Small | `openai/gpt-5.4-nano` |
| Optimal LLM | **`openai/gpt-5.4-mini`** |
| High-performance LLM | `openai/gpt-5.4` |
| Reasoning | `openai/o3` |
| Optimal Embedding | **`openai/text-embedding-3-small`** |
| High-quality Embedding | `openai/text-embedding-3-large` |

---

## Note on current pricing and availability

OpenRouter's model catalog, pricing, aliases, and availability can change. Use the current OpenRouter Models API metadata when making production cost decisions.

The classifications in this document are intended as a **practical selection guide**, not a permanent ranking of all OpenAI models.
