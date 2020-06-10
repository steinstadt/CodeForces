# Problem 148 A - Insomnia cure

# input
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

# initialization
ans = 0
num = [k, l, m, n]

# count
for i in range(1, d+1):
    for j in num:
        if i%j==0:
            ans += 1
            break

# output
print(ans)
