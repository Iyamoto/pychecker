# PoC for internal Docker infrastructure HTTP checker

import requests
import time
import fire
import collections

url = 'http://www.google.com:80'
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
    limit = 2
    data = collections.defaultdict(int)

    while True:
        c += 1
        try:
            r = requests.get(url, timeout=requesttimeout)
        except requests.exceptions.RequestException as e:
            error = type(e).__name__
            # print(error)
            data[error] += 1
            # return type(e).__name__

        if timeout > 0:
            time.sleep(timeout)

        if c > limit:
            return data

if __name__ == '__main__':
  fire.Fire(check)