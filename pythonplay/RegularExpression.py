import re

# re模块中compile用于生成pattern的对象，再通过调用pattern实例的match方法处理文本最终获得match实例；通过使用match获得信息；
# pattern = re.compile(r'rlovep')
#
# m = pattern.match('rlovep.com')
# if m:
#     print(m.group())


# 在起始位置匹配
# print(re.match('www','www.runoob.com').span())
# 不在起始位置匹配
# print(re.match('com','www.runoob.com'))



# line = 'Cats are smartter than dogs'
# matchObj = re.match(r'(.*) are (.*?) .*', line,re.M|re.I)
# if matchObj:
#     print("matchObj.group(): ",matchObj.group())
#     print("matchObj.groups(): ",matchObj.groups())
#     print("matchObj.group(1): ",matchObj.group(1))
#     print("matchObj.group(2): ",matchObj.group(2))
# else:
#     print("No match")



# re.search 扫描整个字符串并返回第一个成功的匹配。
#   函数语法：
#   re.search(pattern, string, flags=0)
# print(re.search("relove","relove.com").span())
# print(re.search("com","relove.com").span())



# line = "This is my blog"
# 匹配含有is的字符串
# matchObj = re.search(r'(.*) is (.*?) .*', line, re.M|re.I)
# 使用了组输出：当group不带参数是将整个匹配成功的输出
# 当带参数为1时匹配的是最外层左边包括的第一个括号，一次类推；
# if matchObj:
#     print(("matchObj.group() : ", matchObj.group()))  # 匹配整个
#     print(("matchObj.group(1) : ", matchObj.group(1))) # 匹配的第一个括号
#     print(("matchObj.group(2) : ", matchObj.group(2))) # 匹配的第二个括号
# else:
#     print(("No match!!"))





# search和match区别
#   re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
#
# 实例
# line = "Cats are smarter than dogs";
# matchObj = re.match(r'dogs', line, re.M|re.I)
# if matchObj:
#     print(("match --> matchObj.group() : ", matchObj.group()))
# else:
#     print(("No match!!"))
# matchObj = re.search(r'dogs', line, re.M|re.I)
# if matchObj:
#     print(("search --> matchObj.group() : ", matchObj.group(0)))
# else:
#     print(("No match!!"))






# 检索和替换
#   Python 的re模块提供了re.sub用于替换字符串中的匹配项。
#   语法：
#   re.sub(pattern, repl, string, count=0)
#   参数：
#
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# phone = "2004-959-559 # 这是一个电话号码"
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print(("电话号码 : ", num))
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print(("电话号码 : ", num))




# 以下实例中将字符串中的匹配的数字乘于 2：
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))