# Função para verificar se um número é primo
def eh_primo(numero):
    if numero <= 1:
        return False
    # Verificar se o número tem divisores além de 1 e dele mesmo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função para encontrar os números primos em um array
def verificar_numeros_primos(numeros):
    # Lista para armazenar os números primos
    primos = []
    
    # Verificar cada número da lista
    for numero in numeros:
        if eh_primo(numero):
            primos.append(numero)
    
    return primos

# Exemplo de array com 10 números inteiros
numeros = [10, 3, 4, 7, 11, 14, 17, 19, 20, 23]

# Chamar a função para verificar os números primos
numeros_primos = verificar_numeros_primos(numeros)

# Exibir os números primos encontrados
print(f"Os números primos no array são: {numeros_primos}")

# Testar a função
if __name__ == "__main__":
    print("Verificação de números primos concluída!") 
