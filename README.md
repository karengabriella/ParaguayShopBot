
# Robô de Consulta e Atualização de Produtos no site que reune as principais Lojas do Paraguai.

Este repositório contém um robô desenvolvido para consultar a disponibilidade e atualização de produtos em lojas do Paraguai. 

O robô permite buscar informações de produtos por código e nome, atualizar valores e disponibilidade e exportar os dados coletados para um arquivo Excel.

# Funcionalidades

- Consulta por Código do Produto: O robô permite buscar informações de produtos utilizando o código do produto.

- Cadastro de Novos Produtos: Caso o código do produto não esteja disponível, o robô cadastra o produto utilizando o nome fornecido e gera um código.

- Atualização de Dados: O robô atualiza o valor e a disponibilidade dos produtos em tempo real.

- Exportação para Excel: Todos os dados coletados e atualizados são exportados para um arquivo Excel para facilitar a análise e o gerenciamento.

# Estrutura do Projeto

- view.py: Script principal interface do robô.
- funcoes_consulta.py: Módulo responsável pela consulta e atualização de produtos.
- funcoes_consulta_seguranca.py: backup de funções primárias que funcionam mesmo que a estrutura do site mude.
- encontrar_codigo.py: Módulo responsável pelo cadastro de novos produtos.
- produtos_a_venda.xlsx: arquivo excel padrão necessário.


## Instalação

Rrequirements:

```bash
selenium
pandas
webdriver-manager
tkinter

```
    
## Stack utilizada

**Front-end:** Python tkinter

**Back-end:** Python 3.12.1 


## Usado por

Esse projeto é usado pelas seguintes empresas:

- Baron's Tech


