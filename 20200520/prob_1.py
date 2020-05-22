# Problem 236 A - Boy or Girl

# input
s = list(input())

# initialization
s_len = len(set(s))

# output
if s_len%2==0:
    print("CHAT WITH HER!");
else:
    print("IGNORE HIM!")
