
#SISTEMA DE VENDAS

estoque_produtos = {
 1:{"Nome": "Camiseta de banda Blade and Bath", "preco":110.00, "quantidade": 20},
 2:{"Nome": "Camiseta de banda Decalius", "preco":100.00, "quantidade":17},
 3:{"Nome": "Camiseta de banda Made Of Pain", "preco":99.99, "quantidade":50},
 4:{"Nome": "Camiseta de banda Type O negative", "preco":110.00, "quantidade":33}
}

carrinho = []

while True:
    print("💀💀💀💀💀💀💀💀💀💀💀")
    print("Seja bem vindo!")
    print("💀💀💀💀💀💀💀💀💀💀💀")
    print(" [1] Vizualizar estoque.")
    print(" [2] Adicionar item ao carrinho.")
    print(" [3] Vizualizar carrinho.")
    print(" [4] Finalizar compra.")
    print(" [5] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Vizualizando Estoque!")
        print("ID | NOME | VALOR | QUANTIDADE")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}| {valor}")

    elif opcao == 2:
        print("Adicionando itens ao carrinho!")
        id_produto = int(input("Qual ID do produto você deseja comprar? "))
        if id_produto in estoque_produtos:
            qtd_produto = int(input("Quantas unidades vcê deseja?"))
            if qtd_produto <= 0:
                print("Quantidade inválida!")
            elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                item = {
                    "qtd": qtd_produto,
                    "nome": estoque_produtos[id_produto]["nome"],
                    "preco": estoque_produtos[id_produto]["preco"],
                    "preco_total": qtd_produto * estoque_produtos[id_produto]["preco"]
                }
                carrinho.append(item)
                estoque_produtos[id_produto]["quantidade"] -= qtd_produto
                print(item)
            else:
                print(f"Quantidade indisponivel, temos apenas"
                      f"{estoque_produtos[id_produto]["quantidade"]} no estoque.")
        else:
            print("Id informado não existe no estoque!")

    elif opcao == 3:
        print("Vizualizando carrinho!")
        subtotal = 0
        for i in carrinho:
            print(f"{i["qtd"]}x {i["nome"]} no valor de R$ {i["preco"]}(cada)\nTotal R${i["preco_total"]}")
            subtotal += i["preco_total"]
            print(f"Subtotal da compra R${subtotal}")

        else:
            print("Carrinho vazio!")

    elif opcao == 4:
        print("Finalizando compra!")

    elif opcao == 5:
        print("Saindo do sistema!")

    else:
        print("Opção inválida!!Tenta denovo beta")
