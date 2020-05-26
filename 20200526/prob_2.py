# Problem 266 B - Queue at the School

# input
n, t = map(int, input().split())
people = list(input())

# count
for i in range(t):
    j = 0
    while j<n-1:
        if people[j]=='B' and people[j+1]=='G':
            tmp = people[j]
            people[j] = people[j+1]
            people[j+1] = tmp
            j += 2
            continue
        j += 1

# output
print("".join(people))
