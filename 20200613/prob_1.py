# Problem 581 A - Vasya the Hipster

# input
a, b = map(int, input().split())

# initialization
fashion_days = min(a, b)
tmp = max(a, b) - min(a, b)
same_days = tmp // 2

# outout
print(fashion_days, same_days)
