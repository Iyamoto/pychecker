# PoC for internal Docker infrastructure HTTP checker

import requests
import time
import fire

url = 'http://127.0.0.1:80'
timeout = 1 # Seconds
requests.adapters.DEFAULT_RETRIES = 1
reqesttimeout = 1 # Seconds

def check(url=url, timeout=timeout, reqesttimeout=reqesttimeout):
    """Checks URL
    Args:
        url (str): URL to check
        timeout (int): Time between checks, seconds
    Return:
        """
    while True:
        r = requests.get(url, timeout=reqesttimeout)
        if not r.ok:
            return (r.status_code, r.reason)
        else:
            return (r.status_code, r.reason)
        time.sleep(timeout)

if __name__ == '__main__':
  fire.Fire(check)