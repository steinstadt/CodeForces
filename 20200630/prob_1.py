# Problem A - New Year and Hurry

# input
n, k = map(int, input().split())

# initialization
remain = 240 - k
count = 0

# count
i = 1
while remain-5*i>=0:
    count += 1
    remain -= 5*i
    i += 1
    if count>=n:
        break

# output
print(count)
