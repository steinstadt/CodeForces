# Problem 344 A - Magnets

# input
n = int(input())

# initialization
magnets = [["", ""] for i in range(n)]
for i in range(n):
    m = list(input())
    magnets[i][0] = m[0]
    magnets[i][1] = m[1]
group_count = 0

# count
for i in range(n):
    if i==0:
        continue

    if magnets[i-1][1]==magnets[i][0]:
        group_count += 1

# output
print(group_count + 1)
