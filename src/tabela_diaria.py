#definindo produtos do dia

def criacao_de_tabela():
    tabela_de_precos = {} 
    quant_produtos = int(input('QUANTIDADE DE PRODUTOS: '))
    print(f'DIGITE O NOME E PREÇO DOS {quant_produtos} PRODUTO(S):')
    for i in range(quant_produtos): #registrando os produtos na tabela
        nome, preço = input().rsplit(maxsplit=1)
        preço = float(preço)
        tabela_de_precos[nome.lower()] = preço
    
    return tabela_de_precos