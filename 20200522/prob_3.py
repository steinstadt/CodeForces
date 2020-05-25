# Problem 122 A - Lucky Division

# input
n = int(input())

def dfs(s):
    # stop condition
    if len(s)==4:
        return False
    if not len(s)==0:
        num = int(s)
        if n%num==0:
            return True

    # next process
    t_1 = s + '4'
    t_2 = s + '7'
    result = dfs(t_1) or dfs(t_2)

    return result

# check
ans = dfs('')

# output
if ans:
    print("YES")
else:
    print("NO")
