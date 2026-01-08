"""
Browser Utilities for Google AI Mode Skill
Uses persistent context to avoid CAPTCHAs
"""

import time
import random
from typing import Optional

from patchright.sync_api import Playwright, Browser, BrowserContext, Page
from config import BROWSER_ARGS, USER_AGENT, BROWSER_PROFILE_DIR, LOCALE, EXTRA_HTTP_HEADERS


class BrowserFactory:
    """Factory for creating configured browser instances"""

    @staticmethod
    def launch_persistent_context(playwright: Playwright, headless: bool = True) -> BrowserContext:
        """
        Launch browser with PERSISTENT CONTEXT - keeps cookies/session!
        This dramatically reduces CAPTCHA occurrences.

        Sets English as preferred language (but multi-language selectors handle any locale).
        """
        import json

        # Step 1: Set Local State (profile-wide settings)
        local_state_file = BROWSER_PROFILE_DIR / "Local State"
        local_state = {}
        if local_state_file.exists():
            try:
                with open(local_state_file, 'r', encoding='utf-8') as f:
                    local_state = json.load(f)
            except:
                local_state = {}

        # Force English in Local State
        local_state.update({
            "intl": {
                "app_locale": "en",  # CRITICAL: Chrome UI language
                "accept_languages": "en-US,en"
            }
        })

        with open(local_state_file, 'w', encoding='utf-8') as f:
            json.dump(local_state, f, indent=2)

        # Step 2: Set Default/Preferences (per-profile settings)
        prefs_dir = BROWSER_PROFILE_DIR / "Default"
        prefs_dir.mkdir(parents=True, exist_ok=True)
        prefs_file = prefs_dir / "Preferences"

        prefs = {}
        if prefs_file.exists():
            # Load existing preferences to preserve cookies/session
            try:
                with open(prefs_file, 'r', encoding='utf-8') as f:
                    prefs = json.load(f)
            except:
                prefs = {}

        # FORCE English language settings
        prefs.update({
            "intl": {
                "accept_languages": "en-US,en",
                "selected_languages": "en-US,en",
                "app_locale": "en"  # Redundant but ensures consistency
            },
            "translate": {
                "enabled": False  # Disable auto-translate
            },
            "webkit": {
                "webprefs": {
                    "default_charset": "utf-8"
                }
            }
        })

        # Write preferences atomically
        with open(prefs_file, 'w', encoding='utf-8') as f:
            json.dump(prefs, f, indent=2)

        # NOW launch browser (will read our forced preferences)
        return playwright.chromium.launch_persistent_context(
            str(BROWSER_PROFILE_DIR),  # Persistent profile directory
            channel="chrome",  # Use real Chrome for better anti-detection
            headless=headless,
            user_agent=USER_AGENT,
            locale=LOCALE,  # Force English locale
            extra_http_headers=EXTRA_HTTP_HEADERS,  # Force English language headers
            args=BROWSER_ARGS,
            ignore_default_args=["--enable-automation"],
        )

    @staticmethod
    def launch_browser(playwright: Playwright, headless: bool = True) -> Browser:
        """
        Launch browser with anti-detection features.
        DEPRECATED: Use launch_persistent_context instead to avoid CAPTCHAs!
        """
        return playwright.chromium.launch(
            channel="chrome",  # Use real Chrome for better anti-detection
            headless=headless,
            args=BROWSER_ARGS
        )


class StealthUtils:
    """Human-like interaction utilities"""

    @staticmethod
    def random_delay(min_ms: int = 100, max_ms: int = 500):
        """Add random delay"""
        time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))

    @staticmethod
    def human_type(page: Page, selector: str, text: str, wpm_min: int = 320, wpm_max: int = 480):
        """Type with human-like speed"""
        element = page.query_selector(selector)
        if not element:
            # Try waiting if not immediately found
            try:
                element = page.wait_for_selector(selector, timeout=2000)
            except:
                pass

        if not element:
            print(f"⚠️ Element not found for typing: {selector}")
            return

        # Click to focus
        element.click()

        # Type
        for char in text:
            element.type(char, delay=random.uniform(25, 75))
            if random.random() < 0.05:
                time.sleep(random.uniform(0.15, 0.4))

    @staticmethod
    def realistic_click(page: Page, selector: str):
        """Click with realistic movement"""
        element = page.query_selector(selector)
        if not element:
            return

        # Optional: Move mouse to element (simplified)
        box = element.bounding_box()
        if box:
            x = box['x'] + box['width'] / 2
            y = box['y'] + box['height'] / 2
            page.mouse.move(x, y, steps=5)

        StealthUtils.random_delay(100, 300)
        element.click()
        StealthUtils.random_delay(100, 300)
