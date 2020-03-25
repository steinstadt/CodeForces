# Problem 118 A - String Task

# input
S = list(input())

# initialization
ans = []
vowels = ['A', 'O', 'Y', 'E', 'U', 'I']

# check
for s in S:
    if not s.upper() in vowels:
        tmp = '.' + s.lower()
        ans.append(tmp)

# output
print("".join(ans))
