def prime(arr):
    # print(arr)
    brr = list()
    print("Len of arr", len(arr))  # range(0,len(arr))
    for i in arr:
        flag = False
        # print("arr",arr)
        # print("arr[i]", i)
        for j in range(2, int(arr)):
            if int(arr) % j == 0:
                flag = True  # not prime
                break
        # print(flag)
        if not flag:
            # sum = sum + int(arr[i])
            brr.append(arr)
    # print("&&&&&",brr)
    return brr


def Max(*arr):
    print(arr)
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
