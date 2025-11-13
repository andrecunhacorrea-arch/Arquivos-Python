#correção do exercício 2, lista com nomes e salários.

nomes = []
salarios = []

while True:
    nome = input("digite o nome da pessoa para cadastrar (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":
        print("programa finalizado!")
        break

    nomes.append(nome)

    salario = float(input(f"digite o salário do funcionário: "))

    salarios.append(salario)

    print(f"o total de funcionarios cadrastados é de: {len(nomes)}")
    print(f" o total de ")

