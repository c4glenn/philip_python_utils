import time

from philip_utils import progress_bars

def generator(n):
    for i in range(n):
        yield i

def test_progress_bars():
    for i in progress_bars(range(2), color='red'):
        for j in progress_bars(range(3), color='green'):
            for k in progress_bars(generator(4), total=4, color='blue'):
                for l in progress_bars(generator(5)):
                    print(i, j, k, l)
                    time.sleep(0.05)


if __name__ == "__main__":
    print(f"TESTING PROGRESS BARS")
    test_progress_bars()