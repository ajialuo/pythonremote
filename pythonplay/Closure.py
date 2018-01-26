# 在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问
# def g():
#     print ('g()')
# def f():
#     print ('f()')
#     return g


# 将 g 的定义移入函数 f 内部，防止其他代码调用 g：
# def f():
#     print ('f()...')
#     def g():
#         print ('g()...')
#     return g

# 考察定义的 calc_sum 函数：
# def calc_sum(lst):
#     def lazy_sum():
#         return sum(lst)
#     return lazy_sum
# 注意: 发现没法把 lazy_sum 移到 calc_sum 的外部，因为它引用了 calc_sum 的参数 lst。
#
# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。


# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：
# 希望一次返回3个函数，分别计算1*1,2*2,3*3
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print(f1(),f2(),f3())
# 原因就是当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3

def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())


