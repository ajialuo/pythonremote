#  高阶函数

# 函数式编程
#
#   Python特点：
#
# 不是纯函数式编程（允许变量存在）；
# 支持高阶函数（可以传入函数作为变量）；
# 支持闭包（可以返回函数）；
# 有限度的支持匿名函数；
#   高阶函数：
#
# 变量可以指向函数；
# 函数的参数可以接收变量；
# 一个函数可以接收另一个函数作为参数；


# 内置高阶函数map()
#
#   map函数有两个参数，一个是函数，另一个是列表，返回值为对传入的列表中每一个元素执行传入的函数操作之后得到的列表；
# def format_name(s):
#     return s.title()
# print(list(map(format_name,['bob','tom','jack'])))


# 内置高阶函数reduce()
#
#   reduce函数也有两个参数，一个是函数，另一个是列表，返回值为对list的每一个元素反复调用函数f，得到最终结果，以下函数为连乘；
# from functools import reduce
# def prod(x,y):
#     return x*y
# print(reduce(prod,[2,4,5,7]))



# 内置高阶函数filter()
#
#   filter函数接受函数参数f和列表参数lst，f对lst元素进行判断，返回lst元素中调用f函数结果为true的元素组成的列表（将不满足f函数条件的元素过滤掉）
# import math
# def is_sqr(x):
#     return int(math.sqrt(x))*int(math.sqrt(x))==x
# print(list(filter(is_sqr, range(1,101))))



# 自定义排序函数sorted()
#
#   sorted函数接受一个列表lst和一个函数参数f，f为自定义的比较lst元素大小的函数，返回值为lst中元素按f函数排列的列表；
from filecmp import cmp

def cmp_ignore_case(s1,s2):
    return cmp(s1.lower(),s2.lower())
print(sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case))

