# AGENTS.md — Project Context for AI Agents

- **Name:** Perseus AMD Agent — Complete Agent Context Stack on AMD GPUs
- **Purpose:** AMD Developer Hackathon: Act II submission (Unicorn Track)
- **Repo:** github.com/Perseus-Computing-LLC/perseus-amd-agent
- **Stack:** Python 3.12, Rust (Perseus Vault), vLLM ROCm 7, Qwen3-Coder-FP8
- **License:** MIT

## Architecture
- `src/benchmark.py` — Benchmark suite with honest data-source labeling (published-spec, measured, mathematical)
- `src/context_engine.py` — Perseus context resolution demo (3-session progression)
- `demo/demo_terminal.html` — Playwright terminal simulation for demo video
- `demo/record_video.py` — Record demo video via Playwright + FFmpeg
- `assets/architecture.html` — Dark-themed SVG architecture diagram

## Key Decisions
1. **Published-spec benchmarks** — AMD cloud credits haven't arrived. All benchmarks labeled with data source. No fabricated measurements.
2. **Unicorn Track** — No fixed benchmark. Judged on creativity, originality, product potential.
3. **Fireworks AI credits may suffice** — Track 3 requires "one or both of" AMD Compute pods and Fireworks AI API credits.
4. **Label everything honestly** — `published-spec`, `measured`, `mathematical projection` — judges reward verifiable data over claims.

## Conventions
- Benchmarks must include `data_source` and `methodology` fields
- All MI300X claims must reference published AMD documentation
- Demo terminal uses ASCII only (no Unicode — headless Chromium can't render emoji)
- Architecture diagram uses double-rect technique (opaque backdrop + semi-transparent fill)

## Hackathon
- **Platform:** LabLab.ai (NOT Devpost)
- **Deadline:** July 11, 2026, 15:00 UTC
- **Registration:** Open now; kickoff July 6
- **Registered builders:** 8,314+
- **Video:** Under 3 min, terminal simulation

## Git
- Push to Perseus-Computing-LLC/perseus-amd-agent (main branch)
- Git identity for external commits: perseus <51974392+tcconnally@users.noreply.github.com>
