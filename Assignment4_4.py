from functools import reduce


def main():
    print("Filter Map Reduce")
    arr = list()
    num = input("Enter the number of element you want:::")
    for i in range(0, int(num)):
        n = input("num:")
        arr.append(n)

    brr = list(filter(lambda no: (int(no) % 2 == 0), arr))
    print("Filter", brr)
    crr = list(map(lambda no: int(no) * int(no), brr))
    print("Map", crr)
    drr = reduce(lambda no, no1: int(no) + int(no1), crr)
    print("Reduce", drr)


if __name__ == "__main__":
    main()
