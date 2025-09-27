import requests
import time
import random
from keep_alive import keep_alive

# Jalankan server kecil biar Replit gak tidur
keep_alive()

# URL landing page lo
url = "http://freepalcoin.netlify.app/"

# Daftar user agent biar keliatan natural
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
]

print("🚀 Bot traffic FPC sudah jalan...")

while True:
    headers = {"User-Agent": random.choice(user_agents)}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        print(f"[{res.status_code}] Visit {url}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # jeda 5–15 detik biar natural
    time.sleep(random.randint(5, 15))
