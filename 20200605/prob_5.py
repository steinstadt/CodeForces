# Problem 144 A - Arrival of the General

# input
n = int(input())
nums = list(map(int, input().split()))

# initialization
max_i = 0
min_i = 0
ans = 0

# max_i calc
max_n = nums[-1]
for i in range(n-1, -1, -1):
    if nums[i]>=max_n:
        max_i = i
        max_n = nums[i]

# min_i calc
min_n = nums[0]
for i in range(n):
    if nums[i]<=min_n:
        min_i = i
        min_n = nums[i]

# count
ans = max_i + (n-1-min_i)

# output
if max_i<min_i:
    print(ans)
else:
    print(ans - 1)
