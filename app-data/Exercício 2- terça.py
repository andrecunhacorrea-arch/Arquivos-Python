#criar duas listas, uma com os nomes das pessoas e outra com o seus respectivos salários. 
#o programa deve permitir o usuário cadastrar novos nomes e salários, e ao final mostrar a lista completa de nomes e salários, com o maior e o menor salário.

print("\n Bem-vindo ao sistema de cadastro de nomes e salários!")

nomes = [] #criação de uma lista vazia para armazenar os nomes digitados pelo usuário.
salarios = [] #criação de uma lista vazia para armazenar os salários digitados pelo usuário.

while True: #inicia o loop 
    nome = input("digite o nome da pessoa para cadrastrar (ou 'sair' para encerrar): ") #solicita ao usuário que insira um nome ou digite 'sair' para encerrar o programa.
    if nome.lower() == "sair": #verifica se o usuário digitou 'sair', ignorando maiúsculas e minúsculas.
        print("Encerrando o sistema de cadrastro de nomes e salários. até mais!") #mensagem de despedida.
        break #interrompe o loop se o usuário desejar sair.

    salario = float(input(f"digite o salário de {nome}: R$")) #solicita ao usuário que insira o salário correspondente ao nome digitado.
    nomes.append(nome) #adiciona o nome digitado à lista de nomes.
    salarios.append(salario) #adiciona o salário digitado à lista de salários.
    print(f"nome '{nome}' e salário R${salario:.2f} Cadastrados com sucesso!") #confirmação de que o nome e o salário foram cadastrados.

print("\n Resultados: ") #mensagem indicando o início da exibição dos resultados.   
for i in range(len(nomes)): #percorre as listas de nomes e salários usando um índice.
    print(f"{i+1}. {nomes[i]} - R$ {salarios[i]:.2f}") #exibe cada nome com seu respectivo salário formatado com duas casas decimais.
if len(salarios) > 0: #verifica se a lista de salários não está vazia.
    maior_salario = max(salarios) #obtém o maior salário da lista usando a função max().
    menor_salario = min(salarios) #obtém o menor salário da lista usando a função min().
    indice_maior = salarios.index(maior_salario) #obtém o índice do maior salário na lista.
    indice_menor = salarios.index(menor_salario) #obtém o índice do menor salário na lista.
    print(f"\n maior salário: {nomes[indice_maior]} - R$ {maior_salario:.2f}") #exibe o nome e o valor do maior salário.
    print(F"\n menor salário: {nomes[indice_menor]} - R$ {menor_salario:.2f}") #exibe o nome e o valor do menor salário.
else:
    print("nenhum salário foi cadrastado.") #mensagem informando que nenhum salário foi cadastrado.

    