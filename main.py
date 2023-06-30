import colcon as c
from pprint import pprint


def main():
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


if __name__ == "__main__":
    main()
