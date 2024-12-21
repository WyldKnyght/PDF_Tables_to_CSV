# src/configs/constants.py

from configs.path_config import (
    env_settings,
    DOCS_PATH,
    RAW_DATA_PATH,
    CLEANED_DATA_PATH,
)

# Application Constants
WINDOW_TITLE = "PDF Table Extractor"
WINDOW_SIZE = "1280x768"
LOADING_MESSAGE = "Processing PDF..."

# Paths (resolved dynamically using path_config)
DOCUMENTS_DIR = DOCS_PATH
RAW_DATA_DIR = RAW_DATA_PATH
CLEANED_DATA_DIR = CLEANED_DATA_PATH

# Example of using other environment variables if needed
PROJECT_ROOT = env_settings.PROJECT_ROOT
ENTRY_POINT = env_settings.ENTRY_POINT
