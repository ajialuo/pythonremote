# 众所周知，def cmp 作为方法存在，用sort对实例进行排序时，会用到class 中的cmp。但是，在python3中，取消了 sorted对cmp的支持。
#   python3 中有关排序的sorted方法如下：
# students = [('join','A',20),('bob','A',15),('tom','A',12)]
# print(sorted(students,key=lambda x: x[2]))
# print([x for x in students])


#  这是一个字符串排序，排序规则：小写<大写<奇数<偶数
# s = ‘asdf234GDSdsf23’ #排序:小写-大写-奇数-偶数
s = 'asdf234GDSdsf23'
print(''.join(sorted(s,key=lambda x: (x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x))))
# 原理：先比较元组的第一个值，如果相等就比较元组的下一个值，以此类推。
#   先看一下Boolean value 的排序：
#   print(sorted([True,Flase]))===>结果[False,True]
#   Boolean 的排序会将 False 排在前，True排在后 .
#
# 1.x.isdigit()的作用是把数字放在前边,字母放在后边.
# 2.x.isdigit() and int(x) % 2 == 0的作用是保证奇数在前，偶数在后。
# 3.x.isupper()的作用是在前面基础上,保证字母小写在前大写在后.
# 4.最后的x表示在前面基础上,对所有类别数字或字母排序。
#   最后结果：addffssDGS33224




# 一道面试题
# list1=[7, -8, 5, 4, 0, -2, -5]
# 要求1.正数在前负数在后 2.正数从小到大 3.负数从大到小
list1 = [7,-8,5,4,0,-2,-5]
print(sorted(list1,key=lambda x: (x<0,abs(x))))
