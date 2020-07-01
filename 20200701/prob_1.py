# 427 A - Police Recruits

# input
n = int(input())
t_nums = list(map(int, input().split()))

# initialization
bucket = 0
count = 0

# count
for t in t_nums:
    if t==-1:
        if bucket+t<0:
            count += 1
        else:
            bucket += t
    else:
        bucket += t

# output
print(count)
