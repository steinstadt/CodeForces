# Problem 432 A - Choosing Teams

# input
n, k = map(int, input().split())
y_nums = list(map(int, input().split()))

# initialization
count = 0

# count
for i in range(n):
    y_nums[i] += k

# team create
for y in y_nums:
    if y<=5:
        count += 1

# output
print(count//3)
