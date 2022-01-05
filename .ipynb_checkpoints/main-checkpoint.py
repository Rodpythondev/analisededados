import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
     #ler o arquivo
sol = pd.read_csv('AnnualTicketSales.csv')
sol.columns = ['Ano', 'Vendidos', 'TotalBox', 'Inflacao', 'Preco', 'vazio' ]
del sol['vazio']
#print(sol)
     
     #plote os dados graficos
sns.scatterplot(data=sol, x='Ano', y='Vendidos')
     
