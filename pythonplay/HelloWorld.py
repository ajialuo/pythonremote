# 第一种：for循环判断
# def statistics(lst):
#     dic = {}
#     for k in lst:
#         if not k in dic:
#             dic[k] = 1
#         else:
#             dic[k]+=1
#     return dic
# lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
# print(statistics(lst))


# 比较取巧的，先把列表用set方式去重，然后用列表的count方法
# def statistics2(lst):
#     m = set(lst)
#     dic = {}
#     for x in m:
#         dic[x] = lst.count(x)
#     return dic
# lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
# print(statistics2(lst))

# 第三种：用reduce方式
from functools import reduce

def statistics3(dic,k):
    if not k in dic:
        dic[k] = 1
    else:
        dic[k]+=1
    return dic
lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
print (reduce(statistics3,lst,{}))
