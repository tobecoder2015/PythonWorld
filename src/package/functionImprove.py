'''
Created on 2015年9月5日

@author: Administrator
'''

from _functools import reduce
#函数要在main函数之前

#其實和元組是重複的
# def func(a,b,c):
#     print (a,b,c)
#     
# def addfunc(a,b):
#     print (a+b)
#     
# def f(a,b,c=10):
#     print (a,b,c)
#     
# def func2(**dict):
#     print (type(dict))
#     print (dict)
# 
# def func(*para):
#     print (type(para))
#     print (para)
# 
# def fprint(str1,str2,times1=1,times2=1):
#     print (str1*times1)
#     print (str2*times2)
# 
#     
# 
#     
# args = (1,3,4)
# func(*args)
#     
# dic = {'tom':11,'sam':57,'lily':100}
# func2(**dic)
#    
# f(a=1,b=9)
# f(b=2,a=1,c=11)
# f(a=1,b=2,c=11)
#     
# func(1,2,3)
# func(3,2,1)
#     
# fprint("aa","bb")
# fprint("aa","bb",times1=4)
#     
# addfunc(1,1)
# addfunc(1,1.0)
# addfunc(1,1.00000000001)
# addfunc(10000000000000,1.000000001)
#     
#     
# re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
# print(re)
# for a in re:
#     print(a)
#     
#     
# re = map((lambda x: x+3),[1,2,3])
# print(type(re))
# for a in re:
#     print(a)
#     
#     
# re = map((lambda x,y,z: x+y-z),[1,2,3],[4,5,6],[7,8,9])
# print(type(re))
# for a in re:
#     print(a)   
# 
# 
# re=filter((lambda x:x>0),[-1,-2,5,0,9])
# print(type(re))
# print(help(re))
# for a in re:
#     print(a)   
# 
# 
# re=reduce((lambda x,y:x+y),{1,2,3,4,5,6})
# print(type(re))
# print(re)


# #finally的return 結果會覆蓋原來的返回值，需要注意
# def func(x):
#     try:
#         
#         x+=1
#         print ('aa')
#         return x
#     finally:
# #       x+=1
#         print ('bb')
#         return 'a'
#     
#     
# print (func(11))





  
def f(x):
#     x[0]=100
    x = [4,5,6]
 
a = [1,2,3]
print (a)
f(a)
print (a)


# def fff(x):
#     x = (4,5,6)
#     print (x)
# 
# a = (1,2,3)
# fff(a)
# print (a)

