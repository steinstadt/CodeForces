# Problem 228 A - Is your horseshoe on the other hoof?

# input
s_list = list(map(int, input().split()))

# initialization
ans = 4 - len(set(s_list))

# output
print(ans)
