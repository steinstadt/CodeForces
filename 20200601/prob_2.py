# Problem 1030 A - In Search of an Easy Problem

# input
n = int(input())
nums = list(map(int, input().split()))

# initialization
is_easy = True

# check
for i in nums:
    if i==1:
        is_easy = False
        break

# output
if is_easy:
    print("EASY")
else:
    print("HARD")
