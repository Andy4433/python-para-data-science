import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de gráficos
%matplotlib inline  
# Permite exibir os gráficos inline no notebook

class Circle(object):  # Define a classe Circle
    def __init__(self, radius=3, color='blue'):  # Define o construtor da classe com os atributos radius e color
        self.radius = radius  # Atribui o valor do parâmetro radius ao atributo radius do objeto
        self.color = color  # Atribui o valor do parâmetro color ao atributo color do objeto
    
    def add_radius(self, r):  # Define o método add_radius para adicionar um valor ao raio do círculo
        self.radius = self.radius + r  # Incrementa o raio atual com o valor passado como parâmetro
        return self.radius  # Retorna o novo valor do raio
    
    def drawCircle(self):  # Define o método drawCircle para desenhar o círculo
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))  # Adiciona um círculo ao gráfico
        plt.axis('scaled')  # Define a escala do eixo para ser igual em ambos os eixos
        plt.show()  # Exibe o gráfico

RedCircle = Circle(10, 'red')  # Cria um objeto Circle chamado RedCircle com raio 10 e cor vermelha

dir(RedCircle)  # Retorna a lista de métodos e atributos disponíveis para o objeto RedCircle

RedCircle.radius  # Imprime o valor do atributo radius do objeto RedCircle

RedCircle.color  # Imprime o valor do atributo color do objeto RedCircle

RedCircle.radius = 1  # Modifica o valor do atributo radius do objeto RedCircle para 1

RedCircle.radius  # Imprime o novo valor do atributo radius do objeto RedCircle

RedCircle.drawCircle()  # Chama o método drawCircle do objeto RedCircle para desenhar o círculo
