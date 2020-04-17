import requests
import time
import threading

URL = 'https://wotblitz.asia/en/api/cms/news/?category=&page={page}&page_size=1'


def make_request(page):
    return requests.get(URL.format(page=page)).json()['results']


if __name__ == '__main__':
    result = []
    start = time.time()
    for page in range(1, 11, 1):
        result += make_request(page)
    print('End', time.time() - start)
    print(result)

    result = []
    threads = []
    start = time.time()
    for page in range(1, 11, 1):
        t = threading.Thread(target=make_request, args=(page, ))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    print('End', time.time() - start)
    print(result)
