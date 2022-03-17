# Importando com apelido "plt" pyplot torna semelhante ao plot do Matlab 
import matplotlib.pyplot as plt

#importando numpy
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# gerar relação x em função de y
plt.scatter(x,y)

#Plotar
plt.show()

# Array que começa em zero e termina em 100 pulando de 1 e 1
x1 = nparange(0,1000,1)


plt.plot(x1, x1**2)
plt.show()


#Importando um dataset

import pandas as pd

dados = pd.read_csv('Caminho do dataset')

dados.head()

#Gerar um novo dataset com informações que quero do original

dadosQueQuero = dados.loc[dados['Colunaque quero'] == 'StringDeFiltroIdentificador']

dadosQueQuero.head()
caracteristicas01 = dadosQueQuero['Coluna que quero']
caracteristicas02 = dadosQueQuero['Outra coluna que quero']

#Relacionando dados

plt.scatter(a,p)
plt.show



