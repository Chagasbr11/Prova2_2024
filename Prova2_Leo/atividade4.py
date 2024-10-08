# Função para processar os dados de produtos
def processar_dados():
    # Lista de produtos no formato (nome, preço, quantidade em estoque)
    produtos = [
        ("Arroz", 5.50, 10),
        ("Feijão", 7.25, 8),
        ("Macarrão", 3.20, 15),
    ]

    # Calcular o total de itens em estoque
    total_estoque = sum(produto[2] for produto in produtos)

    # Calcular a média dos preços
    media_precos = sum(produto[1] for produto in produtos) / len(produtos)

    # Encontrar os produtos com preços acima da média
    precos_acima_da_media = [produto[0] for produto in produtos if produto[1] > media_precos]

    # Retornar o total do estoque e a lista de produtos com preços acima da média
    return total_estoque, precos_acima_da_media

# Executar a função e obter os resultados
estoque_total_, produtos_mais_caros = processar_dados()

# Exibir os resultados
print("Estoque total:", estoque_total_)
print("Produtos com preço acima da média:", produtos_mais_caros)

# Testar a função
if __name__ == "__main__":
    print("Processamento de dados de produtos concluído com sucesso!") 
