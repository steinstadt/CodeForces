# Problem 443 A - Anton and Letters

# input
S = input()
S = S.strip("{}").split(", ")

# initialization
ans = 0
if len(S)==1 and S[0]=="":
    ans = 0
else:
    ans = len(set(S))

# output
print(ans)
