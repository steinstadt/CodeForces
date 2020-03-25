# Problem 112 A - Petya and Strings

# input
first_s = input().lower()
second_s = input().lower()

# output
if first_s==second_s:
    print(0)
elif first_s<second_s:
    print(-1)
else:
    print(1)
