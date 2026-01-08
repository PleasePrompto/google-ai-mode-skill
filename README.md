<div align="center">

# Google AI Mode Skill

### **Supercharge Claude Code's Web Research with Google AI Mode**

**For: Claude Code CLI users only**

Transform your LLM's online research capabilities by connecting Claude Code directly to Google's AI Mode—getting AI-synthesized answers from 100+ sources instead of scattered search results.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://www.anthropic.com/news/skills)
[![Based on](https://img.shields.io/badge/Based%20on-Google%20AI%20Mode%20MCP-green.svg)](https://github.com/PleasePrompto/google-ai-mode-mcp)

### Why This Matters

Most built-in web research is mediocre. This skill gives Claude Code **professional-grade research** by tapping into Google's AI Mode—the same technology that synthesizes information from dozens of websites into one cited answer.

**Example Use Cases:**
```
"Next.js 15 App Router best practices 2026 with server components examples"
→ AI-synthesized coding guide with inline citations [1][2][3]

"Compare PostgreSQL vs MySQL JSON performance 2026, include benchmarks"
→ Technical comparison table with real-world data

"Find the latest EU AI regulations 2026 and their impact on startups"
→ Legal overview with official government sources

"Best noise-cancelling headphones under €300, compare Sony vs Bose"
→ Product comparison with reviews and specs

"Intermittent fasting protocols 2026, include recent scientific studies"
→ Health guide with medical research citations
```

**Result:** Research on **ANY topic**—coding, tech comparisons, regulations, product reviews, health, finance, travel. Curated answers with sources. Saves tokens. Superior to generic web search.

[Installation](#installation) • [Quick Start](#quick-start) • [How It Works](#how-it-works) • [MCP Alternative](#mcp-server-alternative)

</div>

---

## 📋 Last Updates (2026-01-08)

**v2.0 - Multi-Language & Detection Overhaul**

✅ **4-Stage Completion Detection** - SVG thumbs-up → aria-label → text → 40s timeout
✅ **Multi-Language Support** - Works in DE/EN/NL/ES/FR/IT browser locales
✅ **87% Faster** - Average 4s detection (was 30s+)
✅ **AI Mode Availability Check** - Detects region restrictions with proxy suggestion
✅ **17 Citation Selectors** - Language-agnostic fallback chain
✅ **15 Cutoff Markers** - Cleaner content extraction across languages

<details>
<summary>📖 Show previous updates</summary>

**v1.5** - Persistent browser profile, CAPTCHA elimination
**v1.0** - Initial release with basic Google AI Mode integration

</details>

---

## ⚠️ Important: Local Claude Code Only

**This skill works ONLY with local [Claude Code](https://github.com/anthropics/claude-code) installations, NOT in the web UI.**

The web UI runs skills in a sandbox without network access, which this skill requires for browser automation. You must use Claude Code locally on your machine.

---

## What This Is

A Claude Code skill that connects your agent to **Google AI Mode**—Google's AI-powered search that synthesizes information from dozens of web sources into a single, cited answer.

Instead of Claude reading page after page, Google does the heavy lifting. Claude gets one clean, structured response with inline citations.

**The advantage:** Free, token-efficient research with grounded sources. No API keys needed.

---

## How It Works

```
Claude asks a question
         ↓
Skill launches stealth browser
         ↓
Google AI Mode searches & synthesizes dozens of sources
         ↓
Skill extracts AI answer + citations
         ↓
Converts to clean Markdown with [1][2][3] references
         ↓
Claude receives final answer
```

**The key difference:**

Traditional web research:
- Claude searches Google → gets 10 links
- Claude reads 5-10 full pages → thousands of tokens consumed
- Claude synthesizes manually → risks missing details or hallucinating
- You pay for all those tokens

With this skill:
- Google AI Mode searches + synthesizes → one request
- Claude receives one clean, cited answer → minimal tokens
- Google's sources are preserved → verifiable, grounded
- It's free (uses public Google Search)

---

## Why This Matters

Google AI Mode (the `udm=50` parameter) makes Google search work like a research assistant. It:
- Reads and analyzes dozens of websites automatically
- Synthesizes findings into structured answers
- Cites every claim with source links
- Handles follow-up context across queries

Claude gets the benefits without doing the work—or burning the tokens.

---

## Installation

### The simplest installation ever:

```bash
# 1. Create skills directory (if it doesn't exist)
mkdir -p ~/.claude/skills

# 2. Clone this repository
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/google-ai-mode-skill google-ai-mode

# 3. That's it! Open Claude Code and say:
"What are my skills?"
```

When you first use the skill, it automatically:
- Creates an isolated Python environment (`.venv`)
- Installs all dependencies including **Google Chrome**
- Sets up browser automation with persistent profile
- Everything stays contained in the skill folder

**Note:** The setup uses real Chrome (not Chromium) for cross-platform reliability, consistent browser fingerprinting, and better anti-detection with Google services.

---

## Quick Start

### 1. Check your skills

Say in Claude Code:
```
"What skills do I have?"
```

Claude will list your available skills including Google AI Mode.

### 2. Start researching

```
"Search Google AI Mode for: Next.js 15 App Router best practices"
```

```
"What are the new features in Astro 4.0?"
```

```
"Research React Server Components"
```

Claude will automatically use the skill to query Google AI Mode and return a clean, cited answer.

### 3. Get better results

Be specific with your queries:

**Instead of:** "React hooks"
**Try:** "React hooks best practices 2026 (useState, useEffect, custom hooks). Include code examples."

**Instead of:** "PostgreSQL features"
**Try:** "PostgreSQL 16 JSON features and performance improvements 2026"

---

## First Run: CAPTCHA Handling

On your first query, Google may show a CAPTCHA to verify you're human. This is normal when the browser profile is created.

**If Claude reports a CAPTCHA error:**
1. Tell Claude: "Run that search with visible browser"
2. The browser will open visibly
3. Solve the CAPTCHA manually
4. The skill continues automatically
5. Next queries will work smoothly without CAPTCHAs

After the first CAPTCHA, searches typically run smoothly. The skill uses a persistent browser profile to eliminate future CAPTCHAs.

---

## How the Skill Works

This is a **Claude Code Skill**—a local folder containing instructions and scripts that Claude Code can use when needed. Unlike the [MCP server version](https://github.com/PleasePrompto/google-ai-mode-mcp), this runs directly in Claude Code without needing a separate server.

### Key Differences from MCP Server

| Feature | This Skill | MCP Server |
|---------|------------|------------|
| **Protocol** | Claude Skills | Model Context Protocol |
| **Installation** | Clone to `~/.claude/skills` | `claude mcp add ...` |
| **Compatibility** | Claude Code only (local) | Claude Code, Codex, Cursor, Cline, etc. |
| **Language** | Python | TypeScript |
| **Browser Profile** | Persistent (eliminates CAPTCHAs) | Per-request context |
| **Distribution** | Git clone | npm package |

### Architecture

```
~/.claude/skills/google-ai-mode/
├── SKILL.md              # Instructions for Claude
├── scripts/              # Python automation scripts
│   ├── run.py            # Universal venv wrapper
│   ├── search.py         # Main search implementation
│   ├── browser_utils.py  # Browser automation
│   └── config.py         # Configuration
├── .venv/                # Isolated Python environment (auto-created)
└── results/              # Saved search results (optional)
```

When Claude needs web research:
1. Loads the skill instructions from SKILL.md
2. Runs the Python search script via run.py wrapper
3. Opens browser with persistent profile (Chrome)
4. Extracts AI answer + citations from Google
5. Returns clean Markdown to Claude
6. Claude uses that knowledge to help with your task

---

## Core Features

**Source-Grounded Responses:**
Google AI Mode synthesizes information from dozens of sources with inline citations. Every claim is backed by a source link.

**Direct Integration:**
No copy-paste between browser and editor. Claude queries and receives answers programmatically.

**Persistent Browser Profile:**
After solving the first CAPTCHA (if any), the browser profile is saved. Future searches run smoothly without interruption.

**Zero Configuration:**
Works out of the box. No API keys, no external services, no configuration files needed.

**Self-Contained:**
Everything runs in the skill folder with an isolated Python environment. No global installations.

**Token Efficient:**
One query returns one synthesized answer instead of Claude reading 5-10 full pages.

---

## Troubleshooting

**Skill not found:**
```bash
# Make sure it's in the right location
ls ~/.claude/skills/google-ai-mode/
# Should show: SKILL.md, scripts/, requirements.txt, etc.
```

**Repeated CAPTCHAs:**

If Google keeps showing CAPTCHAs:
- Tell Claude: "Use visible browser for this search"
- Add 10-30 second delays between searches
- Make sure the persistent profile isn't corrupted

**Browser won't launch:**

Clear the browser profile:
```bash
# Linux/macOS
rm -rf ~/.cache/google-ai-mode-skill/chrome_profile

# Windows
rmdir /s "%LOCALAPPDATA%\google-ai-mode-skill\chrome_profile"
```

**Dependencies issues:**
```bash
# Manual reinstall if needed
cd ~/.claude/skills/google-ai-mode
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m patchright install chrome
```

**Wrong language results:**

The skill forces English results. If you still get wrong languages, clear the browser profile (see above).

---

## Tips for Better Results

**Be specific with your queries:**

Instead of: "React hooks"
Try: "React hooks best practices 2026 (useState, useEffect, custom hooks, common pitfalls)"

**Include version numbers:**

Instead of: "Next.js features"
Try: "Next.js 15 new features and breaking changes"

**Request structured output:**

"Compare PostgreSQL vs MySQL 2026 with a performance comparison table"

**Ask for examples:**

"Show me TypeScript discriminated union examples with type narrowing"

**Use the query template:**

```
[Technology/Topic] [Version] [Year] ([Aspect 1], [Aspect 2], [Aspect 3]). [Format request].
```

---

## Example Use Case

You need to implement OAuth2 in a framework you've never used before.

**Traditional approach:**
- Claude searches Google, gets 10 links
- Reads multiple documentation pages and blog posts
- Consumes thousands of tokens
- May miss important details or synthesize incorrectly

**With this skill:**
```
"Search Google AI Mode for: Hono OAuth2 implementation guide"
```

- Google reads and synthesizes sources automatically
- Claude gets one structured answer with code examples and citations
- Minimal token usage
- Sources are linked for verification

Claude can then use this grounded information to write the actual implementation.

---

## Technical Details

**Core Technology:**
- **Patchright**: Browser automation library (Playwright-based)
- **Python 3.8+**: Implementation language
- **Real Chrome**: Uses Google Chrome (not Chromium) for better reliability
- **Persistent Context**: Saves browser profile to eliminate CAPTCHAs

**Dependencies:**
- `patchright==1.57.2` - Browser automation
- `beautifulsoup4==4.14.3` - HTML parsing
- `html-to-markdown==2.19.6` - HTML conversion

**Data Storage:**

All data is stored locally within the skill directory:

```
~/.cache/google-ai-mode-skill/
└── chrome_profile/       - Persistent browser profile (cookies, session)
```

---

## Limitations

**Skill-Specific:**
- **Local Claude Code only** - Does not work in web UI (sandbox restrictions)
- **Manual CAPTCHA solving** - First query may require human verification
- **Python dependency** - Requires Python 3.8+ on your system

**Google AI Mode:**
- **Rate limits** - Frequent searches may trigger CAPTCHAs
- **Public search only** - No authentication required or supported
- **Query quality matters** - Vague queries may not trigger AI overviews

---

## FAQ

**Why doesn't this work in the Claude web UI?**
The web UI runs skills in a sandbox without network access. Browser automation requires network access to reach Google.

**How is this different from the MCP server?**
This is a simpler, Python-based implementation that runs directly as a Claude Skill. The MCP server is more feature-rich and works with multiple tools (Codex, Cursor, etc.).

**Can I use both this skill and the MCP server?**
Yes, but you probably don't need both. Use the skill for Claude Code, use the MCP server if you want multi-agent support (Cursor, Cline, etc.).

**Is it free?**
Yes. The skill is open source, and it uses public Google Search. No API keys or subscriptions needed.

**Is my data private?**
Everything runs locally on your machine. The browser profile stays on your computer. No credentials or external services required beyond Google Search.

**What if the browser keeps crashing?**
Clear the browser profile (see Troubleshooting section) and try again.

---

## Important Notes

**CAPTCHA handling:**
Google may show a CAPTCHA on first use. Tell Claude to show the browser, solve it manually, and you're good to go for future searches.

**Responsible use:**
This tool automates browser interactions with Google Search. Use it responsibly and be mindful of Google's Terms of Service. Add delays between heavy search sessions if needed.

**Verification:**
While results come from Google's AI Mode with source citations, always verify critical information via the linked sources. This is a research tool, not a source of truth.

---

## MCP Server Alternative

**Using other code agents (Cursor, Codex, Cline, Windsurf)?**

There's a full **MCP server version** of this tool that works with any MCP-compatible agent, not just Claude Code.

**Check it out:** [google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)

The MCP version offers:
- Works with Claude Code, Codex, Cursor, Cline, Windsurf, Zed, etc.
- TypeScript implementation
- npm package distribution
- One-line installation: `claude mcp add google-ai-search npx google-ai-mode-mcp@latest`

If you only use Claude Code, this skill is perfect. If you use multiple agents, consider the MCP server instead.

---

## Contributing

Found an issue or want to contribute?

- Report bugs: [GitHub Issues](https://github.com/PleasePrompto/google-ai-mode-skill/issues)
- Pull requests: Welcome
- Contact: See parent repository

---

## License

MIT License - see LICENSE file for details

---

## Credits

This skill is inspired by the [**Google AI Mode MCP Server**](https://github.com/PleasePrompto/google-ai-mode-mcp) and provides an alternative implementation as a Claude Code Skill:
- Both use Patchright for browser automation (MCP uses TypeScript, Skill uses Python)
- Skill version runs directly in Claude Code without MCP protocol
- Optimized for Claude Code's skill architecture

If you need:
- **Multi-agent support** (Cursor, Cline, etc.) → Use the [MCP Server](https://github.com/PleasePrompto/google-ai-mode-mcp)
- **Claude Code only** → Use this skill
- **npm distribution** → Use the [MCP Server](https://github.com/PleasePrompto/google-ai-mode-mcp)
- **Git clone simplicity** → Use this skill

---

## The Bottom Line

**Without this skill**: Claude searches Google → Gets links → Reads 5-10 pages → Thousands of tokens → Potential hallucinations

**With this skill**: Claude queries Google AI Mode → Gets one synthesized answer with citations → Minimal tokens → Grounded results

Stop burning tokens on web research. Start getting accurate, cited answers directly in Claude Code.

```bash
# Get started in 30 seconds
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/google-ai-mode-skill google-ai-mode
# Open Claude Code: "What are my skills?"
```

---

<div align="center">

Built as a Claude Code Skill adaptation of the [Google AI Mode MCP Server](https://github.com/PleasePrompto/google-ai-mode-mcp)

For free, token-efficient web research directly in Claude Code

</div>
