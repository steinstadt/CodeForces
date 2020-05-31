# Problem 271 A - Beautiful Year

# input
y = int(input())

# count
y += 1
while True:
    tmp = list(str(y))
    tmp = len(set(tmp))
    if tmp==4:
        break
    else:
        y += 1

# output
print(y)
