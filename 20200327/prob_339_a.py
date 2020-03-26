# Problem 339 A - Helpful Maths

# input
summands_list = list(map(int, input().split("+")))

# sort
summands_list = sorted(summands_list)
summands_list = list(map(str, summands_list))
print("+".join(summands_list))
