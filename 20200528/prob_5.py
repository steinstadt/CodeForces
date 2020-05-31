# Problem 677 A - Vanya and Fence

# input
n, h = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
ans = 0

# count
for a in a_nums:
    if a>h:
        ans += 2
    else:
        ans += 1

# output
print(ans)
