import os

HOOKPY_ENABLE_NAME = "HOOKPY_ENABLE"
HOOKPY_ENABLE = os.getenv(HOOKPY_ENABLE_NAME, "0") != "0"
HOOKPY_CONFIG_PATH_NAME = "HOOKPY_CONFIG_PATH"
HOOKPY_CONFIG_PATH = os.getenv(HOOKPY_CONFIG_PATH_NAME, "")