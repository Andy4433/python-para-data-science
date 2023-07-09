##########################################################################################################################################

# Criar uma nova lista
L = ["Michael Jackson", 10.1, 1982]
L

##########################################################################################################################################

# Imprimir o mesmo elemento usando indexação positiva e negativa

# Indexação positiva: L[0] retorna o primeiro elemento da lista
print('O mesmo elemento usando indexação positiva:', L[0])
# Indexação negativa: L[-3] retorna o terceiro elemento a partir do final da lista
print('O mesmo elemento usando indexação negativa:', L[-3])

# Indexação positiva: L[1] retorna o segundo elemento da lista
print('O mesmo elemento usando indexação positiva:', L[1])
# Indexação negativa: L[-2] retorna o segundo elemento a partir do final da lista
print('O mesmo elemento usando indexação negativa:', L[-2])

# Indexação positiva: L[2] retorna o terceiro elemento da lista
print('O mesmo elemento usando indexação positiva:', L[2])
# Indexação negativa: L[-1] retorna o último elemento da lista
print('O mesmo elemento usando indexação negativa:', L[-1])


##########################################################################################################################################

# A função extend() é usada para adicionar elementos a uma lista existente.

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

##########################################################################################################################################

# A função .append() é usada para adicionar elementos a uma lista existente. similar ao .extend()

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

##########################################################################################################################################

# Lista original
A = ["disco", 10, 1.2]

# Alterar elemento com base no índice
print('Before change:', A)  # Output: ["disco", 10, 1.2]
A[0] = 'hard rock'
print('After change:', A)  # Output: ['hard rock', 10, 1.2]

##########################################################################################################################################

# Lista original
A = ['hard rock', 10, 1.2]

# Remover elemento com base no índice
print('Before change:', A)  # Output: ['hard rock', 10, 1.2]
del(A[0])
print('After change:', A)  # Output: [10, 1.2]

##########################################################################################################################################

#O método split() é usado para dividir uma string em uma lista de substrings, usando um separador. 
#Se nenhum separador for especificado, o separador padrão é o espaço em branco.

'hard rock'.split() # output: ['hard', 'rock']

##########################################################################################################################################

# Dividir a string pelo separador ','
string = 'A,B,C,D'
lista = string.split(',') # output: ["A","B","C","D"]

##########################################################################################################################################

# Copiar a lista A por referência
A = ["hard rock", 10, 1.2]
B = A

# Imprimir as listas A e B
print('A:', A)
print('B:', B)
# output: A: ['hard rock', 10, 1.2]
# output: B: ['hard rock', 10, 1.2]

# Examinar a cópia por referência
print('B[0]:', B[0]) # output: B[0]: hard rock

# Modificar o primeiro elemento da lista A
A[0] = "banana"

# Imprimir o primeiro elemento da lista B
print('B[0]:', B[0]) # output: B[0]: banana

##########################################################################################################################################

# Clonar (clonar por valor) a lista A
B = A[:]
B # output: ['banana', 10, 1.2]

# Imprimir o valor de B[0]
print('B[0]:', B[0])

# Alterar o valor de A[0]
A[0] = "hard rock"

# Imprimir novamente o valor de B[0]
print('B[0]:', B[0]) # ouptput: ['hard rock', 10, 1.2]

