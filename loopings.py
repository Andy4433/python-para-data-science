##########################################################################################################################################

# Use the range
range(3)  # Cria um objeto de intervalo que gera uma sequência de números de 0 a 3

# Explicação do uso do range:
# A função range cria um objeto de intervalo que representa uma sequência de números.
# Neste caso, range(3) gera uma sequência de números de 0 a 3 (excluindo o número 3).
# Podemos usar esse objeto de intervalo em iterações, como loops for, para percorrer os números da sequência.
# Por exemplo, 'for i in range(3):' irá iterar sobre os números 0,3.

##########################################################################################################################################

# Exemplo de loop for

dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])
    
# Loop for exemplo

dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])
    
# Explicação do loop for:
# O loop for é usado para executar um bloco de código várias vezes.
# Neste exemplo, temos uma lista chamada dates que contém anos.
# A variável N armazena o comprimento da lista (quantidade de elementos).
# Em seguida, usamos o loop for com a função range(N) para iterar sobre os índices da lista.
# Em cada iteração, o valor do índice é armazenado na variável i.
# Dentro do loop, usamos o índice i para acessar cada elemento da lista dates usando a sintaxe dates[i].
# Em cada iteração do loop, o ano correspondente é impresso.
# Neste exemplo, os anos 1982, 1980 e 1973 serão impressos em linhas separadas.

##########################################################################################################################################

# Neste exemplo, podemos imprimir uma sequência de números de 0 a 7:

# Exemplo de loop for
for i in range(0, 8):
    print(i)
# Resultado:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Em Python, podemos acessar diretamente os elementos em uma lista da seguinte forma:

# Exemplo de loop for, percorrendo uma lista
dates = [1982, 1980, 1973]
for year in dates:
    print(year)
# Resultado:
# 1982
# 1980
# 1973

# Explicação do uso do loop for:
# No primeiro exemplo, usamos a função range(0, 8) para gerar uma sequência de números de 0 a 7.
# O loop for itera sobre cada número gerado pela função range e o imprime.
# O resultado é a impressão de cada número de 0 a 7.

# No segundo exemplo, temos uma lista chamada dates com três elementos.
# O loop for itera sobre cada elemento da lista e o imprime.
# Em cada iteração, a variável year recebe o valor do elemento atual da lista.
# O resultado é a impressão de cada ano contido na lista dates.

##########################################################################################################################################

# Usando o loop for para alterar os elementos de uma lista

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Antes do quadrado ", i, 'é', squares[i])
    squares[i] = 'white'
    print("Depois do quadrado ", i, 'é', squares[i])
    
# Explicação do loop for:
# Neste exemplo, temos uma lista chamada squares que contém cores.
# Usamos o loop for com a função range(0, 5) para iterar sobre os índices de 0 a 4.
# Em cada iteração, o valor do índice é armazenado na variável i.
# Dentro do loop, usamos o índice i para acessar cada elemento da lista squares usando a sintaxe squares[i].
# Antes de alterar o elemento, imprimimos a cor original com uma mensagem usando a função print().
# Em seguida, atribuímos o valor 'white' ao elemento da lista usando a mesma sintaxe squares[i] = 'white'.
# Depois de alterar o elemento, imprimimos a nova cor com uma mensagem usando a função print().
# Neste exemplo, todas as cores da lista squares serão alteradas para 'white'.

##########################################################################################################################################

# Iterar pela lista e iterar sobre o índice e o valor do elemento

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
    
# Explicação do uso do enumerate():
# O enumerate() é uma função embutida do Python que retorna um objeto enumerado.
# No exemplo acima, usamos o enumerate() para iterar sobre a lista squares.
# A função enumerate() retorna uma sequência de tuplas, onde cada tupla contém um índice e o valor do elemento correspondente na lista.
# A variável i representa o índice do elemento e a variável square representa o valor do elemento em cada iteração.
# Ao usar o enumerate() em um loop for, podemos acessar tanto o índice quanto o valor do elemento simultaneamente.
# Neste exemplo, imprimimos o índice e o valor do elemento em cada iteração usando a função print().
# O resultado será a impressão do índice e o valor de cada elemento da lista squares.

##########################################################################################################################################

# Looping while:
count = 1
while count <= 5:
    print(count)
    count += 1
# o looping while so fuciona por meio de uma condicioal como mostrado no codigo acima
# tambem podemos fazer looping por meio do while True.
# Neste caso, o laço será executado indefinidamente até que o processo seja interrompido 
# por uma intervenção externa (CTRL + C) ou quando uma instrução break for encontrada (você saberá mais sobre a instrução break em instantes).

##########################################################################################################################################
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

##########################################################################################################################################

