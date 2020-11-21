# Problem 1367 A - Short Substrings

# input
t = int(input())

# string check
for i in range(t):
    b = input()
    b_len = len(b)
    ans = [b[0]]

    if b_len>2:
        i = 1
        while i<b_len:
            ans.append(b[i])
            i += 2
        print("".join(ans))
    else:
        print(b)
