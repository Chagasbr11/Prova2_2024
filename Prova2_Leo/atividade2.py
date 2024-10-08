# Função para calcular a temperatura média por cidade
def calcular_temperatura_media(cidades_temperaturas):
    # Lista para armazenar os resultados
    temperaturas_medias = []
    
    # Iterar sobre a lista de tuplas (cidade, lista de temperaturas)
    for cidade, temperaturas in cidades_temperaturas:
        # Calcular a média das temperaturas da cidade
        media = sum(temperaturas) / len(temperaturas)
        # Adicionar a tupla (cidade, temperatura média) à lista de resultados
        temperaturas_medias.append((cidade, media))
    
    return temperaturas_medias

# Exemplo de dados: lista de tuplas (cidade, temperaturas)
cidades_temperaturas = [
    ("São Paulo", [22.5, 23.0, 21.5, 20.0, 19.5, 22.0, 21.0]),
    ("Rio de Janeiro", [30.0, 31.5, 32.0, 29.5, 28.0, 30.0, 31.0]),
    ("Belo Horizonte", [25.0, 26.0, 24.5, 23.0, 22.0, 24.0, 25.5])
]

# Chamar a função e armazenar os resultados
resultados = calcular_temperatura_media(cidades_temperaturas)

# Exibir os resultados
for cidade, media in resultados:
    print(f"A temperatura média em {cidade} foi de {media:.2f}°C")

# Testar a função
if __name__ == "__main__":
    print("Temperaturas médias calculadas com sucesso!") 
