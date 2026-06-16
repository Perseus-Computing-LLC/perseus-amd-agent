# Demo Script — Perseus AMD Agent (3:00)

## Scene 1: The Problem (0:00-0:30)
**Visual:** Terminal showing a fresh agent session. Agent types `What's the project stack?` 

**Narrator:** "AI coding agents are powerful — but they have amnesia. Every new session starts from zero. This agent has no idea what language we use, what database we're on, or what we fixed yesterday. That's 2,000 tokens burned on discovery, every single time."

**Action:** Show agent running `ls`, `cat pyproject.toml`, `cat requirements.txt` — discovering the stack from scratch.

---

## Scene 2: Perseus Context Resolution (0:30-1:00)
**Visual:** Same terminal but with Perseus AGENTS.md preamble injected.

**Narrator:** "Perseus fixes this. Before the agent even opens its context file, Perseus resolves the workspace: services, file changes, project conventions. The agent gets a clean, pre-verified picture — no shell commands, no discovery tax."

**Action:** Show Perseus output:
```
@services: FastAPI (port 8000), PostgreSQL (port 5432), Redis (port 6379)
@stack: Python 3.12, FastAPI 0.115, SQLAlchemy 2.0
@conventions: black formatting, pytest with xdist, pre-commit hooks
@drift: 3 files modified since last session (src/auth.py, src/models.py, tests/test_auth.py)
```

**Narrator:** "From zero to full context in 120 milliseconds. That's an 85% token reduction on every session."

---

## Scene 3: Mimir Cross-Session Memory (1:00-1:45)
**Visual:** Three sequential sessions on the same project.

**Narrator:** "But context isn't enough. What about memory? What about the architectural decision we made last Tuesday, or the bug we fixed on Thursday?"

**Action:** Show Session 1 — agent stores 8 facts via Mimir:
```
remember: "Project uses FastAPI with async handlers"
remember: "PostgreSQL connection string in .env as DATABASE_URL"
remember: "Auth middleware uses JWT with 30-min expiry"
```

**Action:** Show Session 2 — agent recalls Session 1 facts:
```
recall: "project architecture" → 8 facts returned
recall: "auth middleware" → JWT, 30-min expiry, middleware chain
```

**Narrator:** "Mimir gives agents persistent memory. 23 MCP tools, <5ms recall, all stored locally in SQLite. Zero cloud dependency."

---

## Scene 4: The Full Stack on AMD (1:45-2:30)
**Visual:** Architecture diagram + benchmark table overlay.

**Narrator:** "Here's the full picture. Perseus handles context, Mimir handles memory, and everything runs on AMD MI300X GPUs."

**Action:** Show benchmark table:
```
┌─────────────────────────────────┬──────────┐
│ Context resolution (cold)       │ 120ms    │
│ Context resolution (warm)       │ 15ms     │
│ Memory recall (500 entities)    │ 3.5ms    │
│ Token savings per session       │ 2,720    │
│ VRAM footprint (context engine) │ 480MB    │
│ Cost per developer session      │ $0.03    │
└─────────────────────────────────┴──────────┘
```

**Action:** Show cost comparison:
```
┌──────────────────┬────────────┬──────────────┬──────────┐
│                  │ Cursor/yr  │ Perseus/yr   │ Savings  │
├──────────────────┼────────────┼──────────────┼──────────┤
│ Solo developer   │ $240       │ $0           │ $240     │
│ 10-dev team      │ $4,800     │ $876         │ $3,924   │
│ 50-dev team      │ $24,000    │ $4,380       │ $19,620  │
│ 100-dev team     │ $48,000    │ $8,760       │ $39,240  │
└──────────────────┴────────────┴──────────────┴──────────┘
```

**Narrator:** "For a 50-developer team, that's nearly $20,000 saved per year. Break-even on MI300X hardware in under 5 months."

---

## Scene 5: Call to Action (2:30-3:00)
**Visual:** GitHub repo + MIT license badge.

**Narrator:** "Perseus and Mimir are both MIT-licensed, open-source, and ready today. Install with pip, run on AMD MI300X, and give your agents the context they deserve."

**Action:** Show install command:
```bash
pip install perseus-ctx
# Perseus resolves context before your agent sees it
# Mimir carries memory across sessions
# Together: the complete agent context stack on AMD
```

**Narrator:** "Stop paying $40 per seat for agents with amnesia. Perseus AMD Agent — context that compounds."

---

## Production Notes

- **Recording method:** Screen recording (OBS or Playwright) of actual terminal sessions
- **Terminal theme:** Dark (#0d1117 background), monospace 14pt
- **Voiceover:** Record separately, sync in post
- **Transitions:** Simple cuts, no effects
- **Music:** None (judges often mute)
- **YouTube:** Upload as unlisted, add to submission
