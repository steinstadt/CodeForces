# Problem 155 A - I love username

# input
n = int(input())
nums = list(map(int, input().split()))

# initialization
tmp_nums = [nums.pop(0)]
count = 0

# count
for num in nums:
    is_less = True
    is_more = True

    # less check
    for t in tmp_nums:
        if t<=num:
            is_less = False

    # more check
    for t in tmp_nums:
        if t>=num:
            is_more = False

    # check
    if is_less or is_more:
        count += 1

    # next step
    tmp_nums.append(num)

# output
print(count)
