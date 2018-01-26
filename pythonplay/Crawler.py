'''
Create on 2017/12/26
@author: jiakaisheng
使用python爬取CSDN个人博客的访问量
'''


#当前的博客列表页号
import urllib.request
import urllib
import re

page_num = 1
# 不是最后列表的一页
notLast = 1
account = str(input('输入csdn的登录账号：'))
while notLast:
    #首页地址
    baseUrl = 'http://blog.csdn.net/'+account
    #连接页号，组成爬取的页面网址
    myUrl = baseUrl+'?ref=toolbar'
    #伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    #构造请求
    req = urllib.request.Request(url=baseUrl,headers=headers)
    #访问页面
    myResponse = urllib.request.urlopen(req)
    myPage = myResponse.read().decode()
    #在页面中查找是否存在‘尾页'这一个标签来判断是否为最后一页
    notLast = re.findall('<span>访问量：</span><span class="num">.*?</span>',myPage,re.S)
    print('---------------第%d页-------------' % (page_num,))
    #利用正则表达式来获取博客的标题
    title = re.findall('<a href="/u014639984/article/details/.*?" target="_blank">.*?</a>',myPage,re.S)
    titleList=[]
    for items in title:
        titleList.append(str(items).lstrip().rstrip())
    #利用正则表达式获取博客的访问量
    view = re.findall('<i class="icon iconfont icon-read"></i><span>.*?</span>',myPage,re.S)
    viewList=[]
    for items in view:
        viewList.append(str(items).lstrip().rstrip())
    #将结果输出
    for n in range(len(titleList)):
        print(('访问量:%s 标题:%s' % (viewList[n].zfill(4),titleList[n])))
    #页号加1
    page_num = page_num + 1