# Problem 1352 B - Same Parity Summands

# input
t = int(input())

# count
for i in range(t):
    n, k = map(int, input().split())
    ans = [0]*k
    is_ok = False

    # even check
    if n%2==0 and n>=2*k:
        is_ok = True
        for j in range(k-1):
            ans[j] = 2
        ans[k-1] = n - 2*(k-1)
    elif n>=k and (n-k)%2==0:
        is_ok = True
        for j in range(k-1):
            ans[j] = 1
        ans[k-1] = n - (k-1)

    # output
    if is_ok:
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")
