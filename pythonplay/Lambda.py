# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
# values = map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])
# for item in values:
#     print(item, end=' ')

# 返回函数的时候，也可以返回匿名函数：
# myabs = lambda x: -x if x < 0 else x
# print(myabs(-2))


items = filter(lambda s: s and len(s.strip())>0,['test',None,'','str',' ','END'])
for item in items:
    print(item, end=' ')
