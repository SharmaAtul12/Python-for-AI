import os

# read from environment
api_key = os.environ.get('API_KEY_PYTHON')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using database: {database}")
print(f"Using API key: {api_key}")


# Windows
# export API_KEY_PYTHON=sk-1234567890abcdef
# python app.py

#! USing python-dotenv

from dotenv import load_dotenv 

# load .env file -> return True if .env file is found and loaded, else False

load_dotenv()

# or do load_dotenv(dotenv_path='path/to/.env') to load a specific .env file