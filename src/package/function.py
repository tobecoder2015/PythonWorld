'''
Created on 2015年9月1日

@author: Administrator
'''
def isrunnian(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%4==0 or year%100==0:
        return True
    else:
        return False