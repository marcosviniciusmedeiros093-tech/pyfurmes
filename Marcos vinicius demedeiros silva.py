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
            pos=input('digite a posição que esse cliente ocupará')
            nome=input('digite o nome completo: ')
            cpf=input('digite o CPF: ')
            tel=input('digite o telefone para contato: ')
            mail=input('digite o E-mail')
            endereco=input('digite o endereço')
            clients[pos]=[nome,cpf,mail,endereco,tel]
            print('clientes: ',clients)
            print('cadastro concluido')
        elif seletorc==2:
            pos=input('digite a numeração do cliente cadastado: ')
            if pos in clients:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clients[pos][0])
                print(' CPF    :', clients[pos][1])
                print('Email  :', clients[pos][2])
                print('Endereço : ',clients[pos][3])
                print('Telefone : ',clients[pos][4])
                print()
                nome=input('digite o nome completo: ')
                cpf=input('digite o CPF: ')
                tel=input('digite o telefone para contato: ')
                mail=input('digite o E-mail')
                endereco=input('digite o endereço')
                clients[pos]=[nome,cpf,mail,endereco,tel]
                print('alteração concluida')
            else:
                print('cliente não encontrado')
        elif seletorc==3:
            pos=input('digite a numeração do cliente que você quer deletar: ')
            if pos in clients:
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    del clients[pos]
                    print('cliente removido com sucesso')
                else:
                    print('exclusão cancelada')
        elif seletorc==4:
            pos=input('digite a numeração do cliente que você quer visualizar: ')
            if pos in clients:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clients[pos][0])
                print(' CPF    :', clients[pos][1])
                print('Email  :', clients[pos][2])
                print('Endereço : ',clients[pos][3])
                print('Telefone : ',clients[pos][4])
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
            marca=input('escreva o nome da marca: ')
            nomep=input('escreva o nome do produto: ')
            preco=int(input('escreva o preço de mercado do produto: '))
            valor=int(input('escreva o valor do produto para seus clientes: '))
            estoque=int(input('digite o quantidade desse produto no o estoque: '))
        elif seletorp==2:
            altp=int(input('digite a numeração do produto cadastado: '))
            marca=input('escreva o nome da marca: ')
            nomep=input('escreva o nome do produto: ')
            preco=int(input('escreva o preço de mercado do produto: '))
            valor=int(input('escreva o valor do produto para seus clientes: '))
            estoque=int(input('digite o quantidade desse produto no o estoque: '))
            print('alteração concluida')
        elif seletorp==3:
            removep=int(input('digite a numeração do produto que você quer deletar: '))
            salvador=input(' você tem certeza? S/N ')
            if salvador=='s' or salvador=='S':
                print('produto removido com sucesso')
            else:
                print('exlusão cancelada')
        elif seletorp==4:
            pesquisa=int(input('digite a numeração do produto que você quer visualizar: '))
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    elif seletor==3:
        print(' aqui estaria a lista dos produtos')
        seletorv=int(input('''
        digite 1 para deletar venda declarada
        digite 2 para declarar as vendas
        digite 3 para pesquisar vendas
        digite 4 para alterar venda declarada
        '''))
        if seletorv==2:
            produto=input('digite a numerção do produto')
            nome=input('digite a numerção do cliente')
            valorv=input('digite o valor da venda')
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
