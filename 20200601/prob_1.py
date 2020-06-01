# Problem 705 A - Hulk

# input
n = int(input())

# initialization
ans = ""

# count
for i in range(1, n+1):
    if i%2==0:
        if i==n:
            ans += "I love it"
        else:
            ans += "I love that "
    else:
        if i==n:
            ans += "I hate it"
        else:
            ans += "I hate that "

# output
print(ans)
