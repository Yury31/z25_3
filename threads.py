import time
import threading


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def print_text(text, count):
    for _ in range(count):
        print(text)


if __name__ == '__main__':
    t1 = threading.Thread(target=print_text, args=('A', 10))
    t2 = threading.Thread(target=print_text, args=('B', 10))
    t1.start()
    t2.start()
    NUMBER = 100000
    start = time.time()
    factorial(NUMBER)
    factorial(NUMBER)
    factorial(NUMBER)
    print('Time:', time.time() - start)

    thread1 = threading.Thread(target=factorial, args=(NUMBER, ))
    thread2 = threading.Thread(target=factorial, args=(NUMBER, ))
    thread3 = threading.Thread(target=factorial, args=(NUMBER, ))

    start = time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print('Time:', time.time() - start)