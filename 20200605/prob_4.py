# Problem 469 A - I Wanna Be the Guy

# input
n = int(input())
x_nums = list(map(int, input().split()))
y_nums = list(map(int, input().split()))

# initialization
nums = [0] * n

# count x
x_i = x_nums[0]
i = 1
if x_i>0:
    while i<=x_i:
        x = x_nums[i]
        nums[x-1] = 1
        i += 1

y_i = y_nums[0]
i = 1
if y_i>0:
    while i<=y_i:
        y = y_nums[i]
        nums[y-1] = 1
        i += 1

# set
nums = list(set(nums))

# output
if nums[0]==1 and len(nums)==1:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
