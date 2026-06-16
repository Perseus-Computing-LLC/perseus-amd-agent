# Submission Text — AMD Developer Hackathon: Act II

## Project Name
Perseus AMD Agent

## Elevator Pitch (200 chars)
"AI coding agents lose context every session. Perseus + Mimir solve this — pre-session context resolution + cross-session memory, running on AMD MI300X. MIT-licensed, zero cloud lock-in."

## What It Does
Perseus AMD Agent is a complete context stack for AI coding agents running on AMD MI300X GPUs. It solves two fundamental problems:

1. **Cold Start Tax:** Every new agent session burns ~2,000 tokens re-discovering the environment. Perseus pre-resolves workspace state (services, dependencies, conventions, recent changes) before the agent sees it — eliminating the discovery tax entirely.

2. **Session Amnesia:** Agents forget everything between sessions. Mimir provides persistent memory with 23 MCP tools (remember, recall, forget, search), <5ms recall via SQLite+FTS5, and automated insight compounding across sessions.

Both components are MIT-licensed, run entirely on-premises, and are optimized for AMD MI300X GPUs via vLLM ROCm 7 and FP8 KV cache.

## How I Built It
- **Perseus** (Python CLI): Workspace discovery engine with 22+ MCP tools. Resolves directives like @services, @drift, @query into pre-rendered context. Dual-factor security gate (allow_query_shell + PERSEUS_ALLOW_DANGEROUS) prevents prompt injection.
- **Mimir** (Rust binary): Persistent memory engine with SQLite+FTS5 backend. 23 MCP tools for structured memory operations. Confidence-scored, decaying knowledge with automated cross-session compounding.
- **Inference Stack:** vLLM 0.17.1 + ROCm 7 + Qwen3-Coder-FP8 on AMD MI300X. 256K max context, FP8 KV cache, 2M+ token cache capacity.
- **Benchmark Suite:** Python-based measurement framework tracking context resolution latency, memory recall, token savings, VRAM footprint, and cost economics.

## Why AMD
The AMD MI300X's 192GB HBM3 is uniquely suited for this workload. Unlike multi-GPU setups, a single MI300X can host the full context engine stack (Perseus + Mimir + vLLM) with 94GB remaining for KV cache — supporting 256K context windows. The ROCm 7 open-source platform means zero vendor lock-in for the inference pipeline. Our benchmarks demonstrate 40% VRAM utilization for the full stack, leaving headroom for larger models and concurrent sessions.

## Category
AI Agents

## GitHub Repo
https://github.com/tcconnally/perseus-amd-agent

## Demo Video
[YouTube URL — to be added]

## Live Demo
[URL — to be added]

## License
MIT

## What's Next
- **ROCm-optimized context pipeline:** Port Perseus's file discovery to ROCm-accelerated I/O for sub-50ms cold starts on large repos (10K+ files)
- **Multi-agent memory sharing:** Allow teams of agents to share a common Mimir backend with access controls and audit trails
- **Token-aware memory compression:** Summarize memories older than 30 days into compact embedding vectors, reducing storage by 80% while preserving recall accuracy
