# Problem 71 A - Way Too Long Words

# input
N = int(input())

# change
for i in range(N):
    s = input()
    if len(s)>10:
        f = s[0]
        e = s[-1]
        l = len(s)-2
        ans = f + str(l) + e
        print(ans)
    else:
        print(s)
