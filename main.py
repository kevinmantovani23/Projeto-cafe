MENU = {
    "expresso": {
        "ingredientes": {
            "água": 50,
            "café": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "custo": 3.0,
    }
}
moedas = {
    "quantidade":{
        "um real": 0,
        "cinquenta centavos": 0,
        "vinte-cinco centavos": 0,
        "dez centavos": 0,
    },
    "valor":{
        "um real": 1,
        "cinquenta centavos": 0.50,
        "vinte-cinco centavos": 0.25,
        "dez centavos": 0.10,
    }
}
resources = {
    "água": 810,
    "leite": 500,
    "café": 400,
    "dinheiro": 0,
}
total = 0


def verificar_recurso(pedido_ingredientes):
    for item in pedido_ingredientes:
        if pedido_ingredientes[item] >= resources[item]:
            print(f'Desculpe, não há {item} suficiente.')
            return False
        else:
            return True


def atualizar_valor(sabor_escolhido):
    for item in sabor_escolhido:
            resources[item] = resources[item] - sabor_escolhido[item]




while True:
    choice = input("Qual café você deseja? (expresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Água: {resources['água']}ml")
        print(f"Leite: {resources['leite']}ml")
        print(f"Café: {resources['café']}g")
        print(f"Dinheiro: R${resources['dinheiro']}")
        continue
    else:
        bebida = MENU[choice]
        if verificar_recurso(bebida['ingredientes']):
            dinheiro = moedas['quantidade']
            valor = moedas['valor']
            for item in dinheiro:
                dinheiro[item] = int(input(f'Insira a quantidade de moedas de {item}: '))
                total = total + dinheiro[item] * valor [item]
            if total < bebida['custo']:
                print('O valor que você inseriu é insuficiente. Moedas retornadas.')
                continue
            print(f'Aqui está o seu {choice}, aprecie esse saboroso café.')
            if total > bebida['custo']:
                total = total - bebida['custo']
                total = round(total, 2)
                print(f'Aqui está o troco: R${total}')
            resources['dinheiro'] += total
            atualizar_valor(bebida['ingredientes'])


