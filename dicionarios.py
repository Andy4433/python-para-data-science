##########################################################################################################################################

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
# "key1": 1: A chave é uma string "key1" e seu valor correspondente é o inteiro 1.
# "key2": "2": A chave é uma string "key2" e seu valor correspondente é a string "2".
# "key3": [3, 3, 3]: A chave é uma string "key3" e seu valor correspondente é uma lista [3, 3, 3].
# A lista contém três elementos, todos eles sendo o inteiro 3.
# "key4": (4, 4, 4): A chave é uma string "key4" e seu valor correspondente é uma tupla (4, 4, 4). 
# A tupla contém três elementos, todos eles sendo o inteiro 4.
# ('key5'): 5: A chave é uma tupla ('key5',) e seu valor correspondente é o inteiro 5. 
# Observe que a chave é envolvida por parênteses para indicá-la como uma tupla. Nesse caso, a tupla contém um único elemento: a string "key5".
# (0, 1): 6: A chave é uma tupla (0, 1) e seu valor correspondente é o inteiro 6. Essa tupla contém dois elementos: 0 e 1.
# Portanto, o dicionário Dict possui várias chaves com diferentes tipos de dados como valores.

##########################################################################################################################################

# Acessar o valou do dicionaro.

Dict["key1"] # output: 1

Dict[(0, 1)] # output: 6


##########################################################################################################################################

# Criação do dicionário com as chaves sendo o nome dos álbuns e os valores sendo os anos de lançamento
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                     "Saturday Night Fever": "1977", "Rumours": "1977"}

# Acessa o valor associado à chave 'Thriller' no dicionário
release_year_dict['Thriller']
# Output: 1982

# Acessa o valor associado à chave 'The Bodyguard' no dicionário
release_year_dict['The Bodyguard']
# Output: 1992

# Retorna todas as chaves presentes no dicionário
release_year_dict.keys()
# Output: dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 
# 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours', 'Graduation'])

# Retorna todos os valores presentes no dicionário
release_year_dict.values()
# Output: dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977', '2007'])

# Adiciona uma nova entrada ao dicionário com a chave 'Graduation' e o valor '2007'
release_year_dict['Graduation'] = '2007'
# Output: {'Thriller': '1982','Back in Black': '1980','The Dark Side of the Moon': '1973','The Bodyguard': '1992',
# 'Bat Out of Hell': '1977','Their Greatest Hits (1971-1975)': '1976','Saturday Night Fever': '1977','Rumours': '1977','Graduation': '2007'}

# Remove as entradas do dicionário com as chaves 'Thriller' e 'Graduation'
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
# Output: {'Back in Black': '1980','The Dark Side of the Moon': '1973','The Bodyguard': '1992','Bat Out of Hell': '1977',
# 'Their Greatest Hits (1971-1975)': '1976','Saturday Night Fever': '1977','Rumours': '1977'}



# Verifica se a chave 'The Bodyguard' está presente no dicionário
'The Bodyguard' in release_year_dict
# Output: True

