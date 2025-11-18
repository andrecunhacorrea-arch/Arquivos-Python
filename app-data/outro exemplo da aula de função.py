#outro exemplo de função

def cadrastro_produto(estoque)
    nome = input("nome do produto: ")
    qtd =  int(input("quantidade: "))
    estoque[nome] = qtd
    print("\n produto cadrastado")


def vender(estoque):
    nome = input("produtos para vender: ")
    if nome in estoque and estoque[nome] > 0:
        estoque[nome] -= 1
        print("venda realizada!")

    else:
        print("produto não encontrado!")

def mostrar(estoque):
    print("\n --------ESTOQUE--------")
    for p, q in estoque.iens():
        print(f"{p}:{q}")


def menu():
    estoque = {}

    while True:
        print("\n1 - cadrastar \n2 - vender, \n3 mostrar estoque \n4 - sair")

        op = int(input("escolha: "))

        match op:
            case 1:
                cadrastro_produto(estoque)

            case 2:
                vender(estoque)

            case 3:
                mostrar(estoque)

            case 4:
                print("saindo...")
                break
            
