# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

numeros = [1,2,3,4,5]
print('numeros[0]:', numeros[0])
print('numeros[-1]:', numeros[-1])
numeros[0] = 10 
print('numeros:', numeros) 

letras = ['a','b','c','d']
print('letras;',letras)
letras[2]=54
print('letras:',letras)

contador = 0
while contador < 10 :
    if contador !=9 :
         print(contador, end="-")
    else:
        print(contador,end='')
    contador += 1
print('\n======================================')

for i in range(10) :
    if i !=9 :
         print(i, end="-")
    else:
      print ( i, end=' ' )
print('\n======================================')

contador=0
lista = [1,45,78,'a',[ 3 , 5 ]] 
for item in lista:
     if contador != len(lista) - 1:     
      print ( item, end='-' )
     else: 
        print(item)
     contador +=1 
print('\n======================================')

for letra in ' minha string ' :
     print ( letra, end=' ' )
print('\n======================================')