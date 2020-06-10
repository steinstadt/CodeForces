# Problem 785 A - Anton and Polyhedrons

# input
n = int(input())

# initialization
ans = 0

# count
for i in range(n):
    s = input()
    if s=='Icosahedron':
        ans += 20
    elif s=='Cube':
        ans += 6
    elif s=='Tetrahedron':
        ans += 4
    elif s=='Dodecahedron':
        ans += 12
    elif s=='Octahedron':
        ans += 8

# output
print(ans)
