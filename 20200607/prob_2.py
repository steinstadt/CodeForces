# Problem 268 A - Games

# input
n = int(input())
uniforms = [[0,0] for i in range(n)]
for i in range(n):
    h, a = map(int, input().split())
    uniforms[i][0] = h
    uniforms[i][1] = a

# initialization
count = 0

# count
for i in range(n):
    t = uniforms[i][1]
    for j in range(n):
        if i==j:
            continue
        if uniforms[j][0]==t:
            count += 1

# output
print(count)
