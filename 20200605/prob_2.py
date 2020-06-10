# Problem 200 B - Drinks

# input
n = int(input())
nums = list(map(int ,input().split()))

# initialization
vol_num = 0
ans = 0

# count
for i in range(n):
    vol_num += nums[i]/100

# output
ans = (vol_num/n)*100
print(ans)
