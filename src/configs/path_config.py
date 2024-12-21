# src/configs/path_config.py
import os
from dotenv import load_dotenv

load_dotenv()

class EnvSettings:
    """Class to store environment settings."""

    SETTINGS = {
        'PROJECT_ROOT': 'PROJECT_ROOT',
        'ENTRY_POINT': 'ENTRY_POINT',
        'DOCS_PATH': 'DOCS_PATH', 
        'RAW_DATA_PATH': 'RAW_DATA_PATH', 
        'CLEANED_DATA_PATH': 'CLEANED_DATA_PATH', 
    }

    def __init__(self):
        """Initialize the settings and set attributes."""
        for attr, env_var in self.SETTINGS.items():
            value = os.getenv(env_var)
            if value and '${PROJECT_ROOT}' in value:
                project_root = os.getenv('PROJECT_ROOT')
                value = value.replace('${PROJECT_ROOT}', project_root)
            setattr(self, attr, value)

env_settings = EnvSettings()

# Expose the settings at the module level
for attr in EnvSettings.SETTINGS:
    globals()[attr] = getattr(env_settings, attr)

def get_path_settings():
    """Return all path settings as a dictionary."""
    return {
        "PROJECT_ROOT": env_settings.PROJECT_ROOT,
        "ENTRY_POINT": env_settings.ENTRY_POINT,
        "DOCS_PATH": env_settings.DOCS_PATH,
        "RAW_DATA_PATH": env_settings.RAW_DATA_PATH,
        "CLEANED_DATA_PATH": env_settings.CLEANED_DATA_PATH,
    }
