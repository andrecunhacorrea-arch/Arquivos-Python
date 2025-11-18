produto =   [{"nome":"café", "preço":25.96, "categoria":"aliemnto", "estoque":900},
            {"nome":"detergente", "preço":2.99, "categoria":"limpeza", "estoque":500 },
            {"nome":"sabão em pó", "preço":7.99, "categoria":"limpeza", "estoque":550},
            {"nome":"pão", "preço":5.99, "categoria":"aliemnto", "estoque":2000}]

print("\n ----Lista de Produto ----")
for i in produto:
    for chave, valor, in i.items(): #serve para pegar a chave e o valor no dicionário
        print(f"{chave}{valor}")
