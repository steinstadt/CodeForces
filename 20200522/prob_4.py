# Problem 791 A - Bear and Big Brother

# input
a, b = map(int, input().split())

# initialization
year = 0

# count
while a<=b:
    year += 1
    a *= 3
    b *= 2

# output
print(year)
