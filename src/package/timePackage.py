'''
Created on 2015年9月5日

@author: Administrator
'''
import time,datetime

print(time.localtime())
t=time.localtime;

print(time.time())
print(time.clock())

# print('start')
# time.sleep(10)     # sleep for 10 seconds
# print('wake up')


st = time.gmtime()      # 返回struct_time格式的UTC时间
for s in st:
    print(s)
    
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
for s in st:
    print(s)
print(str(st[0])+"年"+str(st[1])+"月"+str(st[2])+"日")


    
s  = time.mktime(st)    # 将struct_time格式转换成wall clock time
st = time.gmtime(s)   
for s in st:
    print(s)
    
st = time.clock   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print(st)


t = datetime.datetime(2012,9,3,21,30)
print(t)

t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)


from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt" 
str    = "output-1997-12-23-030000.txt" 
t      = datetime.strptime(str, format)
print(t)



