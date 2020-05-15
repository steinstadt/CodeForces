# Problem B - Binary Period

# input
T = int(input())

# count
for t in range(T):
    t_list = list(input())
    ans = "".join(set(t_list)) * len(t_list)
    print(ans)
