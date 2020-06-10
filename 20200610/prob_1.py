# Problem 1335 A - Candies and Two Sisters

# input
t = int(input())

# count
for i in range(t):
    n = int(input())
    if n==1 or n==2:
        print(0)
        continue
    tmp = n // 2
    tmp_1 = n - tmp
    if tmp==tmp_1:
        print(tmp - 1)
    else:
        print(tmp)
