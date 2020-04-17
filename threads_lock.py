import time
from threading import Lock, Semaphore, Thread


def print_text(text, count, lock=None):
    with lock:
        for _ in range(count):
            print(text)
            time.sleep(0.5)


if __name__ == '__main__':
    sem = Semaphore(1)
    lock = Lock()
    t1 = Thread(target=print_text, args=('A', 10, lock))
    t2 = Thread(target=print_text, args=('B', 10, lock))
    t3 = Thread(target=print_text, args=('C', 10, lock))
    t1.start()
    t2.start()
    t3.start()
