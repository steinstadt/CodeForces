# Problem 69 A - Young Physicist

# input
n = int(input())

# initialization
ans_vec = [0, 0, 0]

# vector calc
for i in range(n):
    x, y, z = map(int, input().split())
    ans_vec[0] += x
    ans_vec[1] += y
    ans_vec[2] += z

# output
if ans_vec[0]==0 and ans_vec[1]==0 and ans_vec[2]==0:
    print("YES")
else:
    print("NO")
