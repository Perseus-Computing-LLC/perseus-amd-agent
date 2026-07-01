# AMD Act II — Winning Strategy

**Hackathon:** AMD Developer Hackathon: Act II
**Theme:** AI Agents
**Dates:** July 6-11, 2026
**Prize Pool:** $10,000 (1st: $5K, 2nd: $3K, 3rd: $2K)
**Judging:** Application of Technology, Presentation, Business Value, Originality

---

## Act I Autopsy: What Won

481 submissions. Winners had three things we didn't:

1. **Hardware benchmarks with tables** — REPOMIND published VRAM usage, throughput at every context length, needle-in-haystack at 200K tokens, and a real AMD AITER bug report
2. **Cost economics** — REPOMIND: "$4.12 of compute vs $40/seat/month. One MI300X = 70-140 developer seats. Breaks even in 3-6 months."
3. **Domain depth** — CatalystMD used real PDB protein structures, AutoDock Vina physics-based docking, not mock data

**Lesson:** Judges reward verifiable numbers over architectural descriptions. Every claim needs a table.

---

## Our Entry: Perseus + Mneme on AMD MI300X

### The Pitch

> "AI coding agents lose context every session. Perseus resolves workspace state before the agent sees it. Mneme carries memory across sessions. Both run on AMD MI300X — $0.03/session vs $40/month for SaaS. Demonstrated with benchmarks."

### Why This Wins

| Judging Criterion | How We Score |
|-------------------|-------------|
| **Application of Technology (25%)** | Real AMD MI300X utilization: vLLM ROCm 7 for inference, benchmarked context resolution latency, VRAM footprint measured |
| **Presentation (25%)** | 3-session progression demo with live context rendering + memory recall. Before/after comparison with token counts |
| **Business Value (25%)** | Cost economics table: solo dev to 100-dev team. Break-even analysis. Open-source (MIT) — no vendor lock-in |
| **Originality (25%)** | Combining pre-session context resolution with cross-session memory is novel. Nobody else does both. |

### The Demo: 3-Session Progression

**Session 1 (Cold Start):**
- Agent starts with zero context
- Perseus resolves: Python 3.12, FastAPI, PostgreSQL, black formatting, pytest convention
- 8 facts stored in Mneme
- Token count: 1,200 for context discovery

**Session 2 (Warm Start):**
- Perseus renders cached context (15ms vs 120ms)
- Agent recalls Session 1 facts via Mneme
- 5 facts recalled, 3 new insights generated
- Token count: 80 for context (94% reduction)

**Session 3 (Compounding):**
- 12 facts compounded into project summary
- Architecture pattern detected, convention drift flagged
- Agent knows the codebase better than a new hire
- Token count: 60 for context

### Required Evidence

| Evidence | Format | Status |
|----------|--------|--------|
| MI300X benchmarks | Table of latency, VRAM, throughput | To build |
| Cost economics | Solo/team/enterprise comparison table | In README |
| Demo video | 3-minute screen recording | To record |
| Architecture diagram | SVG + PNG thumbnail | To build |
| GitHub repo | Public, MIT, with working code | Created |
| Presentation | Lablab submission PDF | To create |

---

## Competitive Analysis

### Direct Competitors in Act I

| Project | What They Did | Why They Won |
|---------|--------------|--------------|
| REPOMIND | Repo-scale coding agent on MI300X | Hardware benchmarks, cost economics, found AITER bug |
| CatalystMD | 5-agent drug discovery pipeline | Real domain expertise, physics-based docking |
| Boardroom | Multi-agent debate summarization | Novel architecture, agent-on-agent interaction |

### Our Differentiators

1. **Combined context + memory** — nobody else does both pre-session resolution AND cross-session persistence
2. **Zero cloud dependency** — runs entirely on-premises (regulated industries can use it)
3. **MIT licensed** — no vendor lock-in, no $40/seat/month
4. **23+22 MCP tools** — the most comprehensive agent tool suite

---

## Execution Plan

## Current Status (June 21, 2026 — 20 days to deadline)

- [x] Repo created: `Perseus-Computing-LLC/perseus-amd-agent`
- [x] Architecture diagram with published-spec labeling
- [x] Benchmark suite with honest data-source labeling
- [x] Demo terminal simulation (Playwright-compatible)
- [x] SUBMISSION.md (LabLab.ai format)
- [x] Demo script (5-scene, 3-minute)
- [x] Cost economics tables (math-based, no GPU required)
- [ ] Demo video recording (in progress)
- [ ] Architecture thumbnail re-rendered with published-spec label
- [ ] Push all changes to GitHub
- [x] Register for AMD Developer Program ($100 credits + $50 Fireworks AI)
- [ ] Join lablab Act II team
- [ ] Upload demo video to YouTube
- [ ] Submit on LabLab.ai (July 6-11 window)

### AMD Cloud Credits Status

AMD Developer Cloud credits have not arrived (11 days since request). Fireworks AI API credits ($50) may have arrived separately — these are sufficient for Track 3 (Unicorn Track) which requires "one or both of AMD Compute pods and Fireworks AI API credits."

**Strategy:** Build everything without credits. All benchmarks are labeled with data source (`published-spec`, `measured`, `mathematical projection`). When credits arrive, swap in real measurements — the architecture and code don't change.

---

## Risks and Mitigations

| Risk | Impact | Mitigation | Status |
|------|--------|-----------|--------|
| AMD cloud credits don't arrive | Can't run MI300X benchmarks | **Done.** All benchmarks labeled with data source. Published-spec estimates in place. | ✅ MITIGATED |
| Fireworks AI credits also delayed | Can't show Fireworks AI integration | Plan B: Show architecture with Fireworks AI integration described; code is ready | ⚠️ WATCH |
| LabLab submission format unknown | Wrong format = rejected | LabLab has simpler form than Devpost. Submission text pre-written in SUBMISSION.md. | ✅ READY |
| Video over 3 minutes | Disqualified | Script designed for 2:35. Record at 165s with 10s buffer. | ✅ MITIGATED |
| Time (20 days out) | Rush job | **All code assets built.** Only video recording + registration remain. | ✅ AHEAD |

---

## Key URLs

- **Repo:** https://github.com/Perseus-Computing-LLC/perseus-amd-agent
- **Hackathon:** https://lablab.ai/ai-hackathons/amd-developer-hackathon-act-ii
- **AMD Developer Program:** https://www.amd.com/en/developer/ai-dev-program.html
- **Perseus:** https://github.com/tcconnally/perseus
- **Mneme:** https://github.com/Perseus-Computing-LLC/mneme
