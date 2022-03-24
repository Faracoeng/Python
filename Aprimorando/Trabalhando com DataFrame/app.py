import pandas as pd

#Construtor
#DataFrame(data, index, columns, dtype, copy)

#Vazio
#pd.DataFrame()

#Para isso
df = pd.DataFrame(data=[5], index=['a'], columns=['col1'])
print(df)
#saida:
#	col1
#a	5

# Cada lista abaixo vai representar uma linha
# index deve ser proporcional ao numero de linhas
 dfList = pd.DataFrame(data=[[1, 2, 3], 
 			      [4, 5, 6], 
 			      [7, 8, 9]], index=['a', 'b', 'c'], columns=['col1', 'col2', 'col3'])
 print(dfList)
