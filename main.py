import random, string

def gerar_senha(tamanho=12):
#Letras maiúsculas, minúsclas, números e símbolos.
    caracteres = string.ascii_letters + string.digits + string.punctuation
#Gerar senha aleatória com tamanho desejado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    try:
#Solicitar o tamanho para o usuário
        tamanho = int(input("Digite o tamanho da senha (ou 0 para SAIR): "))
        if tamanho == 0:
            print("Encerrando o programa!")
            break #Quebra o loop

#Gera e exibe a senha
        print("Senha gerada:", gerar_senha(tamanho))
        print("-" * 40)

    except ValueError:
        print("Por favor, digite um número válido")