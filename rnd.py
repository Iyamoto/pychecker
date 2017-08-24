# PoC for internal Docker infrastructure HTTP checker

import requests
import time
import fire

url = 'http://www.google.com:801'
timeout = 1 # Seconds
requests.adapters.DEFAULT_RETRIES = 1
requesttimeout = 1 # Seconds

def check(url=url, timeout=timeout, requesttimeout=requesttimeout):
    """Checks URL
    Args:
        url (str): URL to check
        timeout (int): Time between checks, seconds
        requesttimeout (int): Time between checks, seconds
    Return:
        """
    c = 0
    while True:
        c += 1
        try:
            r = requests.get(url, timeout=requesttimeout)
        except requests.exceptions.RequestException as e:
            # print(type(e).__name__)
            return type(e).__name__

        time.sleep(timeout)
        if c > 2:
            exit()

if __name__ == '__main__':
  fire.Fire(check)