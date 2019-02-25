机器学习算法的随机数据生成:https://www.cnblogs.com/pinard/p/6047802.html
pandas:http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cat.html
Requests 的一些高级特性（Session,stream=True）
正则：[^...] 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
http://docs.python-requests.org/zh_CN/latest/user/advanced.html
在selenium中设置代理ip：1.https://www.cnblogs.com/nail/p/6616417.html
selenium+python设置爬虫代理IP：https://blog.csdn.net/zwq912318834/article/details/78626739
https://blog.csdn.net/weixin_36279318/article/details/79475388
Selenium
官网 http://www.seleniumhq.org/
GitHub https://github.com/SeleniumHQ/selenium
文档 http://selenium-python.readthedocs.io/
中文文档：https://selenium-python-zh.readthedocs.io/en/latest/index.html
one-hot:
    https://blog.csdn.net/dongyanwen6036/article/details/78555163
拉勾获取页面例子：https://www.jianshu.com/p/61dfbc3cd683
计算程序运行时间的四种计算方法：https://blog.csdn.net/asialee_bird/article/details/79673860
Python random模块sample、randint、shuffle、choice随机函数概念和应用(https://www.cnblogs.com/dylancao/p/8202888.html)
词云和jieba:https://blog.csdn.net/fontthrone/article/details/72782971


爬虫流处理：https://www.jianshu.com/p/0eff5fb281c0
r = requests.get('https://pvp.qq.com/web201605/js/herolist.json', stream=True)
with open("allhero.json", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
正则的用法：
https://www.cnblogs.com/deerchao/archive/2006/08/24/zhengzhe30fengzhongjiaocheng.html
