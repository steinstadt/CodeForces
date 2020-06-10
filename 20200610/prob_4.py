# Problem 472 A - Design Tutorial: Learn from Math

# input
n = int(input())

# initialization
if n%2==0:
    ans_1 = 4
    ans_2 = n - 4
    print(ans_1, ans_2)
else:
    ans_1 = 9
    ans_2 = n - 9
    print(ans_1, ans_2)
    
