import pandas as pd
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Função para substituir espaços por "+"
def substituir_espacos_por_mais(texto):
    return '+'.join(texto.split())

# Função para extrair o número final depois do último underline
def extrair_numero_final_do_href(href):
    match = re.search(r'_(\d+)/$', href)
    return match.group(1) if match else None

def buscar_item_no_site(driver, codigo):
    url = f"https://www.comprasparaguai.com.br/busca/?q={codigo}"
    driver.get(url)
    time.sleep(3)

    try:
        elemento = driver.find_element("xpath", '//a[@class="truncate"]')
        texto_item = elemento.text.strip()

        try:
            elemento_preco = driver.find_element("xpath", '//div[@class="price-model"]/span')
            texto_preco = elemento_preco.text.strip()
        except Exception as e:
            texto_preco = "Preço não encontrado"  

        try:
            elemento_ofertas = driver.find_element("xpath", '//button[@class="btn btn-blue"]')
            texto_ofertas = elemento_ofertas.text.strip()
            valor_ofertas = re.findall(r'\d+', texto_ofertas)[0]
        except Exception as e:
            valor_ofertas = "0" 

        return texto_item, texto_preco, valor_ofertas

    except Exception as e:
        print("Erro ao encontrar o item:", e)
        return None, None, None

def atualizar_planilha(file_path):
    # Configurar as opções do Chrome para negar notificações
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")

    # Inicializar o Chrome WebDriver com um tempo limite de 10 segundos
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)

    # Carregar a planilha
    df = pd.read_excel(file_path)

    # Criar uma lista para armazenar os códigos encontrados durante a pesquisa
    codigos_encontrados = []

    # Iterar sobre as linhas da planilha para buscar e atualizar os itens
    for index, row in df.iterrows():
        codigo_busca = str(row['codigo'])
        if codigo_busca != 'SEM CODIGO':
            texto_item, texto_preco, valor_ofertas = buscar_item_no_site(driver, codigo_busca)
            if texto_item:
                df.at[index, 'nome_produto'] = texto_item
                df.at[index, 'valor'] = texto_preco
                df.at[index, 'lojas'] = valor_ofertas
                df.at[index, 'disponivel'] = 'SIM'  # Atualiza para 'SIM' se o item for encontrado
            else:
                df.at[index, 'disponivel'] = 'NAO'
                df.at[index, 'valor'] = None
                df.at[index, 'lojas'] = None

    # Atualizar a coluna 'disponivel' para 'NAO' para itens 'SEM CODIGO'
    df.loc[df['codigo'] == 'SEM CODIGO', 'disponivel'] = 'NAO'

    # Salvar as alterações na planilha
    df.to_excel(file_path, index=False)
    print("Planilha atualizada com sucesso.")

    # Fechar o navegador
    driver.quit()

# Executar a atualização da planilha
caminho_planilha = r'C:\Users\karen.santos\Downloads\consulta_paraguai\produtos_a_venda.xlsx'
atualizar_planilha(caminho_planilha)

print('Finalizado')
