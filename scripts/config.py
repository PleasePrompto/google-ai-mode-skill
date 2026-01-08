"""
Configuration for Google AI Mode Skill
Minimal config - no auth, no persistence needed
"""

from pathlib import Path
import os
import sys

# Paths
SKILL_DIR = Path(__file__).parent.parent
RESULTS_DIR = SKILL_DIR / "results"
LOGS_DIR = SKILL_DIR / "logs"

# Browser Profile - persistent context to avoid CAPTCHAs!
# Store in user's home directory for persistence across sessions
# Platform-specific cache directories:
# - Windows: %LOCALAPPDATA%\google-ai-mode-skill\chrome_profile
# - macOS: ~/Library/Caches/google-ai-mode-skill/chrome_profile
# - Linux: ~/.cache/google-ai-mode-skill/chrome_profile
if sys.platform == "win32":
    # Windows: Use AppData\Local
    BROWSER_PROFILE_DIR = Path(os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "google-ai-mode-skill" / "chrome_profile"
elif sys.platform == "darwin":
    # macOS: Use ~/Library/Caches
    BROWSER_PROFILE_DIR = Path.home() / "Library" / "Caches" / "google-ai-mode-skill" / "chrome_profile"
else:
    # Linux/Unix: Use ~/.cache
    BROWSER_PROFILE_DIR = Path.home() / ".cache" / "google-ai-mode-skill" / "chrome_profile"

BROWSER_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

# Browser Configuration
BROWSER_ARGS = [
    '--disable-blink-features=AutomationControlled',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--no-first-run',
    '--no-default-browser-check',
    '--lang=en',  # CRITICAL: Must be 'en' not 'en-US' for UI language!
    '--disable-translate',  # Disable auto-translate popup
]

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Locale settings for consistent language
LOCALE = "en-US"
EXTRA_HTTP_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9"
}

# Timeouts
PAGE_LOAD_TIMEOUT = 45000  # 45 seconds
AI_RESPONSE_TIMEOUT = 30    # 30 seconds
