# Problem 734 A - Anton and Danik

# input
n = int(input())
games = list(input())

# initialization
anton_count = 0
danik_count = 0

# count
for i in range(n):
    g = games[i]
    if g=='A':
        anton_count += 1
    else:
        danik_count += 1

# output
if anton_count>danik_count:
    print("Anton")
elif anton_count<danik_count:
    print("Danik")
else:
    print("Friendship")
