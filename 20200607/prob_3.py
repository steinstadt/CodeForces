# Problem 520 A - Pangram

# input
n = int(input())
s = list(input().lower())

# initialization
s_len = len(set(s))

# output
if s_len==26:
    print("YES")
else:
    print("NO")
