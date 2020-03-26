# Problem 96 A - Football

# input
s = list(input())

# initialization
zero_count = 0
one_count = 0

# count
for i in range(1,len(s)):
    # zero check
    if s[i]=='0':
        if s[i-1]=='0':
            zero_count += 1
        else:
            zero_count = 0

        if zero_count+1>=7:
            break
    else:
        if s[i-1]=='1':
            one_count += 1
        else:
            one_count = 0

        if one_count+1>=7:
            break

# output
if zero_count+1>=7 or one_count+1>=7:
    print("YES")
else:
    print("NO")
