'''
Find missing no. in array.
'''


def missingNo(arr):
    n = len(arr)
    sumOfArr = 0

    for num in range(0,n):
        sumOfArr = sumOfArr + arr[num]
  

    sumOfNno = (n * (n+1)) // 2
    missNumber = sumOfNno - sumOfArr

    print(missNumber)



arr = [3,0,1]
missingNo(arr)
