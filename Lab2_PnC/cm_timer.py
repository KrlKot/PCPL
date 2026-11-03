import time
import contextlib

class cm_timer_1:
    def __enter__(self):
        self.start = time.perf_counter()
        return self


    def __exit__(self, exc_type, exc, tb):
        result = time.perf_counter() - self.start
        print(result)

@contextlib.contextmanager
def cm_timer_2():
    start = time.perf_counter()
    yield
    result = time.perf_counter() - start
    print(result)

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)
