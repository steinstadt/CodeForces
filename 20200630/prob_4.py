# Problem 758 A - Holiday Of Equality

# input
n = int(input())
a_nums = list(map(int, input().split()))

# initialization
a_max = max(a_nums)
ans = 0

# check
if n==1:
    print(0)
else:
    for a in a_nums:
        ans += a_max-a
    print(ans)
