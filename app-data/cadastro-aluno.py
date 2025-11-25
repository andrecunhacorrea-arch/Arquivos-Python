#Objetivo: Criar um programa de gerenciamento de notas e mostrar o uso de len(), append(), sum(), remove()

#lista vazuia para armazenar as notas dos alunos
notas = []

print("Bem-vindo ao sistema de gerenciamento de notas!")

#Menu de opções para o usuário
while True: 
    print("\n Menu de opções:")
    print("1. Adicionar nota")
    print("2. Remover nota")
    print("3. Mostrar todas as notas")
    print("4. Mostrar a quantidade e média das notas")
    print("5. Sair")

    #se a opção for 1, adicionar nota
    opcao = int(input("escolha uma opção (1-5): "))
    if opcao == 1:
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)
        print("Nota adicionada com sucesso!")

    #remover nota
    elif opcao == 2: #elif é igual ao senão se no portugol, uma condicional dentro de outra condicional
        if len(notas) == 0: #verifica se a lista está vazia
            print("Nenhuma nota para remover.")# se a lista estiver vazia, mostra essa mensagem
        else:
            print("Notas atuais: ", notas) #mostra as notas atuais
            remover = float (input("digite a nota que deseja remover: "))#pega a nota que o usuário deseja remover
            if remover in notas:
                notas.remove(remover)# remove a nota da lista
                print("nota removida com sucesso!")
            else:
                print("essa nota não está na lista.") #se a nota não estiver na lista, mostra essa mensagem

    #mostrar todas as notas            
    elif opcao == 3:    
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")# se a lista estiver vazia, mostra essa mensagem
        else:
            print("Notas cadastradas: ", notas) #mostra as notas cadastradas

    #mostrar quantidade e média das notas
    elif opcao == 4:
        if len(notas) == 0:
            print("nenhuma nota cadastrada") # se a lista estiver vazia, mostra essa mensagem
        else:
            print("quantidade de notas: ", len(notas))#mostra a quantidade de notas cadastradas
            print("média das notas: ", sum(notas)/len(notas))#mostra a média das notas, len ler a quantidade de notas e sum soma as notas
            

    #sair do sistema
    elif opcao == 5:
        print("Obrigado por usar nosso sistema, até mais!")
        break
    else:
        print("opção inválida, por favor escolha uma opção válida.")
        continue #continua o loop do menu
        pritn
    