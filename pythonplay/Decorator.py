from functools import reduce

# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
#   使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。
#   考察一个@log的定义：
# def log(f):
#     def fn(x):
#         print('call ' + f.__name__ + '()...')
#         return f(x)
#     return fn
#
# @log
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1,n+1))
# print(factorial(10))
# 要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：


# 请编写一个@performance，它可以打印出函数调用的时间。
#   计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
#   参考代码:
# import time
#
# def performance(f):
#     def fn(*args, **kw):
#         t1 = time.time()
#         r = f(*args, **kw)
#         t2 = time.time()
#         print('call %s() in %fs' % (f.__name__, (t2-t1)))
#         return r
#     return fn
#
# @performance
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1,n+1))
# print(factorial(10))


# 带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：
# def log(prefix):
#     def log_decorator(f):
#         def wrapper(*args, **kw):
#             print('[%s] %s()...' % (prefix, f.__name__))
#             return f(*args, **kw)
#         return wrapper
#     return log_decorator
#
# @log('DEBUG')
# def test():
#     pass
# print(test())


# 在@performance实现打印秒的同时，请给 @performace 增加一个参数，允许传入’s’或’ms’：
import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))