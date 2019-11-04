from functools import reduce


def main():
    print("Filter Map Reduce")
    arr = list()
    num = input("Enter the number of element you want:::")
    for i in range(0, int(num)):
        n = input("num:")
        arr.append(n)
    # filter
    # print(arr)
    brr = list(filter(lambda no: ((int(no) >= 70) & (int(no) <= 90)), arr))
    print("Filter", brr)
    crr = list(map(lambda no: int(no) + 10, brr))
    print("Map", crr)
    ans = 1
    drr = reduce(lambda no, no1: int(no) * int(no1), crr)
    print("Reduce", drr)


if __name__ == "__main__":
    main()
