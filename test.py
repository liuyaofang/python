# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

height = float(input('请输入您的身高:'))
weight = float(input('请输入您的体重:'))
bmi = weight / height**2
print(bmi)
if bmi < 18.5:
	print('童靴你太瘦了')
elif bmi >=18.5 and bmi < 25:
	print('童靴你身材很棒哦')
elif bmi >= 25 and bmi < 28:
	print('童靴你有点胖哦')
elif bmi >= 28 and bmi < 32:
	print('童靴你该减肥了')
else:
	print('童靴。。。')

#循环
l = ['Bart','Lisa','Adam']
for x in l:
	print('hello:',x)

a = len(l)
while a>0:
	print('hello:',l[a-1])
	a = a-1

#break跳出全部循环
n = 1
while n<=100:
	if n>10:
		break	
	print(n)
	n = n+1
print('END')

#continue跳出本次循环
s = 0
while s<10:
	s = s+1
	if s%2 == 0:
		continue
	print(s)

