# Problem 282 A - Bit++

# input
n = int(input())

# initialization
result = 0

# operation
for i in range(n):
    s = input()
    if '+' in s:
        result += 1
    else:
        result -= 1

# output
print(result)
