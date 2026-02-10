"""
Global configuration module for environment variables.
This module loads environment variables once at import time,
eliminating the need to call load_dotenv in multiple files.
"""

from dotenv import load_dotenv

# Load environment variables once
load_dotenv(dotenv_path='.env')
