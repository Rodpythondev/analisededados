import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

games = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')


plataforma = games['Year_of_Release'].tolist()
total_vendas = games['Global_Sales'].tolist()
score = games['Critic_Score'].tolist()
notas = []

for g, scor in enumerate(score):
    if score[g]>=80:
        notas.append('excelente')
    elif score[g]<=79 and score[g]>=60:
        notas.append('good')
    elif score[g]<60:
        notas.append('ruins')
    else:
        notas.append('None')

games['notas'] = notas
cores={'excelente': 'green', 'good': 'blue', 'ruins': 'orange', 'None': 'red' }
sns.lmplot(data=games, x='Global_Sales', y='Critic_Score', hue='notas', palette=cores )
plt.show()


