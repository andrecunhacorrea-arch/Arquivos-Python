#aticidade 1, criar uma lista de nomes, sendo digitado pelo usuário, até o mesmo digitar "sair".

nomes = [] #criação de uma lista vazia para armazenar os nomes digitados pelo usuário.

print("\n Bem-vindo ao sistema de cadastro de nomes!")

while True : #início de um loop infinito para permitir múltiplas entradas de nomes.
    nome = input("Digite um nome para cadastrar (ou 'sair' para encerrar): ") #solicita ao usuário que insira um nome ou digite 'sair' para encerrar o programa.
    
    if nome.lower() == "sair": #verifica se o usuário digitou 'sair', ignorando maiúsculas e minúsculas.
        print("\nEncerrando o sistema de cadastro de nomes. Até mais!") #mensagem de despedida.
        break #interrompe o loop se o usuário desejar sair.

    nomes.append(nome) #adiciona o nome digitado à lista de nomes.
    print(f"Nome '{nome}' cadastrado com sucesso!") #confirmação de que o nome foi cadastrado.

#exibe a lista completa de nomes cadastrados
print("\n nomes cadastrados: ") #mensagem indicando o início da exibição dos nomes cadastrados.
for i, nome in enumerate(nomes, start=1): #percorre a lista de nomes com um índice começando em 1. o comando enumerate() é usado para obter tanto o índice quanto o valor do elemento na lista.
    print(f"{i}. {nome}") #exibe cada nome com seu respectivo número na lista.