print(100+200);
print('hello','python');
print('100+200=',100+200);
# name=input();
# print('hello',name);

#注释
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
	print('kid')

# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

print('''line1
line2
line3''')

print(3>2)

n = 123
f = 456.789
s1 = 'hello,world'
s2 = 'hello,\'Adam\''
s3 = r'\'hello\',"bart"'
s4 = r'''hello,
lisa'''
print('n=',n,'\nf=',f,'\ns1=',s1,'\ns2=',s2,'\ns3=',s3,'\ns4=',s4)

#列表[] tuple()tuple一旦初始化就不能修改,但指向的list本身可变
classmates = ['lyf','李雷','韩梅梅']
print('classmates:',classmates)
print(len(classmates))	#长度
print(classmates[0])	
print(classmates[len(classmates)-1])
classmates.append('肉丝')	#追加
classmates.insert(1,'杰克')	#插入
# classmates.pop(1)	#删除
classmates[0] = '杰克'	#替换
print(classmates)

t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print('t=',t,t[0]) 
# t[0] = 'A'	TypeError: 'tuple' object does not support item assignment

#循环
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

sum = 0
n = 99
while n>0:
	sum = sum + n
	n = n-2
print(sum)

#dict
d = ['michael':95,'bob':75,'tracy':85]
d['michael']