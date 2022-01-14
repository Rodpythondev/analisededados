import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

dados = pd.read_csv('advertising.csv')
sns.heatmap(dados.corr(), cmap='Wistia', annot=True)
plt.show()

#treino

y = dados['Vendas']
x = dados[['TV', 'Radio', 'Jornal']]

#teste

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

modelo_regressaolienar = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

modelo_regressaolienar.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolienar.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

dados_au = pd.DataFrame()
dados_au['y_teste'] = y_teste
dados_au['previsao r linear'] = previsao_regressaolinear
dados_au['previsao arvore'] = previsao_arvoredecisao

sns.lineplot(data=dados_au)
plt.show()

novo = pd.read_csv('novos.csv')
print(novo)

previsao = modelo_arvoredecisao.predict(novo)
print(previsao)
novo['previsao'] = previsao
novo.to_csv('previsao.csv', index=False)