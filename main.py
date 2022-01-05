import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

turbina = pd.read_csv('T1.csv')
turbina.columns = ['Data/hora', 'ActivePower(kw)', 'WindSpeed(m/s)', 'CurvaTeorica', 'Vento']
del turbina['Vento']
turbina['Data/hora'] = pd.to_datetime(turbina["Data/hora"])

sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kw)')

pot_real = turbina['ActivePower(kw)'].tolist()
pot_teorica = turbina['CurvaTeorica'].tolist()
pot_max = []
pot_min = []
dentro_limite = []
for potencia in pot_teorica:
    pot_max.append(potencia * 1.20)
    pot_min.append(potencia * 0.95)
for p, potencia in enumerate(pot_real):
    if pot_min[p] <= potencia <= pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')
turbina['DentroLimite'] = dentro_limite
cores = {'Dentro': 'Green', 'Fora': 'red', 'Zero': 'orange'}
sns.jointplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kw)', hue='DentroLimite', s=10, palette=cores)
plt.show()
