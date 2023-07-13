##########################################################################################################################################
def add(a):
  # Adiciona 1 a 'a'
  # Armazena a soma de 'a' + 1 em 'b'
  b = a + 1
  # Imprime o valor de 'a' e o valor de 'b' após a adição
  print(a, "se você adicionar um", b)
  # Retorna o valor de 'b'
  return b
  
# Uma função é um bloco de código reutilizável que executa operações especificadas na função. 
# Eles permitem que você divida as tarefas e reutilize seu código em diferentes programas.
# Existem dois tipos de funções:
# Funções pré-definidas
# Funções definidas pelo usuário

# What is a Function?
# Você pode definir funções para fornecer a funcionalidade necessária. Aqui estão regras simples para definir uma função em Python:

# * Os blocos de funções começam com def seguido pela função name e parênteses ()
# * Existem parâmetros de entrada ou argumentos que devem ser colocados entre esses parênteses.
# * Você também pode definir parâmetros dentro desses parênteses.
# * Existe um corpo dentro de cada função que começa com dois pontos : e é recuado.
# * Você também pode colocar a documentação antes do corpo.
# * A instrução return encerra uma função, opcionalmente retornando um valor.

# Um exemplo de função que adiciona ao parâmetro a imprime e retorna a saída como b:

# Obtenha ajuda sobre a função de adição

help(add)

# output: Help on function add in module __main__:
# add(a)
#    add 1 to a


# Chame a função add()

add(1)
# output: 1 if you add one 2
# 2

##########################################################################################################################################

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)
# output: 24

Mult(2, 3)
# output: 6


Mult(10.0, 3.14)
# output: 31.400000000000002

Mult(2, "Michael Jackson ")
# output: 'Michael Jackson Michael Jackson '

##########################################################################################################################################

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Inicializa a variável global
x = 3
# Faz a chamada da função e atribui o retorno à variável y
y = square(x)
y

# output: 3 if you square + 1 10
# 10


# Informa um número diretamente como parâmetro

# Chama a função square() com o argumento 2
square(2)

# output: 2 if you square + 1 5
# 5

##########################################################################################################################################

# Define a função MJ, que não possui valor de retorno
def MJ():
    print('Michael Jackson')

# Define a função MJ1, que possui valor de retorno None
def MJ1():
    print('Michael Jackson')
    return None

MJ()
# output: Michael Jackson
MJ1()
# output: Michael Jackson
print(MJ())
print(MJ1())
# output: Michael Jackson
# None
# Michael Jackson
# None

##########################################################################################################################################

def con(a, b):
    return(a + b)

con("This ", "is")  # Chama a função 'con' com os argumentos "This " e "is"

# output: This is

##########################################################################################################################################

def freq(string):
    # Passo 1: Declaração e inicialização de uma lista vazia
    words = []
    
    # Passo 2: Dividir a string em uma lista de palavras
    words = string.split()  # ou string.lower().split()
    
    # Passo 3: Declaração de um dicionário vazio
    Dict = {}
    
    # Passo 4: Iterar pelas palavras e contar a frequência
    for key in words:
        Dict[key] = words.count(key)
        
    # Passo 5: Imprimir o dicionário contendo a frequência das palavras
    print("A frequência das palavras é:", Dict)

# Passo 6: Chamada da função e passagem da string como argumento
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# output: The Frequency of words is: {'Mary': 6, 'had': 2, 'a': 2, 'little': 3, 'lamb': 3, 'Little': 1, 'lamb,': 1, 'lamb.Its': 1, 'fleece': 1, 'was': 2, 
#'white': 1, 'as': 1, 'snow': 1, 'And': 1, 'everywhere': 1, 'that': 2, 'went': 3, 'went,': 1, 'Everywhere': 1, 'The': 1, 'sure': 1, 'to': 1, 'go': 1}

##########################################################################################################################################

myFavouriteBand = "AC/DC"  # Variável global 'myFavouriteBand' é definida como "AC/DC".

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"  # Variável local 'myFavouriteBand' é definida como "Deep Purple".
    if bandname == myFavouriteBand:

      return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))  # Chama a função getBandRating com o argumento "AC/DC". Retorna 0.0, pois a condição é falsa.
print("Deep Purple's rating is:", getBandRating("Deep Purple"))  # Chama a função getBandRating com o argumento "Deep Purple". Retorna 10.0, pois a condição é verdadeira.
print("My favourite band is:", myFavouriteBand)  # Imprime o valor da variável global 'myFavouriteBand', que é "AC/DC".

# output: AC/DC's rating is: 0.0
# Deep Purple's rating is:  10.0
# My favourite band is: AC/DC 

##########################################################################################################################################

myFavouriteBand = "AC/DC"  # A variável global 'myFavouriteBand' é definida como "AC/DC".

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))  # Chama a função getBandRating com o argumento "AC/DC". Retorna 10.0, pois a condição é verdadeira.
print("Deep Purple's rating is:", getBandRating("Deep Purple"))  # Chama a função getBandRating com o argumento "Deep Purple". Retorna 0.0, pois a condição é falsa.
print("My favourite band is:", myFavouriteBand)  # Imprime o valor da variável global 'myFavouriteBand', que é "AC/DC".

# output: AC/DC's rating is: 10.0
# Deep Purple's rating is: 0.0
# My favourite band is: AC/DC

##########################################################################################################################################

def printAll(*args):  # O asterisco (*) indica que todos os argumentos serão empacotados em uma tupla chamada args
    print("Número de argumentos:", len(args))  # Imprime o número de argumentos passados
    for argument in args:  # Itera sobre cada argumento na tupla args
        print(argument)  # Imprime cada argumento

printAll('Horsefeather', 'Adonis', 'Bone')  # Chama a função printAll com 3 argumentos. Imprime o número de argumentos (3) e os argumentos individualmente.
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage')  # Chama a função printAll com 4 argumentos. Imprime o número de argumentos (4) e os argumentos individualmente.

# output: No of arguments: 3
# Horsefeather
# Adonis
# Bone
# No of arguments: 4
# Sidecar
# Long Island
# Mudslide
# Carriage

##########################################################################################################################################

def printAll(*args):  # O asterisco (*) indica que todos os argumentos serão empacotados em uma tupla chamada args
    print("Número de argumentos:", len(args))  # Imprime o número de argumentos passados
    for argument in args:  # Itera sobre cada argumento na tupla args
        print(argument)  # Imprime cada argumento

printAll('Horsefeather', 'Adonis', 'Bone')  # Chama a função printAll com 3 argumentos. Imprime o número de argumentos (3) e os argumentos individualmente.
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage')  # Chama a função printAll com 4 argumentos. Imprime o número de argumentos (4) e os argumentos individualmente.

# output: Country : Canada
# Province : Ontario
# City : Toronto

