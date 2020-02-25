# 深入理解python @ classmethod
#
# 被 @ classmethod装饰的方法
# 1.
# 强制带个参数，cls，cls代表这个类本身
# 2.
# 不用实例化，和静态方法一样，直接
# 类().方法()
# 即可调用
# 3.
# cls是个位置参数，可随意换成其他词，如this
#
# 如想获取类属性x的值，可直接cls.x，等价于A.x


# class A():
#     x = 1
#
#     @classmethod
#     def B(cls):
#         print(cls.x)
#
# A.B()


# 1

# 已知cls代表类本身，那么cls(123), 就等价于A(123), 调用init初始化，实例化为x
# cls(123)
# 等价于
# x = A(123)


class A():

    def __init__(self, q):
        self.q = q

    @classmethod
    def B(cls):
        return cls(123)


x = A.B()
print(x.q)
# 123
# 运行逻辑：A() - B() - cls(123) - x = A(123)
