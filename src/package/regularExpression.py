'''
Created on 2015年9月5日

@author: Administrator
'''
import re
m = re.search('\d{2,6}','abcd4666esss444f')
print(type(m))
print(m.group())


import re
m1 = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
m2 = re.search("(?P<zimu>.\w{3})", "output_1981.10.21.txt") 
print(m1.group("year"))
print(m2.group("zimu"))


import os,re,datetime
filename="output_1981.10.21.txt"
print(filename)
get_time=re.search("(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})\.",filename)
year=get_time.group("year")
month=get_time.group("month")
day=get_time.group("day")
date=datetime.date(int(year),int(month),int(day))
wd=date.weekday()+1
filename=filename.replace(year+"."+month+"."+day, year+"-"+month+"-"+day+"-"+str(wd))
print(filename)
# os.rename(filename,"output_"+year+"-"+month+"-"+day+"-"+str(wd)+".txt")


import os, datetime, re
 
filename = "output_1981.10.21.txt"
get_time = re.search("\d{4}\.\d{2}\.\d{2}", filename)
date = datetime.date(*map((lambda str: int(str)), get_time.group(0).split('.')))
weekday = date.weekday() + 1
newFilename = "output_" + str(date) + "-" + str(weekday) + ".txt"
print(newFilename)
# os.rename(filename, newFilename)
