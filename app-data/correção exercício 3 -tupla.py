meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho","julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

print(" ------ Meses do Ano ---------")

while True:
    numero = int(input("digite um número entre 1 e 12 para saber o Mês correspondente ( informe -1 para sair): "))

    if numero == -1:
        print("encerrando o sistema, brigadão os crias")
        break
    
    if numero >= 1 and numero <= 12:
        print(f"o mês correspondete é: {meses[numero -1]}")
    else:
        print("não tem mês maior que 13 né seu animal, digita essa bomba novamente ae")