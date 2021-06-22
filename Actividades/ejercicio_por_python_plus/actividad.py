import pandas as pd
from matplotlib import pyplot as plt

data_set = pd.read_csv('datos de prueba.csv', encoding="utf-8")

data_set = data_set[data_set['Nombre de evento' ] == 'fin']

nicks = data_set['Usuarie - nick'].value_counts()

plt.pie(nicks,labels=nicks.keys(),autopct="%0.1f %%")
plt.axis('equal')
plt.show()