def main():
    print("program which contains one lambda function which accepts one parameter and return power of two")
    num = input("Enter the number:")
    ans = lambda num: 2 ** int(num)
    ret = ans(num)
    print("Ans::", ret)


if __name__ == "__main__":
    main()
