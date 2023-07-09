import re

numbers = "0123456"
numbers[::2]
# para mostrar so numeros pares
###########################################################################################################################################
a = "Olá! Michael Jackson tem: 12 caracteres."  # Definindo uma variável de string 'a' com uma frase
print(a)  # Imprimindo a frase original

b = a.replace('!', '').replace(':', '').replace('.', '')  # Removendo o ponto de exclamação, dois-pontos e ponto da frase
print(b)  # Imprimindo a frase modificada

# Explicação:
# A string 'a' contém a frase "Olá! Michael Jackson tem: 12 caracteres."
# O método 'replace()' é usado para substituir caracteres específicos em uma string.
# Neste caso, encadeamos vários métodos 'replace()' para remover o ponto de exclamação, dois-pontos e ponto da string.
# A string modificada é atribuída à variável 'b'.
# Por fim, imprimimos tanto a frase original quanto a frase modificada para comparar os resultados.

##########################################################################################################################################

s1 = "Michael Jackson is the best"  # Definindo uma variável de string 's1' com uma frase

# Define o padrão a ser buscado
pattern = r"Jackson"

# Usa a função search() para buscar o padrão na string
result = re.search(pattern, s1)

# Verifica se houve uma correspondência encontrada
if result:
    print("Correspondência encontrada!")
else:
    print("Correspondência não encontrada.")

# Explicação:
# A string 's1' contém a frase "Michael Jackson is the best".
# A variável 'pattern' armazena o padrão de busca, que é a palavra "Jackson".
# Usando a função 're.search()', procuramos pelo padrão na string 's1'.
# Se uma correspondência for encontrada, ou seja, se a palavra "Jackson" estiver presente na string 's1',
# a condição 'if result:' será verdadeira e o código dentro do bloco 'if' será executado, imprimindo "Correspondência encontrada!".
# Caso contrário, se nenhuma correspondência for encontrada, a condição 'if result:' será falsa
# e o código dentro do bloco 'else' será executado, imprimindo "Correspondência não encontrada.".

##########################################################################################################################################

# Define o padrão de expressão regular a ser buscado
pattern = r"King of Pop"

# Define a string de substituição
replacement = "lenda"

# Usa a função sub para substituir o padrão pela string de substituição
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# A nova_string contém a string original com o padrão substituído pela string de substituição
print(new_string)

# Explicação:
# A variável 'pattern' armazena o padrão de expressão regular a ser buscado, que é "King of Pop".
# A variável 'replacement' armazena a string de substituição, que é "lenda".
# Usando a função 're.sub()', substituímos o padrão encontrado na string 's2' pela string de substituição.
# O parâmetro 'flags=re.IGNORECASE' indica que a busca deve ser feita sem diferenciação entre maiúsculas e minúsculas.
# A nova_string conterá a string original com o padrão substituído pela string de substituição.
# Por fim, imprimimos a nova_string para visualizar o resultado.

##########################################################################################################################################

pattern = r"\d\d\d\d\d\d\d\d\d"  # Corresponde a qualquer sequência de dez dígitos consecutivos
text = "Meu número de telefone é 1234577890"
match = re.search(pattern, text)

if match:
    print("Número de telefone encontrado:", match.group())
else:
    print("Sem correspondência")

# Explicação:
# A variável 'pattern' contém o padrão de expressão regular "\d\d\d\d\d\d\d\d\d", que corresponde a qualquer sequência de dez dígitos consecutivos.
# A variável 'text' contém a string em que a busca será realizada, que é "Meu número de telefone é 1234577890".
# Usando a função 're.search()', procuramos pelo padrão na string 'text'.
# Se for encontrada uma correspondência, o bloco 'if' será executado e imprime a mensagem "Número de telefone encontrado:" seguida do número de telefone encontrado utilizando 'match.group()'.
# Caso contrário, o bloco 'else' será executado e imprime a mensagem "Sem correspondência".
# Nesse caso, a correspondência será encontrada, pois a sequência "1234577890" corresponde ao padrão especificado.

##########################################################################################################################################
