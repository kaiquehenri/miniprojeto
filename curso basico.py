#Lógica de programação / programming logic
# 0 - entender o desafio que você quer resolver/understand the challenge you want to solve
# 1- percorrer todos os arquivos da pasta base de dados (vendas)/ go through all files in the database folder (sales)
# 2- importar da base de dados/ import from database
# 3- tratar/ compilar base de dados / treat/compile database
# 4- calcular o produto mais vendido (quantidade) / calculate best selling product (quantity)
# 5- calcular o produto que mais faturou (faturamento)/ calculate the product that generated the highest turnover (revenue)
# 6 - calcular a loja/cidade que mais vendeu (em faturamento)- cria um gráfico darshiboard/ Calculate the store/city with the highest sales revenue – create a dashboard chart.

import os 
import pandas as pd 
import plotly.express as px
# 1- percorrer todos os arquivos da pasta base de dados (vendas)/ go through all files in the database folder (sales)
lista_arquivo = os.listdir("C:/Users/Kaiqu/Documents/curso basico python/Vendas")

tabela_total = pd.DataFrame()

# 2- importar da base de dados/ import from database
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        tabela =pd.read_csv(f'C:/Users/Kaiqu/Documents/curso basico python/Vendas/{arquivo}')
        tabela_total = pd.concat([tabela_total, tabela])
# 3- tratar/ compilar base de dados / treat/compile database
print(tabela_total)
# 4- calcular o produto mais vendido (quantidade) / calculate best selling product (quantity)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida', 'Preco Unitario']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)
# 5- calcular o produto que mais faturou (faturamento)/ calculate the product that generated the highest turnover (revenue)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
print(tabela_faturamento )
# 6 - calcular a loja/cidade que mais vendeu (em faturamento)- cria um gráfico darshiboard/ Calculate the store/city with the highest sales revenue – create a dashboard chart.
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)
grafico = px.bar(tabela_lojas, x = tabela_lojas.index, y = 'Faturamento')
grafico.show()
