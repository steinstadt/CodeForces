# Problem 263 A - Beautiful Matrix

# input
row_d = 0
col_d = 0
ans = 0
for i in range(5):
    s = list(input().split())
    for j in range(5):
        c = s[j]
        if c=='1':
            row_d = abs(i - 2)
            col_d = abs(j - 2)
            ans = row_d + col_d

# output
print(ans)
