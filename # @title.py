# @title
seletor=1
escolha='s'
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
        seletor1=int(input('''
        digite 1 para cadastra clientes
        digite 2 para alterar clientes cadastros
        digite 3 para remover clientes cadastrados
        digite 4 para pesquisar clientes cadastrados
        '''))
        if seletor1==1:
            cliente=input('digite seu nome completo: ')
            cpf3=input('digite seu CPF: ')
            tel=input('digite seu telefone para contato: ')
            mail=input('digite seu E-mail')
            endereco=input('digite seu endereço')
            print('cadastro concluido')
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    elif seletor==2:
        seletor2=int(input('''
        digite 1 para cadastra produtos
        digite 2 para alterar produtos cadastros
        digite 3 para remover produtos cadastrados
        digite 4 para pesquisar produtos cadastrados
        '''))
        if seletor2==1:
            print('cadastro de produtos')
            marca=input('escreva o nome da marca: ')
            nomep=input('escreva o nome do produto: ')
            preco=int(input('escreva o preço de mercado do produto: '))
            valor=int(input('escreva o valor do produto para seus clientes: '))
            estoque=int(input('digite o quantidade desse produto no seu estoque: '))
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    elif seletor==3:
        print(' aqui estria a lista dos produtos')
        seletorp=int(input('''
        digite 1 para alterar a quantidade de produtos em estoque
        digite 2 para para remover produto da lista
        digite 3 para declarar as vendas
        digite 4 para ver seus lucros
        digite 5 para pesquisar vendas
        '''))
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