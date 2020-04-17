import time
from multiprocessing import Process, Event, Semaphore, Lock


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == '__main__':
    NUMBER = 100000
    start = time.time()
    factorial(NUMBER)
    factorial(NUMBER)
    factorial(NUMBER)
    factorial(NUMBER)
    print('Time:', time.time() - start)

    p1 = Process(target=factorial, args=(NUMBER, ))
    p2 = Process(target=factorial, args=(NUMBER, ))
    p3 = Process(target=factorial, args=(NUMBER, ))
    p4 = Process(target=factorial, args=(NUMBER, ))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print('Time:', time.time() - start)
