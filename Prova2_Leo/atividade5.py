# a) Função para criar um produto
def criar_produto(nome, codigo, preco, estoque):
    # Retorna a tupla no formato (nome, codigo, preco, estoque)
    return (nome, codigo, preco, estoque)

# b) Função para atualizar o estoque de um produto
def atualizar_estoque(produto, quantidade):
    nome, codigo, preco, estoque = produto
    # Atualiza o estoque somando a quantidade
    novo_estoque = estoque + quantidade
    # Retorna uma nova tupla com o estoque atualizado
    return (nome, codigo, preco, novo_estoque)

# c) Função para listar os produtos
def listar_produtos(produtos):
    print("Lista de produtos disponíveis:")
    for produto in produtos:
        nome, codigo, preco, estoque = produto
        print(f"Nome: {nome}, Código: {codigo}, Preço: R${preco:.2f}, Estoque: {estoque} unidades")

# d) Exemplo de uso
if __name__ == "__main__":
    # Criar três produtos
    produto1 = criar_produto("Arroz", 101, 5.50, 10)
    produto2 = criar_produto("Feijão", 102, 7.25, 8)
    produto3 = criar_produto("Macarrão", 103, 3.20, 15)

    # Lista de produtos
    produtos = [produto1, produto2, produto3]

    # Atualizar o estoque do produto2 (Feijão), adicionando 5 unidades
    produto2_atualizado = atualizar_estoque(produto2, 5)

    # Atualizar a lista com o produto modificado
    produtos[1] = produto2_atualizado

    # Listar todos os produtos
    listar_produtos(produtos) 



