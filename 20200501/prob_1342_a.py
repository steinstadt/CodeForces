# Problem A - Road to Zero

# input
t = int(input())

# count
for i in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    tmp_count_1 = abs(x - y)
    tmp_count_2 = min(x, y)
    tmp_1 = tmp_count_1*a + tmp_count_2*b
    tmp_2 = (x + y)*a
    ans = min(tmp_1, tmp_2)
    print(ans)
