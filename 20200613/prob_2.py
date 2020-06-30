# Problem 1154 A - Restoring Three Numbers

# input
num_list = list(map(int, input().split()))
num_list = sorted(num_list)

# initialization
ans_list = [0] * 3

# count
for i in range(3):
    ans_list[i] = num_list[-1] - num_list[i]

# output
print(" ".join(list(map(str, ans_list))))
