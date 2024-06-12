X = int(input())

res = X//10

if X%10 > 0:
	res += 1
print(res)