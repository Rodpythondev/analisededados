import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
bit = pd.read_csv('BitCoin.csv')
print(bit)

sns.lmplot(data=bit, x='Global_Sales', y='Critic_Score', hue='notas', palette=cores )