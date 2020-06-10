# Problem 141 A - Amusing Joke

# input
s_1 = "".join(sorted(input()))
s_2 = "".join(sorted(input()))
s_3 = "".join(sorted(input()))

# initialization
ans = "".join(sorted(s_1 + s_2))

# output
if ans==s_3:
    print("YES")
else:
    print("NO")
