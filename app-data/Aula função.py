#a função serve para orgazinar o programa em blocos, como se fosse uma caixa, onde você pode armazenar os dados e utiliza-los como atalho para poder otimizar o código.
#Exenoki, você pode usar a função para armazenar idade





#exemplo de função

def pegar_notas():
    n1 = float(input("digite a sua nota 1: "))
    n2 = float(input("digite a sua nota 2: "))
    n3 = float(input("digite a sua nota 3: "))
    return n1, n2, n3

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3)/3

def verificar_situacao(media):
    if media >= 7:
        return "aprovado"
    
    elif media >=5:
        return "recuperação"
    
    else:
        return "Reprovado"
    
nome = input("nome do aluno: ")
notas = pegar_notas() 
media = calcular_media(*notas)
situcao = verificar_situacao(media)

print(f"\n Aluno: {nome}")
print((f"média: {media:.2f} - situação: {situcao}"))






