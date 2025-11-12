#lá vamos nós de novo para mais um exemplo de tupla, tuplamente tuplástico:

#esse vai ser uma criação de um programa que vai permitir o usuário consultar o preço de um produto digitando o nome do produto.

#cria duas tuplas paralelas, uma com os nomes dos produtos e outra com os preços dos produtos.
Produtos = ("arroz", "feijão", "macarrão", "leite", "pão", "ovos", "miojo", "carne", "frango")
precos = (5.50, 7.90, 4.20, 6.30, 3.00, 8.40, 2.50, 15.00, 12.00)

#exibe a lista completa de produtos com seus respectivos preços
print("Lista de produtos")
for i in range(len(Produtos)):
    print(f"{Produtos[i]}: R$ {precos[i]:.2f}")
    #percorre as tuplas e exibe cada produto com seu preço formatado com duas casas decimais.

#inicia um loop infinito para permitir múltiplas consultas
while True:
    nome = input("\n digite o nome do produto para consultoar o preço (ou 'sair' para encerrar):").lower()
    #metódo .lower() converte a string para minúsculas, facilitando a comparação.
    
    #se o usuário digitar sair, o programa encerra
    if nome == "sair":
        print("Obrigado por usar o sistema de consulta de preços. Até mais!")
        break

    #verifica se o produto está na lista
    if nome in Produtos:
        indice = Produtos.index(nome) #se o produto estiver na lista, obtém o índice do produto, uitlizando index()
        #index() serve para retornar a posição (indice) onde o nome foi encontrado na tupla Produtos.
        print(f"o preço do {nome} é R$: {precos[indice]:.2f}") #exibe o preço do produto formatado com duas casas decimais.
    else:
        print("produto não encontrado. Por favor, verefique o nome do produto e tente novamente.")#se o produto não estiver na lista, exibe essa mensagem.

