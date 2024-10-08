# Função para verificar se a entrada é um palíndromo
def verificar_palindromo(entrada):
    # Remover espaços, pontuação e converter para minúsculas
    entrada_limpa = ''.join(e for e in entrada if e.isalnum()).lower()
    
    # Verificar se a sequência é igual ao inverso dela
    return entrada_limpa == entrada_limpa[::-1]

# Função principal
def main():
    # Receber entrada do usuário
    entrada = input("Digite uma palavra, frase ou número para verificar se é um palíndromo: ").strip()

    # Verificar se a entrada está vazia
    if not entrada:
        print("A entrada não pode estar vazia. Tente novamente.")
        return
    
    # Chamar a função de verificação
    if verificar_palindromo(entrada):
        print(f"'{entrada}' é um palíndromo!")
    else:
        print(f"'{entrada}' não é um palíndromo.")

# Chamar a função principal
if __name__ == "__main__":
    main()  
