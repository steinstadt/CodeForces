# Problem B - Balanced Array

# input
t = int(input())

# count
for i in range(t):
    n = int(input())
    tmp = n // 2
    if tmp%2==1:
        print("NO")
    else:
        ans = [0]*n
        tmp_sum1 = 0
        tmp_sum2 = 0
        # even number
        for i in range(tmp):
            ans[i] = (i+1)*2
            tmp_sum1 += (i+1)*2
        # odd number
        for i in range(tmp, n-1):
            ans[i] = (i-tmp)*2 + 1
            tmp_sum2 += (i-tmp)*2 + 1
        ans[n-1] = tmp_sum1 - tmp_sum2
        print("YES")
        print(" ".join(list(map(str, ans))))
