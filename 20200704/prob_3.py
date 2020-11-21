# Problem 1348 A - Phoenix and Balance

# input
t = int(input())

# count
for i in range(t):
    n = int(input())
    n_l = n // 2
    tmp_1 = 0
    tmp_2 = 0
    for j in range(1, n):
        if j<n_l:
            tmp_1 += 2**j
        else:
            tmp_2 += 2**j
    tmp_1 += 2**n
    print(abs(tmp_1-tmp_2))
