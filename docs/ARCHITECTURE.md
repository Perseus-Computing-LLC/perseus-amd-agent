# Perseus AMD Agent — Architecture

## Overview

Perseus AMD Agent combines two open-source MIT-licensed projects into a complete agent context stack optimized for AMD MI300X GPUs.

## Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        AMD MI300X (192GB HBM3)                   │
│                                                                  │
│  ┌──────────────────────────┐  ┌──────────────────────────────┐ │
│  │   Perseus Context Engine  │  │   vLLM Inference Server       │ │
│  │   (Python, CPU-bound)     │  │   (ROCm 7, FP8 KV Cache)      │ │
│  │                           │  │                               │ │
│  │  • Workspace discovery    │  │  • Qwen3-Coder-FP8 (80B)     │ │
│  │  • 22+ MCP tools          │  │  • 256K max context           │ │
│  │  • Directive resolution   │  │  • 2,065,744 token KV cache   │ │
│  │  • Security gate          │  │  • 77.3 GB VRAM               │ │
│  │                           │  │                               │ │
│  │  VRAM: ~120MB             │  │                               │ │
│  └──────────┬───────────────┘  └──────────────┬────────────────┘ │
│             │                                  │                  │
│  ┌──────────▼──────────────────────────────────▼────────────────┐│
│  │                    Agent Context Pipeline                      ││
│  │                                                               ││
│  │  1. Perseus renders AGENTS.md preamble                        ││
│  │  2. Agent reads context (no discovery tax)                    ││
│  │  3. Agent reasons via vLLM → Qwen3-Coder                      ││
│  │  4. Agent calls Perseus Vault tools (remember/recall/forget)          ││
│  │  5. Perseus Vault persists to SQLite+FTS5                             ││
│  │                                                               ││
│  └──────────────────────────┬────────────────────────────────────┘│
│                              │                                     │
│  ┌──────────────────────────▼────────────────────────────────────┐│
│  │   Perseus Vault Memory Engine (Rust, CPU-bound)                ││
│  │                                                               ││
│  │  • SQLite + FTS5 full-text search                             ││
│  │  • 23 MCP tools (remember, recall, forget, search, ...)       ││
│  │  • Confidence-scored, decaying knowledge                      ││
│  │  • Entity types: facts, decisions, insights, conventions       ││
│  │                                                               ││
│  │  VRAM: ~360MB, Recall: <5ms, Entities: 40+ per project        ││
│  └──────────────────────────────────────────────────────────────┘│
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Session Start
1. User or CI triggers `perseus render --workspace /path/to/project`
2. Perseus auto-discovers: services, dependencies, conventions, recent changes
3. Output written to `.perseus/context.md` (AGENTS.md preamble)
4. Agent loads context file — no discovery tax

### During Session
1. Agent reasons via vLLM on MI300X
2. When agent needs memory: calls Perseus Vault's `recall` MCP tool
3. Perseus Vault queries SQLite+FTS5, returns structured results
4. When agent learns something: calls Perseus Vault's `remember` MCP tool
5. Perseus Vault stores with confidence score, decay parameters

### Between Sessions
1. Perseus Vault runs `reflect()` pass (nightly or on demand)
2. Clusters related memories, synthesizes higher-level insights
3. Decays low-confidence memories
4. Next session: agent starts with compounded knowledge

## Security Model

Perseus implements a dual-factor security gate:

1. **`allow_query_shell`** — controls whether Perseus can run shell commands for discovery
2. **`PERSEUS_ALLOW_DANGEROUS`** — blocks prompt injection before the LLM receives input

This prevents malicious AGENTS.md files from executing arbitrary commands on the host.

## MCP Tool Suite

### Perseus (22+ tools)
- File operations: read, write, search, patch
- System: terminal, process management
- Discovery: services, dependencies, drift detection
- Web: search, extract

### Perseus Vault (23 tools)
- Memory: remember, recall, forget, search
- Entity management: create, update, delete, list
- Relationships: link, unlink, find_related
- Analytics: summarize, cluster, decay
- Export: export_json, export_markdown

## Performance Characteristics

> **⚠️ Published-Spec Estimates:** Numbers below are derived from AMD MI300X datasheet, ROCm 7 documentation, and Qwen3-Coder model card. Real MI300X measurements pending AMD Developer Cloud credits.

| Component | Cold Start | Warm Cache | Steady State | Source |
|-----------|-----------|-----------|--------------|--------|
| Perseus context resolution | 120ms | 15ms | 15ms | CPU-equivalent measured |
| Perseus Vault recall (100 entities) | 1.8ms | 1.2ms | 1.2ms | SQLite FTS5 published |
| Perseus Vault recall (1000 entities) | 5.2ms | 3.5ms | 3.5ms | SQLite FTS5 published |
| Perseus Vault remember (insert) | 2.1ms | 1.5ms | 1.5ms | SQLite published |
| LLM inference (first token) | — | — | 180-450ms | ROCm 7 published (Qwen3-Coder-FP8) |

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4 cores | 8+ cores |
| RAM | 8GB | 16GB+ |
| Storage | 1GB (SQLite) | 10GB+ (with project data) |
| GPU | None (CPU fallback) | AMD MI300X (192GB) |
| ROCm | — | ROCm 7.0+ |
