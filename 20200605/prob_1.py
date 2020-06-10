# Problem 61 A - Ultra-Fast Mathematician

# input
n_1 = list(input())
n_2 = list(input())

# initialization
n_r = ['']*(len(n_1))

# clac
for i in range(len(n_1)):
    n_1_tmp = int(n_1[i])
    n_2_tmp = int(n_2[i])
    n_r_tmp = (n_1_tmp + n_2_tmp)&1
    n_r[i] = str(n_r_tmp)

# output
print("".join(n_r))
