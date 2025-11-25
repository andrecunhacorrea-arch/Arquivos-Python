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


print("====== Concessionária dos uchihas ======")

carros = {
    "porsche": {
        "skyline": 5000.0,
        "porsche 911 carrera": 749486.0,
        "porsche 911 t": 1046812.0,
        "porsche 911 targa 4 gts": 1431250.0,
        "porsche 911 4s coupe 2017": 580563.0,
        "porsche cayenne turbo gt": 1631250.
    }
}

def menu_cliente():
    print("opções de cliente")
    print("\n 1 - comprar carro")
    print(" 2 - alugar carro")
    print(" 3 - ver estoque")
    print(" 4 - sair")


def menu_vendedor():
    print("opções vendedor ")
    print("\n 1 -vender carro")
    print(" 2 - consultar tabela fipe")
    print(" 3 - sair")

if pessoa == 1:
    menu_cliente()
    opc = int(input("escolha uma opção: "))
    
    match opc:
        case 1:
            print("\n=== Comprar carro ===")
            print("Carros disponíveis: ")
            
            for marca, modelos in carros.items():
                print(f"\nModelos da marca {marca}:")
            for modelo, preco in modelos.items():
                print(f" - {modelo} | R$ {preco}")

        case 2:
            print("você escolheu alugar um carro")
        case 3:
            print("você escolheu ver estoque")
        

else:
    menu_vendedor()






