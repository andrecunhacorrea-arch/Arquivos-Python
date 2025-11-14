pessoa = {} #criando um dicionário vazio chamado pessoa

pessoa["nome"] = input("digite seu nome: ") #nome é a chave e o que o usuário digitar sera o valor acossiado
pessoa["idade"] = int(input("digite sua idade: ")) #idade é a chave e o que o usuário digitar será o valor associado, int pois será um número 
pessoa["cidade"] = input("digite sua cidade: ") #cidade é a chave e o que o usuário digitar será o valor acossiado 

print("\n ========DADOS=========")
#opercorrendo o dicionário usando itens{}, chave = nome - valor = o valor do conteúdo guardaddo
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}") #exebindo o valor da chave e valores formatados