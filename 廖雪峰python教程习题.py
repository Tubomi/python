#yield 知识点
def fib(max):
    n,a,b=0,0,1
    while n <max:
        yield b
        a,b=b,a+b
        n=n+1
        
for i in fib(6):
    print(i)

    
#map 练习
def normal(n):
    return n.capitalize()
list(map(tiger,['adam','LISA','barT']))#没明白为什么map需要加list才显示，reduce不用）

#reduce
from functools import reduce
def multip(x,y):
    return x*y
reduce(multip,[1,2,3,4,5])

#filter 清除素数
def Prime_number(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return True #这样写展示的是合数
list(filter(Prime_number,range(1,101)))
#二
def Prime_number(n):
    if n<=1:
        return False
    for i in range(2,n):
        return n%i==0 #这样写展示的是除2以外的偶数
list(filter(Prime_number,range(1,101)))
# 取素数
def Prime_number(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
list(filter(Prime_number,range(1,101)))

# 排序 升序降序复杂排序 见网址：http://www.cnblogs.com/whaben/p/6495702.html

#装饰器：https://www.cnblogs.com/Egbertbaron/p/7242515.html
______________________________________________
import functools
def  log(func):
    @functools.wraps(func)
    def  wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
——————————————————————————
@log
def now():
    print("123")
——————————————————————————
now.__name__


****************************************************
import functools
def  log(text):
    def  decorator(func):
        @functools.wraps(func)
        def  wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
———————————————————————————
@log('xad')#非常有意思的一个地方如果为@log 则now1.__name__返回的是decorator
def now1():
    print("123")
——————————————————————————
now1.__name__#log('xad')有text内容 则now1.__name__返回的是now1
