# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SQL Server settings
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_DRIVER = os.getenv("SQL_DRIVER", "ODBC Driver 17 for SQL Server")



# Optional: Validate required variables
required_vars = [SQL_SERVER, SQL_DATABASE]
if not all(required_vars):
    raise EnvironmentError("Missing one or more required database environment variables.")



