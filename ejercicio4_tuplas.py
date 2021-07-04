
#tuplas
#conjunto de datos,separados por coma, que no pueden ser modificados, las tuplas parten en la posicion 0

tupla1= (1234, "aeiou", 0.19, 'qwerty')

#nombre_tupla[posicion_elemento]
print (tupla1[0])#1234
print (tupla1[1])#"aeiou"
print (tupla1[2])#0.19
print (tupla1[3])#'qwerty'
#[1:3] significa que desde el 1 hasta el 3, sin considerar el 3
print (tupla1[1:3])#(aeiou", 0.19, 'qwerty')
print (tupla1 [:2])#(1234, "aeiou")
print (tupla1 [2:])#(0.19, 'qwerty')

#listas
#conjunto de datos, separados por comas, ordenados por su ingreso, todos parten en la posicion 0
lista= [1234, "aeiou", 0.19, 'qwerty', True] 
print (lista[2]) #0.19
print (lista[4]) #True

lista[0]= 4321 #reemplazando el valor de la posicion 0
#lista= [4321, "aeiou", 0.19, 'qwerty', True]
print (lista[0])
print (lista[-3]) #0.19, recorre de manera inversa
print (lista[-1]) #True
print (lista[1]) #"aeiou"

lista2 = lista[:] #copia de datos
print (lista) #se mantiene
print (lista2) # es copia de lista
lista2 [1] = '12345678'

print (lista) # [4321, "aeiou", 0.19, 'qwerty', True]
print (lista2) # [4321, '12345678' , 0.19, 'qwerty', True]

lista3= lista
lista3 [1]= '12345678' #[4321, '12345678', 0.19, 'qwerty', True]
print (lista)
print (lista3)