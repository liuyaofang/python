l = [];
n = 1;
while n <= 99:
	l.append(n);
	n = n+2;
print (l);

# 递归 切片
def trim(s):
    if len(s)==0:
        return s
    if s[0]==' ':
        return trim(s[1:])
    elif s[-1]==' ':
        return trim(s[-len(s):-1])
    else:
        return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')