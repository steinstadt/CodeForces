# Problem 617 A - Elephant

# input
x = int(input())

# initialization
count = 0

# count
for i in range(5, 0, -1):
    if x-i>=0:
        count += x//i
        x = x%i

# output
print(count)
