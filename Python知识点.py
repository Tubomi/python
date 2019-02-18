Requests 的一些高级特性（Session,stream=True）
http://docs.python-requests.org/zh_CN/latest/user/advanced.html
在selenium中设置代理ip：1.https://www.cnblogs.com/nail/p/6616417.html 2.https://blog.csdn.net/zwq912318834/article/details/78626739
计算程序运行时间的四种计算方法：https://blog.csdn.net/asialee_bird/article/details/79673860
 Python random模块sample、randint、shuffle、choice随机函数概念和应用(https://www.cnblogs.com/dylancao/p/8202888.html)
 
 词云：https://www.jianshu.com/p/ead991a08563 按照空格来分图

selenium+python设置爬虫代理IP：https://blog.csdn.net/zwq912318834/article/details/78626739

爬虫流处理：https://www.jianshu.com/p/0eff5fb281c0
r = requests.get('https://pvp.qq.com/web201605/js/herolist.json', stream=True)
with open("allhero.json", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
正则的用法：
https://www.cnblogs.com/deerchao/archive/2006/08/24/zhengzhe30fengzhongjiaocheng.html
