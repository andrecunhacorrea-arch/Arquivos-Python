numeros = () #criação de tupla com o nome numeros, que irá armazenar valores fornecidos pelo usuário.

#loop para permitir múltiplas entradas de dados
while True: #aqui inicia um loop infinito para permitir múltiplas entradas de dados.
    n = int(input("Digite um número inteiro (ou -1 para sair): ")) #solicita ao usuário que insira um número inteiro.
    if n == -1: #verifica se o usuário deseja sair do loop.
        break #se o usuário digitar -1, o loop é interrompido.

    numeros += (n,) #adiciona o número digitado à tupla numeros. A vírgula é necessária para indicar que é uma tupla de um único elemento.

    if len(numeros) > 0: #verifica se a tupla está vazia, se o número for maior que zero, significa que há elementos na tupla, e executa o bloco de código abaixo.

        print("\n =====RESULTADODS=====\n") #imprime um cabeçalho para os resultados.
        print(f"numeros digitados: {numeros}") #exibe os números digitados pelo usuário.
        print(f"quantidade de numeros digitados: {len(numeros)}") #exibe a quantidade de números digitados.
        print(f"soma: {sum(numeros)}") #exibe a soma dos números digitados.
        print(f"maior número: {max(numeros)}") #exibe o maior número digitado.
        print(f"menor número: {min(numeros)}") #exibe o menor número digitado.

        media = sum(numeros) / len(numeros) #calcula a média dos números digitados.
        
        if media > 50: #verifica se a média é maior que 50.
            print(f"media: {media:.2f} -> Alta!") #exibe a média formatada com duas casas decimais e uma mensagem indicando que a média é maior que 50.
        else:
            print(f"media: {media:.2f} -> Baixa!") #exibe a média formatada com duas casas decimais e uma mensagem indicando que a média é menor ou igual a 50.

    else:
        print("Nenhum número foi digitado.") #se a tupla estiver vazia, informa que nenhum número foi digitado.