# Problem 996 A - Hit the Lottery

# input
n = int(input())

# initialization
ans = 0
nokori = n

# count
ans += nokori // 100
nokori = nokori % 100

ans += nokori // 20
nokori = nokori % 20

ans += nokori // 10
nokori = nokori % 10

ans += nokori // 5
nokori = nokori % 5

ans += nokori

# outout
print(ans)
