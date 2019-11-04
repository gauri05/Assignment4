def main():
    print("a program which contains one lambda function which accepts two parameters and return its multiplication")
    num1, num2 = [int(num1) for num1 in input("Enter 2 number::").split()]

    ans = lambda num1, num2: int(num1) * int(num2)
    ret = ans(num1, num2)
    print("Ans::", ret)


if __name__ == "__main__":
    main()
