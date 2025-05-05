import os
from dotenv import load_dotenv

class ConfigService:
    def __init__(self):
        load_dotenv()

    def get_env_variable(self, var_name, default=None):
        return os.getenv(var_name, default)