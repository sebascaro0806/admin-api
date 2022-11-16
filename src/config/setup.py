from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class AppSettings:
    
    #Api settings
    PROJECT_NAME = "ISA_2 - API Administration"
    PROJECT_VERSION = "0.0.1"
    PROJECT_DESCRIPTION = "API para manejar la administracion"
    URL_PREFIX="/api/v1"

settings = AppSettings()