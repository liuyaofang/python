# name = input('please enter your name:')
# print('hello,',name)

# n1 = input('n1:')
# n2 = input('n2:')
# print('n1 * n2 =', int(n1)*int(n2))
# 
a = 100;
if a >= 0:
	print(a);
else:
	print(-a);

print('I\'m \n \"OK\"!');

print(3>2);

print('''n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\\\'world\\\''
s3 = r'Hello,"Bart"'
''')

classmates = ['michael','bob','tracy'];
print(classmates)
print(len(classmates));
print(classmates[-1])

height = 1.78
weight = 90
bmi = weight/(height*height)
print('%.2f'%bmi)
if bmi<18.5:
	print('过轻')
elif 18.5<=bmi<25:
	print('正常')
elif 25<=bmi<28:
	print('过重')
elif 28<=bmi<32:
	print('肥胖')
else:
	print('严重肥胖')

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
d = {'michael':95,'bob':75,'tracy':85}
print(d['michael'])