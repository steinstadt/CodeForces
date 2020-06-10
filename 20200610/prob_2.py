# Problem 510 A - Fox And Snake

# input
n, m = map(int, input().split())

# initialization
switch = 0

# drawing
for i in range(n):
    if i%2==0:
        print("#"*m)
    else:
        if switch==0:
            print("."*(m-1) + "#")
            switch = 1
        else:
            print("#" + "."*(m-1))
            switch = 0
