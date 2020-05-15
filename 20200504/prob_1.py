# Problem 1341 A. Nastya and Rice

# 5
# 7 20 3 101 18
# 11 11 10 234 2
# 8 9 7 250 122
# 19 41 21 321 10
# 3 10 8 6 1

t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    ab_max = (a + b) * n
    ab_min = (a - b) * n
    if ab_max>=(c-d) and ab_min<=(c+d):
        print("Yes")
    else:
        print("No")
