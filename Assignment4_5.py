import functools
from functools import *
from typing import List

from prime_module import *


def main():
    print("Filter Map Reduce")
    arr = list()
    num = input("Enter the number of element you want:::")
    for i in range(0, int(num)):
        n = input("num:")
        arr.append(n)

    filterarr = list(filter(prime, arr))
    print("List of Filter", filterarr)
    maparr = list(map(lambda no: int(no) * 2, filterarr))
    print("List of Map", maparr)

    # reducearray = reduce(pr, maparr)
    # reducearray=reduce(functools.partial(Max, some_var=True), crr)
    reducearray = reduce(Max, maparr)
    # reducearray=reduce(lambda max, current: max if (max > current) else current, crr)
    print("Reduce {} is".format(reducearray))


if __name__ == "__main__":
    main()
