Requests 的一些高级特性（Session,stream=True）
http://docs.python-requests.org/zh_CN/latest/user/advanced.html

 Python random模块sample、randint、shuffle、choice随机函数概念和应用(https://www.cnblogs.com/dylancao/p/8202888.html)

爬虫流处理：https://www.jianshu.com/p/0eff5fb281c0
r = requests.get('https://pvp.qq.com/web201605/js/herolist.json', stream=True)
with open("allhero.json", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
