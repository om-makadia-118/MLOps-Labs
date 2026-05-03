#!/usr/bin/env python3
"""Pipeline utility functions for MLOps workflows."""
import os
import json
from pathlib import Path
from typing import Dict, List, Any

def ensure_dir(directory: str) -> Path:
    """Create directory if it doesn't exist.
    
    Args:
        directory: Path to directory
        
    Returns:
        Path object
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path

def read_json(file_path: str) -> Dict[str, Any]:
    """Read JSON config file safely.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Parsed JSON as dict
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def format_duration(seconds: float) -> str:
    """Convert seconds to human-readable duration.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Formatted string (e.g., '2m 30s')
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}m {secs}s" if minutes else f"{secs}s"

if __name__ == "__main__":
    ensure_dir("logs")
    print(f"Created logs dir: {ensure_dir('logs')}")
    print(format_duration(125.5))  # Test duration
