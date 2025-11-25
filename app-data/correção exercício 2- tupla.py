#correção do exercício 2

numeros = ()
contador = 0

print("por favor caro gafanhoto, digite 5 numeros: ")
for i in range(5):
    n = int(input(f"digite o {i+1}° número: "))
    numeros += (n, )

    if len(numeros) == 5:
        contador += 1

    print(f"numeros digitados: {numeros}")
    print(f"Maior número digitado {max(numeros)}")
    print(f"menor número digitado {min(numeros)}")

