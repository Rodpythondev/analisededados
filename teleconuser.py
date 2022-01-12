import pandas as pd
import plotly.express as px
dados = pd.read_csv('telecom_users.csv')
del dados['Unnamed: 0']
del dados['IDCliente']
dados['TotalGasto'] = pd.to_numeric(dados['TotalGasto'], errors='coerce')
dados = dados.dropna(how= 'all', axis=1)
dados = dados.dropna(how = 'any', axis=0)
print(dados['Churn'].value_counts())
print(dados['Churn'].value_counts(normalize=True).map('{:.2%}'.format))
for colunas in dados.columns:
    grafico = px.histogram(dados, x=colunas, color='Churn')
    grafico.show()




