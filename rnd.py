# PoC for internal Docker infrastructure HTTP checker

import requests
import time
import fire

url = 'http://127.0.0.1:8080'
timeout = 1 # Seconds

def check(url=url, timeout=timeout):
    """Checks URL"""
    while True:
        r = requests.get(url)
        if not r.ok:
            return (r.status_code, r.reason)
        time.sleep(timeout)

if __name__ == '__main__':
  fire.Fire(check)