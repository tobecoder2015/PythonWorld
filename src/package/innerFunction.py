'''
Created on 2015年9月6日

@author: Administrator
'''
# print((-1).__abs__())
# print((2.3).__int__())
# print(True.__or__(False))


class Sample(object):
    def __call__(self,a):
        return a+2;
    def __call2__(self,a,c):
        return a*c;

add=Sample();
print(type(add))
print(help(add))
print(add.__call__(1))
print(add.__call2__(2, 3))

print(add(2))
# a=map(add,[2,4,5])
# for b in a:
#     print(b)
    
dir(_enter_);