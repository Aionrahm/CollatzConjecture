import colcon as c
from pprint import pprint
import random


def main():
    result = []
    j = random.randint(1, 1000000)
    while j >= 2:
        j = c.is_odd_even(j)
        result.append(j)
    print(result)
    plotting(result)

def multi():
    result = []
    for i in range(100, 10000):
        r = []
        j = i
        while j >= 2:
            j = c.is_odd_even(j)
            r.append(j)
        result.append(r)
    for res in result:
        pprint(len(res))

def plotting(r):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(r)
    plt.show()

if __name__ == "__main__":
    main()
