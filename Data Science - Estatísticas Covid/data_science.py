import pandas as pd

url = "http://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
df = pd.read_csv(url)

print(df.head())

cidade_mais_casos = df.loc[df['totalCases'].idxmax()]
print("Cidade com mais casos de Covid-19:", cidade_mais_casos['city'], "- Total de casos:", cidade_mais_casos['totalCases'])

cidade_menos_casos = df.loc[df['totalCases'].idxmin()]
print("Cidade com menos casos de Covid-19:", cidade_menos_casos['city'], "- Total de casos:", cidade_menos_casos['totalCases'])

estado_mais_casos = df.groupby('state')['totalCases'].sum().idxmax()
print("Estado com mais casos de Covid-19:", estado_mais_casos)

estado_menos_casos = df.groupby('state')['totalCases'].sum().idxmin()
print("Estado com menos casos de Covid-19:", estado_menos_casos)

cidade_mais_mortes = df.loc[df['deaths'].idxmax()]
print("Cidade com mais mortes por Covid-19:", cidade_mais_mortes['city'], "- Total de mortes:", cidade_mais_mortes['deaths'])

cidade_menos_mortes = df.loc[df['deaths'].idxmin()]
print("Cidade com menos mortes por Covid-19:", cidade_menos_mortes['city'], "- Total de mortes:", cidade_menos_mortes['deaths'])

estado_mais_mortes = df.groupby('state')['deaths'].sum().idxmax()
print("Estado com mais mortes por Covid-19:", estado_mais_mortes)

estado_menos_mortes = df.groupby('state')['deaths'].sum().idxmin()
print("Estado com menos mortes por Covid-19:", estado_menos_mortes)

total_casos_brasil = df['totalCases'].sum()
print("Total de casos de Covid-19 no Brasil:", total_casos_brasil)

total_mortes_brasil = df['deaths'].sum()
print("Total de mortes por Covid-19 no Brasil:", total_mortes_brasil)

import matplotlib.pyplot as plt
import seaborn as sns


mortes_por_estado = df.groupby('state')['deaths'].sum().sort_values(ascending=False).head(5)


plt.figure(figsize=(10,6))
sns.barplot(x=mortes_por_estado.index, y=mortes_por_estado.values)
plt.title('Top 5 Estados com Mais Mortes por Covid-19')
plt.xlabel('Estados')
plt.ylabel('Total de Mortes')
plt.show()


mortes_por_estado_menos = df.groupby('state')['deaths'].sum().sort_values(ascending=True).head(5)


plt.figure(figsize=(10,6))
sns.barplot(x=mortes_por_estado_menos.index, y=mortes_por_estado_menos.values)
plt.title('Top 5 Estados com Menos Mortes por Covid-19')
plt.xlabel('Estados')
plt.ylabel('Total de Mortes')
plt.show()


