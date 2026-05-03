#!/usr/bin/env python3
"""Color logging utility for MLOps pipeline stages."""
import logging
from termcolor import colored

class ColorFormatter(logging.Formatter):
    """Custom formatter with color codes for log levels."""
    
    COLORS = {
        'DEBUG': 'cyan',
        'INFO': 'green', 
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'magenta'
    }
    
    def format(self, record):
        log_message = super().format(record)
        color = self.COLORS.get(record.levelname, 'white')
        return colored(log_message, color)

def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Setup logger with color formatter."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    handler = logging.StreamHandler()
    formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = setup_logger("test")
    logger.debug("Debug message")
    logger.info("Info message") 
    logger.warning("Warning message")
    logger.error("Error message")
