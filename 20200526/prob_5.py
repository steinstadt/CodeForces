# Problem 59 A - Word

# input
s = list(input())

# initialization
upper_count = 0
lower_count = 0

for n in s:
    if n.isupper():
        upper_count += 1
    else:
        lower_count += 1

# output
if lower_count>=upper_count:
    ans = "".join(s)
    ans = ans.lower()
    print(ans)
else:
    ans = "".join(s)
    ans = ans.upper()
    print(ans)
