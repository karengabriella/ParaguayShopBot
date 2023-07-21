import tkinter as tk
from tkinter import ttk, messagebox

# Lista simulando o conteúdo do arquivo
dados_excel = [
    {"Código Produto": "123", "Nome Produto": "Produto A", "Preço": "10.00"},
    {"Código Produto": "456", "Nome Produto": "Produto B", "Preço": "15.50"},
    {"Código Produto": "789", "Nome Produto": "Produto C", "Preço": "20.00"},
]

def on_new_product():
    # Lógica para adicionar um novo produto
    new_product = new_product_entry.get()
    print("Cadastrar Produto:", new_product)
    new_product_entry.delete(0, tk.END)  # Limpar o campo de entrada após cadastrar o produto

def on_update_item():
    # Lógica para atualizar o item selecionado
    item_to_update = update_entry.get()
    print("Atualizar Produto:", item_to_update)
    update_entry.delete(0, tk.END)  # Limpar o campo de entrada após atualizar o produto

def on_search_item():
    # Lógica para buscar o item selecionado
    item_to_search = search_entry.get()
    print("Buscar Produto:", item_to_search)

    # Procurar o produto na lista simulada
    produto_encontrado = None
    for linha in dados_excel:
        if linha["Código Produto"] == item_to_search:
            produto_encontrado = linha
            break

    # Exibir a linha encontrada em uma nova janela ou mostrar uma mensagem de erro
    if produto_encontrado:
        show_product_window(produto_encontrado)
    else:
        messagebox.showinfo("Produto não encontrado", "O produto não foi encontrado na lista.")

    search_entry.delete(0, tk.END)  # Limpar o campo de busca após buscar o produto

def show_product_window(produto):
    # Criar uma nova janela para exibir os dados do produto
    product_window = tk.Toplevel(root)
    product_window.title("Produto")
    product_window.geometry("250x150")

    # Exibir os dados do produto na nova janela
    produto_info_label = ttk.Label(product_window, text=f"Código: {produto['Código Produto']}\n"
                                                         f"Nome: {produto['Nome Produto']}\n"
                                                         f"Preço: {produto['Preço']}")
    produto_info_label.pack(padx=10, pady=10)

    # Botão "Remover Produto" para deletar o produto da lista
    def remove_product():
        resposta = messagebox.askyesno("Remover Produto", "Deseja remover o produto da lista?")
        if resposta:
            dados_excel.remove(produto)
            product_window.destroy()
            print("Produto removido:", produto)

    remover_produto_button = ttk.Button(product_window, text="Remover Produto", command=remove_product)
    remover_produto_button.pack(pady=5)

def on_download_today():
    # Lógica para baixar os itens de hoje
    print("Download hoje")

# Criar a janela principal
root = tk.Tk()
root.title("Consulta de Produtos")
root.geometry("400x250")  # Definir tamanho da janela (largura x altura)

# Frame para agrupar elementos relacionados ao "Cadastrar"
new_product_frame = ttk.Frame(root)
new_product_frame.pack(pady=10)

# Label para indicar o campo de entrada
new_product_label = ttk.Label(new_product_frame, text="Código Produto")
new_product_label.grid(row=0, column=0)

# Campo de entrada para digitar um novo produto
new_product_entry = ttk.Entry(new_product_frame, width=30)
new_product_entry.grid(row=0, column=1, padx=5)

# Botão 'Cadastrar'
new_product_button = ttk.Button(new_product_frame, text="Cadastrar", command=on_new_product)
new_product_button.grid(row=0, column=2, padx=5)

# Frame para agrupar elementos relacionados ao "Atualizar"
update_frame = ttk.Frame(root)
update_frame.pack(pady=10)

# Label para indicar o campo de entrada
update_label = ttk.Label(update_frame, text="Código Produto")
update_label.grid(row=0, column=0)

# Campo de entrada para buscar itens (para "Atualizar")
update_entry = ttk.Entry(update_frame, width=30)
update_entry.grid(row=0, column=1, padx=5)

# Botão 'Atualizar'
update_button = ttk.Button(update_frame, text="Atualizar", command=on_update_item)
update_button.grid(row=0, column=2, padx=5)

# Frame para agrupar elementos relacionados ao "Buscar"
search_frame = ttk.Frame(root)
search_frame.pack(pady=10)

# Label para indicar o campo de entrada
search_label = ttk.Label(search_frame, text="Código Produto")
search_label.grid(row=0, column=0)

# Campo de entrada para buscar itens (para "Buscar")
search_entry = ttk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5)

# Botão 'Buscar'
search_button = ttk.Button(search_frame, text="Buscar", command=on_search_item)
search_button.grid(row=0, column=2, padx=5)

# Frame para agrupar elementos relacionados aos botões "Atualizar Todos" e "Download hoje"
bottom_frame = ttk.Frame(root)
bottom_frame.pack(pady=10)

# Botão 'Atualizar Todos'
update_all_button = ttk.Button(bottom_frame, text="Atualizar Todos", command=on_update_item)
update_all_button.grid(row=0, column=0, padx=5)

# Botão 'Download hoje'
download_today_button = ttk.Button(bottom_frame, text="Download hoje", command=on_download_today)
download_today_button.grid(row=0, column=1, padx=5)

# Executar o loop principal da aplicação
root.mainloop()
