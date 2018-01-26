# s = ' abc@ jk ,sd,'
# s1 = s.strip().lstrip().rstrip(',')
# print(s1)


# s1 = 'study'
# s2 = s1
# s1 = 'story'
# print(s2)


# 连接字符串
# sStr1 = 'strcat'
# sStr2 = 'append'
# sStr1 += sStr2
# print(sStr1)


# 查找字符
#strchr(sStr1,sStr2)
# < 0 为未找到
# sStr1 = 'strchr'
# sStr2 = 's'
# nPos = sStr1.index(sStr2)
# print(nPos)


# 比较字符串
# python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块。
# from operator import lt, le, eq, ne, gt, ge
#
# sStr1 = 'strchr'
# sStr2 = 'strch'
# print(lt(sStr1,sStr2))
# print(le(sStr1,sStr2))
# print(eq(sStr1,sStr2))
# print(ne(sStr1,sStr2))
# print(gt(sStr1,sStr2))
# print(ge(sStr1,sStr2))




# 扫描字符串是否包含指定的字符
# sStr1 = '12345678'
# sStr2 = '456'
# print(len(sStr1 and sStr2))
# print(len(sStr1 or sStr2))
# print(len(sStr1))
# print(len(sStr2))
# 结果
# 3
# 8
# 8
# 3


# 将字符串中的大小写转换
# sStr1 = 'JCstrlwr'
# sStr1 = sStr1.upper()
# #sStr1 = sStr1.lower()
# print(sStr1)


# 复制指定长度的字符
# sStr1 = ''
# sStr2 = '12345'
# n = 3
# sStr1 = sStr2[0:n]
# print(sStr1)



# 将字符串前n个字符替换为指定的字符
# sStr1 = '12345'
# ch = 'r'
# n = 3
# sStr1 = n * ch + sStr1[3:]
# print(sStr1)


# 扫描字符串
# sStr1 = 'cekjgdklab'
# sStr2 = 'gka'
# nPos = -1
# for c in sStr1:
#     if c in sStr2:
#         nPos = sStr1.index(c)
#         break
# print(nPos)



# 翻转字符串
# sStr1 = 'abcdefg'
# sStr1 = sStr1[::-1]
# print(sStr1)



# 查找字符串
# sStr1 = 'abcdefg'
# sStr2 = 'cde'
# print(sStr1.find(sStr2))


# 分割字符串
# sStr1 = 'ab,cde,fgh,ijk'
# sStr2 = ','
# sStr1 = sStr1[sStr1.find(sStr2) + 1:]
# print(sStr1)
# #或者
# s = 'ab,cde,fgh,ijk'
# print(s.split(','))


# 连接字符串
# delimiter = ','
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))

# 截取字符串
str = '0123456789'
print(str[0:3]) #截取第一位到第三位的字符
print(str[:]) #截取字符串的全部字符
print(str[6:]) #截取第七个字符到结尾
print(str[:-3]) #截取从头开始到倒数第三个字符之前
print(str[2]) #截取第三个字符
print(str[-1]) #截取倒数第一个字符
print(str[::-1]) #创造一个与原字符串顺序相反的字符串
print(str[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
print(str[-3:]) #截取倒数第三位到结尾
print(str[:-5:-3]) #逆序截取，具体啥意思没搞明白？