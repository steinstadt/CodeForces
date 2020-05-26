# Problem 110 A - Nearly Lucky Number

# input
n_list = list(input())

# initialization
count = 0

# check
for n in n_list:
    if n=='4' or n=='7':
        count += 1

# output
if count==4 or count==7:
    print("YES")
else:
    print("NO")
