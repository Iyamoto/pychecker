# PoC for internal Docker infrastructure HTTP checker

import requests
import time
import fire
import collections

requests.adapters.DEFAULT_RETRIES = 0

url = 'http://127.0.0.1:80'
timeout = 1.0 # Seconds
requesttimeout = 1.0 # Seconds
limit = 15 # Seconds

def check(url=url, timeout=timeout, requesttimeout=requesttimeout, limit=limit):
    """Checks URL
    Args:
        url (str): URL to check
        timeout (float): Time between checks, seconds
        requesttimeout (float): Time between checks, seconds
        limit (int): Limit for reports
    Return:
        """
    data = collections.defaultdict(int)
    starttime = time.time()
    while True:
        try:
            r = requests.get(url, timeout=requesttimeout)
        except requests.exceptions.RequestException as e:
            error = type(e).__name__
            data[error] += 1

        if timeout > 0:
            time.sleep(timeout)

        exectime = time.time() - starttime
        if exectime > limit:
            if data:
                print(data)
                # TODO send alert

            data = collections.defaultdict(int)
            starttime = time.time()

            # TODO send to influx


if __name__ == '__main__':
  fire.Fire(check)