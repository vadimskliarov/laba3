#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Определить, есть ли среди трёх заданных чисел чётные.

if __name__ == '__main__':
    a = int(input("Введите число №1"))
    b = int(input("Введите число №2"))
    c = int(input("Введите число №3"))

    x1 = a % 2
    x2 = b % 2
    x3 = c % 2
    if x1 == 0 and x2 !=0 and x3 !=0:
         print("Среди трех чисел есть четные")
    elif x1 == 0 and x2==0 and x3 !=0:
        print("Среди трех чисел есть четные")
    elif x1 == 0 and x2 == 0 and x3==0:
        print("Среди трех чисел есть четные")
    elif x1 != 0 and x2 != 0 and x3==0:
        print("Среди трех чисел есть четные")    
    elif x1 != 0 and x2 == 0 and x3 ==0:
       print("Среди трех чисел есть четные")    
    elif x1 == 0 and x2 != 0 and x3 ==0:
        print("Среди трех чисел есть четные")   

