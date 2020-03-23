# Problem 1 A - Theatre Square

import math

# input
n, m, a = map(int, input().split())

n_count = math.ceil(n / a)
m_count = math.ceil(m / a)

# output
print(n_count * m_count)
