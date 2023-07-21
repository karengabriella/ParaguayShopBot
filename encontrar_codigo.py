import pandas as pd
from selenium import webdriver
import re

# Função para substituir espaços por "+"
def substituir_espacos_por_mais(texto):
    return '+'.join(texto.split())

# Função para extrair o número final depois do último underline
def extrair_numero_final_do_href(href):
    match = re.search(r'_(\d+)/$', href)
    return match.group(1) if match else None

# Configurar as opções do Chrome para negar notificações
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Inicializar o Chrome WebDriver com um tempo limite de 10 segundos
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)

# Lendo a planilha com Pandas
planilha = pd.read_excel('produtos_a_venda.xlsx')  

codigos_encontrados = []

# Iterar sobre os itens da planilha
for _, row in planilha.iterrows():
    nome_produto = row['nome_produto']
    
    # Transformar o nome do produto
    nome_produto_transformado = substituir_espacos_por_mais(nome_produto)
    
    # Montar o URL para o Selenium abrir
    url = f'https://www.comprasparaguai.com.br/busca/?q={nome_produto_transformado}'  
    
    # Abrir o site com Selenium
    driver.get(url)
    
    try:
        # Tentar localizar o elemento com xpath
        elemento = driver.find_element("xpath", '//a[@class="truncate"]')
        
        # Obter o atributo "href" do elemento
        href = elemento.get_attribute('href')
        
        # Extrair o número final depois do último underline do atributo "href"
        numero_final = extrair_numero_final_do_href(href)
        
        # Se o "Número final" for encontrado, adiciona à lista de códigos encontrados
        if numero_final:
            codigos_encontrados.append(numero_final)
        else:
            # Se o "Número final" não for encontrado, adiciona "CODIGO N ENCONTRADO" à lista de códigos encontrados
            codigos_encontrados.append('CODIGO N ENCONTRADO')
            
        # Imprimir os resultados
        print(f'Nome do produto: {nome_produto}')
        print(f'Nome transformado: {nome_produto_transformado}')
        print(f'Href: {href}')
        print(f'Número final: {numero_final}\n')
        
    except Exception as e:
        print(f'CODIGO N ENCONTRADO para o produto {nome_produto}')
        codigos_encontrados.append('SEM CODIGO')

# Atualizar a coluna "codigo" na mesma planilha original
planilha['codigo'] = codigos_encontrados

# Salvar a planilha atualizada
planilha.to_excel('produtos_a_venda.xlsx', index=False)  # Substitua 'encontrar_codigo.xlsx' pelo nome desejado para salvar a planilha atualizada

# Fechar o navegador
driver.quit()
