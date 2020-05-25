# Problem 977 A - Wrong Subtraction

# input
n, k = map(int, input().split())
n = str(n)

# count
for i in range(k):
    tmp = int(n)
    if n[-1]=='0':
        tmp = tmp // 10
        n = str(tmp)
    else:
        tmp -= 1
        n = str(tmp)

# output
print(n)
