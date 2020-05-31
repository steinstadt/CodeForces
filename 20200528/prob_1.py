# Problem 467 A - George and Accommondation

# input
n = int(input())

# initialization
count = 0

# count
for i in range(n):
    p, q = map(int, input().split())
    if q-p>=2:
        count += 1

# output
print(count)
