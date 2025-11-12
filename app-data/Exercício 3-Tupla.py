#crie uma tupla com os 12 meses do ano peça ao usuário para digitar um número de 1 a 12 e mostre o mês correspondente, se o número for inválido mostre uma mensagem de erro.

meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro") #criação de uma tupla com os 12 meses do ano.

numero = int(input("\n digite um número de 1 a 12 para ver o mês correspondente: ")) #solicita ao usuário que insira um número de 1 a 12.

if 1 <= numero <= 12: #verifica se o número digitado está entre 1 e 12.
    mes = meses[numero - 1] #obtem o mês correspondente subtraindo 1 do número digitado para ajustar ao índice da tupla (que começa em 0).
    print(f"\n o mês correspondente ao número {numero} é: {mes}") #exibe o mês correspondente ao número digitado.
else:
   print("\n número inválido! infelizmente não temos 13 ou mais meses né seu animal.") #mensagem de erro para número inválido.