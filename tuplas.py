##########################################################################################################################################

# Criando nossa tupla
tuple1 = ("disco",10,1.2 )
tuple1

##########################################################################################################################################

print(tuple1[0])  # Imprime o valor no índice 0 da tupla
print(tuple1[1])  # Imprime o valor no índice 1 da tupla
print(tuple1[2])  # Imprime o valor no índice 2 da tupla

##########################################################################################################################################

print(type(tuple1[0]))  # Imprime o tipo de dado do valor no índice 0 da tupla
print(type(tuple1[1]))  # Imprime o tipo de dado do valor no índice 1 da tupla
print(type(tuple1[2]))  # Imprime o tipo de dado do valor no índice 2 da tupla

##########################################################################################################################################

tuple1[-1]  # Obtém o valor do último elemento da tupla usando o índice negativo
tuple1[-2]  # Obtém o penultimo elemeto usado da tupla usando o indica negativo

##########################################################################################################################################

tuple2 = tuple1 + ("hard rock", 10)  # Concatena duas tuplas

##########################################################################################################################################

# Slice from index 0 to index 2
# Acessa os elementos do índice 0 até o índice 2 (exclusivo) da tupla
# Retorna uma nova tupla contendo os elementos ('disco', 10, 1.2)
tuple2[0:3]

##########################################################################################################################################

# Retorna o tamanho (número de elementos) da tupla
len(tuple2)

##########################################################################################################################################

# Uma nova tupla
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Ordena a lista Ratings em ordem crescente
RatingsSorted = sorted(Ratings)
RatingsSorted

##########################################################################################################################################

# Criar uma tupla aninhada
NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
NestedT

# Imprimir elementos em cada índice
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

##########################################################################################################################################

# Imprimir elementos em cada índice, incluindo índices aninhados
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

##########################################################################################################################################
