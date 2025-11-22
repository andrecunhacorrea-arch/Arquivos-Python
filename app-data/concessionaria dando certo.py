print("Bem-vindo à concessionária dos Uchihas")

pessoa = int(input("Você é um cliente ou vendedor? (1 = cliente | 2 = vendedor): "))

match pessoa:
    case 1:
        print("Você escolheu ser um cliente")
        cliente = {
            "nome": input("Informe seu nome: "),
            "email": input("Informe seu e-mail: "),
            "saldo": float(input("Informe o seu saldo atual (R$): "))
        }
        print("\n cliente cadrastado")

    case 2:
        print("Você escolheu ser um vendedor")
        vendedor = {
            "nome": input("Informe seu nome: "),
            "email": input("Informe seu e-mail: ")
        }
        print("vendedor cadrastado")

    case _:
        print("\n Só temos as opções 1 ou 2.")

        def menu ():
            print("\n==== concessionário uchiha ======")