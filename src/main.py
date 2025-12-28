from tabela_diaria import criacao_de_tabela
tabela_de_precos = criacao_de_tabela()

#interface
def interface():

    with open('relatorio.txt','a') as f: #anotando no relatório de vendas
        f.write(f'RELATORIO DO DIA\n')
        ativacao = True #manter a máquina ativa ou não
        cliente = 1
        while ativacao == True:
            print('BEM VINDO AO MERCADO!')
            print('DIGITE A SUA LISTA DE COMPRAS ABAIXO:\n')
            
            preço_total = 0
            quantidade_total = int(input('QUANTIDADE DE PRODUTOS: '))
            
            print('DIGITE O PRODUTO E SUA QUANTIDADE: ')
            lista_cliente = []
            erro = False #tratamento de erro
            while quantidade_total != 0: #recebendo os produtos e calculando o total
                
                produto, quantidade = input().rsplit(maxsplit=1)
                produto, quantidade = produto.lower(), int(quantidade)
                
                if quantidade > quantidade_total:
                    print('ERRO, QUANTIDADE É MAIOR QUE O TOTAL, TENTE NOVAMENTE.')
                    erro = True
                    break
                elif quantidade < 0:
                    print('ERRO, QUANTIDADE NEGATIVA, TENTE NOVAMENTE.')
                    erro = True
                    break

                lista_cliente.append((produto, quantidade))
                quantidade_total -= quantidade
            
            if erro == True: #reinicia a lista do cliente
                continue
            
            for j in lista_cliente: #calculando o total 
                if j[0] not in tabela_de_precos: #produto não consta na tabela
                    print('ERRO, PRODUTO NÃO FOI ENCONTRADO, TENTE NOVAMENTE.')
                    erro = True
                    break
                preço_total += tabela_de_precos[j[0]] * j[1]
            
            if erro == True: #reinicia a lista do cliente
                continue

            print(f'SEU TOTAL É DE {preço_total:.2f}')
            f.write(f'cliente {cliente}: {preço_total:.2f}\n') #registrando 
            cliente += 1
            
            desativacao = input('deseja manter ativa a máquina? S/N').strip().upper()
            if desativacao == 'N':
                f.write(f'\n*************************'.strip())
                f.write(f'\n')
                ativacao = False

interface()