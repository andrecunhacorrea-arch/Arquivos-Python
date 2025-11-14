#EXÉRCICIO 2: peça ao usuário para digitar 5 números, armazene esse número em uma tupla depois mostre os números digitados, informe o maio e o menor número e diga quantas vezes o número 5 apareceu na tupla.

numeros = () #criação de tupla vazia para armazenar os números digitados pelo usuário.

for i in range(5):#loop para repetir a entrada 5 vezes
    n = int(input("\n diginte um número interiro: "))

    numeros += (n, ) #adiciona o número digitado à tupla numeros. A vírgula é necessária para indicar que é uma tupla de um único elemento.
    print(f"número {n} adicionado á lista.")


for i, num in enumerate(numeros, start=1): #percorre a tupla de números com um índice começando em 1. o comando enumerate() é usado para obter tanto o índice quanto o valor do elemento na tupla.
    print(f"{i}. {num}") #exibe cada número com seu respectivo número na lista.

vezes_5 = numeros.count(5) #conta quantas vezes o número 5 aparece na tupla usando o método count().
    
print(f"\n maior número: {max(numeros)}") #exibe o maior número.
print(f"\n menor número: {min(numeros)}") #exibe o menor número.
print(f"\n o número 5 apareceu {vezes_5} vezes na lista.") #exibe quantas vezes o número 5 apareceu na tupla.



      
