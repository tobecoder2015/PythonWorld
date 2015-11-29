import package.function
import package.fileOperate as B
import package.classMethod as A


def func(a,b,c):
    print (a,b,c)

dict = {'a':1,'b':2,'c':3}
func(**dict) # 得到value
func(*dict) # 得到key


a=package.function.isrunnian(2000);
print(a)



B.fileOperator.writetxt("pppppppppppppp")
B.fileOperator.output();
B.fileOperator.addText('OKOKOKOKO');
B.fileOperator.output();
A.TestMethod.selfMehhod_A('a')

b=B.fileOperator();
b.descript();