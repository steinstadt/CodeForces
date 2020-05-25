# Problem 546 A - Soldier and Bananas

# input
k, n, w = map(int, input().split())

# initialization
tmp = (k * w * (w + 1)) // 2
ans = tmp - n

if ans>=0:
    print(ans)
else:
    print(0)
