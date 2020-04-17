from threading import Event, Thread


def print_text(text, count, event_wait, event_set):
    for _ in range(count):
        event_wait.wait()
        event_wait.clear()
        print(text)
        event_set.set()


if __name__ == '__main__':
    e1 = Event()
    e2 = Event()
    e1.set()

    t1 = Thread(target=print_text, args=('A', 10, e1, e2))
    t2 = Thread(target=print_text, args=('B', 10, e2, e1))
    t1.start()
    t2.start()
