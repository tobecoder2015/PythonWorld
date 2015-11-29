'''
Created on 2015年9月1日

@author: Administrator
'''

class TestMethod():
    #classmethod
    @classmethod
    def selfMehhod_A(self,a):
        print(a+"selfMehhod_A")
  
    def selfMehhod_B(self,b):
        print(b+"selfMehhod_B")
  
    @staticmethod
    def staticMethod(c):
        print(c+"staticMethod")