"""
生成器 - 生成器语法

Version: 0.1
Author: Damon
Date: 2018-03-21
"""

seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x)

num = 10

bbb = [x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1))]
print(bbb)

gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
    print(next(gen))
    n += 1
