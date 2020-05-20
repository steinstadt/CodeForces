# Problem 1352 A - Sum of Round Numbers

# input
t = int(input())

# count loop
for i in range(t):
    n_list = list(input())
    n_keta = len(n_list)
    ans = []
    ans_num = 0
    for t in n_list:
        n = int(t)
        if not n==0:
            ans_num += 1
            ans.append(n*(10**(n_keta-1)))
        n_keta -= 1
    # output
    print(ans_num)
    print(" ".join(map(str, ans)))
