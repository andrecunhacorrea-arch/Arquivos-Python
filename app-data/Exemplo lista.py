#exemplo de lista
numero = [10,20,30,40,50] #aqui eu criei uma lista de numeros interiros (INT).
print(numero) 
print(numero[4])#aqiu eu estou Acessando a lista e pegano o primeiro valor dela.
numero[1] = 15 #aqui eu Alterei o valor do indice 1 da lista, fazendo com que o valor 20 vire 15.
numero[3] = 25

print(numero) #aqui eu estou imprimindo a lista alterada.

#O comando append() serve para adicionar um novo elemento na lista, como por exemplo, quando você crie uma lista de 2 valores,
#você consegue adicioanr mais um valor dentro da lista, usando esse comando. OBS: é importante a lista ter um nome para poder ser usada 
numero.append(60) #aqui eu adicionei o valor 60 na lista.  
print(numero) #aqui eu estou imprimindo a lista com o novo valor adicionado. 
numero.remove(10) #aqui eu removi o valor 10 da lista.
print(numero) #aqui eu estou imprimindo a lista com o valor 10 removido

if 25 in numero:
    numero.remove(25) #aqui eu removi o valor 25 da lista, usando uma condicional para verificar se o valor 25 está na lista, se o valor estiver na lista, ele vai remover o valor 25.
print(numero) #aqui eu estou imprimindo a lista com o valor 25 removido.

