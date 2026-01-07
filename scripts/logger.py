"""
Logging System for Google AI Mode Skill
Provides comprehensive debug logging with file and console output
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


class SkillLogger:
    """Zentrales Logging-System für Google AI Mode Skill"""

    def __init__(self, debug: bool = False):
        self.debug_enabled = debug
        self.logger = None
        self.log_file = None

        if debug:
            self._setup_logger()

    def _setup_logger(self):
        """Konfiguriert Logger mit File und Console Handlers"""
        # Log-Ordner erstellen
        log_dir = Path(__file__).parent.parent / "logs"
        log_dir.mkdir(exist_ok=True)

        # Timestamp-basierter Log-Filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = log_dir / f"search_{timestamp}.log"

        # Logger konfigurieren
        self.logger = logging.getLogger("GoogleAIMode")
        self.logger.setLevel(logging.DEBUG)

        # Clear existing handlers (avoid duplicates)
        self.logger.handlers.clear()

        # File Handler - speichert ALLE Debug-Infos
        fh = logging.FileHandler(self.log_file, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # Console Handler - nur wichtige Meldungen
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)

        # Format mit Timestamp
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        self.logger.info(f"Debug logging enabled - Log file: {self.log_file}")

    def debug(self, msg):
        """Debug-level logging (nur in File, nicht in Console)"""
        if self.debug_enabled and self.logger:
            self.logger.debug(msg)

    def info(self, msg):
        """Info-level logging (in File und Console)"""
        if self.debug_enabled and self.logger:
            self.logger.info(msg)

    def warning(self, msg):
        """Warning-level logging (in File und Console)"""
        if self.debug_enabled and self.logger:
            self.logger.warning(msg)

    def error(self, msg):
        """Error-level logging (in File und Console)"""
        if self.debug_enabled and self.logger:
            self.logger.error(msg)

    def exception(self, msg):
        """Exception-level logging mit Traceback"""
        if self.debug_enabled and self.logger:
            self.logger.exception(msg)


# Dummy-Logger für non-debug Modus
class DummyLogger:
    """Dummy-Logger der nichts tut (für non-debug mode)"""
    def __init__(self):
        self.debug_enabled = False
        self.log_file = None

    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def exception(self, msg):
        pass


def get_logger(debug: bool = False):
    """Factory function für Logger"""
    if debug:
        return SkillLogger(debug=True)
    else:
        return DummyLogger()
