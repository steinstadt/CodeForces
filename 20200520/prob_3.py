# Problem 1355 A - Sequence with Digits

# input
t = int(input())

# count
for i in range(t):
    a, k = map(int, input().split())
    for j in range(k-1):
        tmp = list(str(a))
        tmp = list(map(int, tmp))
        tmp_min = min(tmp)
        tmp_max = max(tmp)
        if tmp_min==0:
            break
        a = a + tmp_min * tmp_max
    # output
    print(a)
