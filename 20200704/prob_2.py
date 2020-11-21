# Problem 703 A - Mishka and Game

# input
n = int(input())

# initialization
mishka_count = 0
chris_count = 0

# count
for i in range(n):
    m, c = map(int, input().split())
    if m>c:
        mishka_count += 1
    elif m<c:
        chris_count += 1

# output
if mishka_count>chris_count:
    print("Mishka")
elif mishka_count<chris_count:
    print("Chris")
else:
    print("Friendship is magic!^^")
