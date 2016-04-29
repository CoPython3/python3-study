
# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com
import pymysql
'''
# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
print(100+200)
'''
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('\r\'Hello, \"Bart\"\'')
print(r'''Hello,
Lisa!''')

print('{3},{1},{2},{0},{p1}'.format(n,f,s1,s2,p1=f))
print('%5s,%10d%20s'%('aa',22,s1))
print('%10s%10s%10s'%('name','age','sex')  )

print('%50d%%'%(len('25991')))

# -*- coding: utf-8 -*-

year1 = 72
year2 = 85
p_year=year2-year1
print('p_up:%d,%.2f%%'%(p_year,p_year/year1*100))