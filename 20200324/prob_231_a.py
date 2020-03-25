# Problem 231 A - Team

# input
N = int(input())
prob_list = []

# initialization
solution_count = 0

# count
for i in range(N):
    one_count = 0
    p = list(map(int, input().split()))
    for j in p:
        if j==1:
            one_count += 1
    if one_count>=2:
        solution_count += 1

# output
print(solution_count)
