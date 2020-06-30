# Problem 732 A - Buy a Shovel

# input
k, r = input().split()
k = int(k)

# initialization
count = 1
test = k

# count
while True:
    if str(test)[-1]==r or str(test)[-1]=='0':
        break
    test += k
    count += 1

# output
print(count)
