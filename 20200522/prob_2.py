# Problem 116 A - Tram

# input
n = int(input())

# initialization
ans = 0
tmp = 0

# count
for i in range(n):
    a, b = map(int, input().split())
    tmp -= a
    tmp += b
    ans = max(ans, tmp)

# output
print(ans)
