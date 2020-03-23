# Problem 158 A - Next Round

# input
n, k = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
ans_count = 0
check_num = a_list[k-1]

# check
for a in a_list:
    if a>0 and a>=check_num:
        ans_count += 1

# output
print(ans_count)
