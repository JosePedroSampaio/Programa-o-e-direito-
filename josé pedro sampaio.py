# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def soma (a, b):
    return a + b

def quadrado ( a ):
    return a**2

def hipotnusa( cateto1 , cateto2 ):
    return soma( quadrado ( cateto1 ), quadrado(cateto2)) ** (1/ 2)

print (soma(2,3))

