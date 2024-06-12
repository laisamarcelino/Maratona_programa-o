def aVeryBigSum(ar):
    sumNumbers = 0
    for i in range(len(ar)):
        sumNumbers += ar[i]
    return sumNumbers

print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))