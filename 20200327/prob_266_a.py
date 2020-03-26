# Problem 266 A - Stones on the Table

# input
n = int(input())
stones = list(input())

# initialization
result = 0

# count
for i in range(n-1):
    if stones[i]==stones[i+1]:
        result += 1

# output
print(result)
