import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# Always load the .env that lives next to this file so CWD doesn't matter
_ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=_ENV_PATH)


SUPABASE_KEY= os.getenv("SUPABASE_KEY")
SUPABASE_URL= os.getenv("SUPABASE_URL")
SUPABASE_JWT_SECRET= os.getenv("SUPABASE_JWT_SECRET")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



