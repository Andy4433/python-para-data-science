##########################################################################################################################################

# Criar conjuntos
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1
# Output: {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}
##########################################################################################################################################

# Criar uma lista
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]

# Converter a lista em um conjunto
album_set = set(album_list)

# Imprimir o conjunto
album_set
# Output: {'00:42:19',10.0,1982,'30-Nov-82',46.0,65,'Michael Jackson',None,'Pop, Rock, R&B','Thriller'}

# Criar uma lista de gêneros musicais
music_genres = ["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"]

# Converter a lista em um conjunto
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"])


# Um conjunto não permite elementos duplicados, então apenas as ocorrências únicas dos gêneros serão mantidas
music_genres
#output: {'R&B', 'disco','folk rock','hard rock','pop','progressive rock','rock','soft rock','soul'}

##########################################################################################################################################

# Criar um conjunto de exemplo
A = set(["Thriller", "Back in Black", "AC/DC"])
A

# Adicionar um elemento ao conjunto
A.add("NSYNC")
A

# Tentar adicionar um elemento duplicado ao conjunto
## Como conjuntos não permitem elementos duplicados, o elemento duplicado não será adicionado
A.add("NSYNC")
A

# Remover o elemento do conjunto
A.remove("NSYNC")
A

# Verificar se o elemento está presente no conjunto
"AC/DC" in A

##########################################################################################################################################

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Imprimir dois conjuntos
album_set1
album_set2

# Encontrar a interseção dos conjuntos
intersection = album_set1 & album_set2
intersection
# output: {'AC/DC', 'Back in Black'}

# Encontrar a diferença entre set1 e set2 (elementos presentes em set1, mas não em set2)
album_set1.difference(album_set2) 
#output: {'Thriller'}

# Encontrar a diferença entre set2 e set1 (elementos presentes em set2, mas não em set1)
album_set2.difference(album_set1)
#output: {'The Dark Side of the Moon'}

# Usar o método intersection para encontrar a interseção entre album_set1 e album_set2
album_set1.intersection(album_set2) 
#output:{'AC/DC', 'Back in Black'}

# Encontrar a união de dois conjuntos
album_set1.union(album_set2) 
#output: {'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'}

# Verificar se album_set1 é um superset de album_set2
set(album_set1).issuperset(album_set2)
#output: False

# Verificar se album_set2 é um subset de album_set1
set(album_set2).issubset(album_set1)
#output: False

# Verificar se {"Back in Black", "AC/DC"} é um subset de album_set1
set({"Back in Black", "AC/DC"}).issubset(album_set1)
#output: True

# Verificar se album_set1 é um superset de {"Back in Black", "AC/DC"}
album_set1.issuperset({"Back in Black", "AC/DC"})
#output: True

##########################################################################################################################################

