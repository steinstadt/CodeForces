# Problem 723 A - The New Year: Meeting Friends

# input
x_nums = list(map(int, input().split()))

# initialization
x_max = max(x_nums)
x_min = min(x_nums)
dist_min = float('INF')

# count
for i in range(x_min, x_max+1):
    tmp = 0
    for x in x_nums:
        tmp += abs(i-x)
    dist_min = min(dist_min, tmp)

# output
print(dist_min)
