# Problem 136 A - Presents

# input
n = int(input())
p_nums = list(map(int, input().split()))

# initialization
ans_nums = [0]*n

# count
for i in range(n):
    p = p_nums[i]
    ans_nums[p-1] = i + 1

# output
print(" ".join(list(map(str, ans_nums))))
