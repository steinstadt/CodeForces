# Problem 486 A - Calculating Function

# input
n = int(input())

# initialization
even = n // 2
odd = n - even
ans = even*(even + 1) - odd**2

# output
print(ans)
