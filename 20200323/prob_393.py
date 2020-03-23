# Problem 393 A - Nineteen

# input
S = input()

# initialization
max_count = 0
letter_dic = {'n':0, 'i':0, 'e':0, 't':0}

# search
for s in S:
    if s in letter_dic:
        letter_dic[s] += 1
n_count = (letter_dic['n']-1)//2
i_count = (letter_dic['i'])
e_count = (letter_dic['e'])//3
t_count = (letter_dic['t'])

# output
ans_num = min(n_count, i_count, e_count, t_count)
if ans_num<0:
    ans_num = 0
print("%d"%(ans_num))
