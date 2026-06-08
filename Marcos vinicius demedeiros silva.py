# @title
seletor=1
escolha='s'
clients={
    '123' : ["Homer Simpson",'0933863826', "homer@springfield.com",'rua', "99999-9999"],
    '234' : ["Marge Simpson",'0933863826', "marge@springfield.com",'rua', "88888-8888"],
    '345' : ["Bart Simpson",'0933863826', "bart@springfield.com",'rua', "77777-7777"],
    '456' : ["Lisa Simpson",'0933863826', "lisa@springfield.com",'rua', "66666-6666"],
    '678' : ["Maggie Simpson",'0933863826', "maggie@springfield.com",'rua', "55555-5555"]
}
produtos={
    '001':['Ivone','perfume a',15.00,20.00,10],
    '002':['Ivone','perfume b',15.00,20.00,10],
    '003':['Ivone','perfume c',15.00,20.00,10],
    '004':['Ivone','perfume d',15.00,20.00,10],
    '005':['Ivone','perfume e',15.00,20.00,10],
}
vendas={
    '001':[clients['123'][0],produtos['001'][0],produtos['001'][1],10.00],
    '002':[clients['345'][0],produtos['002'][0],produtos['002'][1],10.00],
    '003':[clients['456'][0],produtos['003'][0],produtos['003'][1],10.00],
    '004':[clients['678'][0],produtos['004'][0],produtos['004'][1],10.00],
}
while seletor!=0:
    seletor=int(input('''
    para sair digite 0
    digite 1 para cadastra clientes
    digite 2 para cadastrar produtos
    digite 3 para cadastrar vendas
    digite 4 para relatorios
    digite 5 para informações
    '''))

    if seletor==1:
        seletorc=int(input('''
        digite 0 para voltar ao menu principal
        digite 1 para cadastra clientes
        digite 2 para alterar clientes cadastros
        digite 3 para remover clientes cadastrados
        digite 4 para pesquisar clientes cadastrados
        '''))

        if seletorc==1:
            posc=input('digite a posição que esse cliente ocupará')
            nome=input('digite o nome completo: ')
            cpf=input('digite o CPF: ')
            tel=input('digite o telefone para contato: ')
            mail=input('digite o E-mail')
            endereco=input('digite o endereço')
            clients[posc]=[nome,cpf,mail,endereco,tel]
            print('clientes: ',clients)
            print('cadastro concluido')

        elif seletorc==2:
            posc=input('digite a numeração do cliente cadastado: ')
            if posc in clients:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clients[posc][0])
                print(' CPF    :', clients[posc][1])
                print('Email  :', clients[posc][2])
                print('Endereço : ',clients[posc][3])
                print('Telefone : ',clients[posc][4])
                print()
                nome=input('digite o nome completo: ')
                cpf=input('digite o CPF: ')
                tel=input('digite o telefone para contato: ')
                mail=input('digite o E-mail')
                endereco=input('digite o endereço')
                clients[posc]=[nome,cpf,mail,endereco,tel]
                print('alteração concluida')
            else:
                print('cliente não encontrado')

        elif seletorc==3:
            posc=input('digite a numeração do cliente que você quer deletar: ')
            if posc in clients:
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    del clients[posc]
                    print('cliente removido com sucesso')
                else:
                    print('exclusão cancelada')
        
        elif seletorc==4:
            posc=input('digite a numeração do cliente que você quer visualizar: ')
            if posc in clients:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clients[posc][0])
                print(' CPF    :', clients[posc][1])
                print('Email  :', clients[posc][2])
                print('Endereço : ',clients[posc][3])
                print('Telefone : ',clients[posc][4])
                print()
            else:
                print('cliente não encontrado')
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')

    elif seletor==2:
        seletorp=int(input('''
        digite 1 para cadastra produtos
        digite 2 para alterar produtos cadastros
        digite 3 para remover produtos cadastrados
        digite 4 para pesquisar produtos cadastrados
        '''))

        if seletorp==1:
            print('cadastro de produtos')
            posp=input('digite a posição deste produto: ')
            marca=input('escreva o nome da marca: ')
            nomep=input('escreva o nome do produto: ')
            preco=float(input('escreva o preço de mercado do produto: '))
            valor=float(input('escreva o valor do produto para seus clientes: '))
            estoque=int(input('digite o quantidade desse produto no o estoque: '))
            produtos[posp]=[marca,nomep,preco,valor,estoque]

        elif seletorp==2:
            posp=int(input('digite a numeração do produto cadastado: '))
            if posp in produtos:
                print(' Dados atuais do produto:')
                print(' Marca     :', produtos[posp][0])
                print(' Nome    :', produtos[posp][1])
                print('Valor de mercado  :', produtos[posp][2])
                print('Valor de venda : ',produtos[posp][3])
                print('Estoque : ',produtos[posp][4])
                print()
                marca=input('escreva o nome da marca: ')
                nomep=input('escreva o nome do produto: ')
                preco=float(input('escreva o preço de mercado do produto: '))
                valor=float(input('escreva o valor do produto para seus clientes: '))
                estoque=int(input('digite o quantidade desse produto no o estoque: '))
                produtos[posp]=[marca,nomep,preco,valor,estoque]
                print('alteração concluida')
            else:
                print('produto não encontrado')

        elif seletorp==3:
            posp=(input('digite a numeração do produto que você quer deletar: '))
            if posp in produtos:
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    del produtos[posp]
                    print('produto removido com sucesso')
                else:
                    print('exclusão cancelada')
            else:
                print('produto não encontrado')

        elif seletorp==4:
            posp=input('digite a numeração do produto que você quer visualizar: ')
            if posp in produtos:
                print(' Dados atuais do produto:')
                print(' Marca     :', produtos[posp][0])
                print(' Nome    :', produtos[posp][1])
                print('Valor de mercado  :', produtos[posp][2])
                print('Valor de venda : ',produtos[posp][3])
                print('Estoque : ',produtos[posp][4])
                print()
            else:
                print('produto não encontrado')
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')

    elif seletor==3:
        print(' aqui estaria a lista dos produtos')
        seletorv=int(input('''
        digite 0 para sair
        digite 1 para declarar as vendas
        digite 2 para alterar venda declarada
        digite 3 para deletar venda declarada
        digite 4 para pesquisar vendas
        '''))
        
        if seletorv==1:
            posv=input('digite a numerção da venda')
            posp=input('digite a numerção do produto')
            posc=input('digite a numerção do cliente que comprou')
            if posp in produtos and posc in clients:
                valorv=input('digite o valor da venda')
                vendas[posv]=[clients[posc][0],produtos[posp][0],produtos[posp][1],valorv]
        elif seletorv==2:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas:
                    print(' Dados atuais da venda:')
                    print(' Nome do cliente     :', vendas[posv][0])
                    print(' Marca do produto    :', vendas[posv][1])
                    print('Produto  :', vendas[posv][2])
                    print('Valor da venda : ',vendas[posv][3])
                    print()
                    posp=input('digite a numerção do produto')
                    posc=input('digite a numerção do cliente que comprou')
                    if posp in produtos and posc in clients:
                        valorv=input('digite o valor da venda')
                        vendas[posv]=[clients[posc][0],produtos[posp][0],produtos[posp][1],valorv]
                        print('venda alterada com sucesso')

        elif seletorv==3:
                posv=(input('digite a numeração da venda que você quer deletar: '))
                if posv in vendas:
                    salvador=input(' você tem certeza? S/N ')
                    if salvador=='s' or salvador=='S':
                        del vendas[posv]
                        print('venda removida com sucesso')
                    else:
                        print('exclusão cancelada')
                else:
                    print('venda não encontrada')

        elif seletorv==4:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas:
                    print(' Dados atuais da venda:')
                    print(' Nome do cliente     :', vendas[posv][0])
                    print(' Marca do produto    :', vendas[posv][1])
                    print('Produto  :', vendas[posv][2])
                    print('Valor da venda : ',vendas[posv][3])
                    print()
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')        
    elif seletor==4:
        escolha=int(input('''
        digite 1 para lista de clientes
        digite 2 para lista de produtos
        digite 3 para lista de vendas
        '''))
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    
    elif seletor==5:
        print()
        print("Projeto de Gestão de Perfumaria")
        print("Equipe de desenvolvimento:     ")
        print("Marcos Vincius de Medeiros Silva ")
        print("Licença Pública Geral GNU      ")
        print("www.gnu.org/licenses/gpl.html  ")
        input("digite ENTER para sair ")
    
    elif seletor==0:
        print('você saiu do programa')
    else:
        erro=input('comando invalido digite ENTER para voltar a seleção: ')
print('fim do programa')
