# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lean_input
   Description :
   Author :       彭鸿儒
   date：          2018/7/23
-------------------------------------------------
   Change Activity:
                   2018/7/23:
-------------------------------------------------
"""
__author__ = '彭鸿儒'

a = int(input('a = '))
b = int(input('b = '))
print(f'{a:d} + {b:d} = {a + b:d}')
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
