import pandas as pd
from selenium import webdriver

web = webdriver.Chrome()

#pegar cotacao dolar
web.get('https://www.google.com')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotacao do dolar no brasil hoje')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
dollar = web.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
dollar = float(dollar)
print(f'{dollar:.2f}')

#pegar cotacao euro
web.get('https://www.google.com')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotacao do euro no brasil hoje')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
euro = web.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
euro = float(euro)
print(f'{euro:.2f}')
#pegar cotacao ouro
web.get('https://www.melhorcambio.com/ouro-hoje')
ouro = web.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(',', '.')
ouro = float(ouro)
print(ouro)
web.quit()
#atualizar minha base
dados = pd.read_excel('Produtos.xlsx')
dados.columns = ['produtos', 'preco_original', 'Moeda', 'cotacao', 'preco_compra', 'margem', 'preco_venda']
print(dados)

#calcular os precoes
dados.loc[dados['Moeda'] == 'Dólar', 'cotacao'] = dollar
dados.loc[dados['Moeda'] == 'Ouro', 'cotacao'] = ouro
dados.loc[dados['Moeda'] == 'Euro', 'cotacao'] = euro

dados['preco_compra'] = dados['preco_original'] * dados['cotacao']
dados['preco_venda'] = dados['preco_compra'] * dados['margem']
print(dados)
dados.to_csv('produtos.csv', index=False)