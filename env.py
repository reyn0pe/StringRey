import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("Tidak ditemukan API_ID. Keluar...")
    raise SystemExit
if not API_HASH:
    print("Tidak ditemukan API_HASH. Keluar...")
    raise SystemExit
if not BOT_TOKEN:
    print("Tidak ditemukan BOT_TOKEN. Keluar...")
    raise SystemExit
if not DATABASE_URL:
    print("Tidak ditemukan DATABASE_URL. Keluar...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID bukan bilangan bulat yang valid. Keluar...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
