# @title
seletor=1
escolha='s'
consumidores=[]
produtos=[]
vendas=[]
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
        cliente=input('digite seu nome completo: ')
        CPF=input('digite seu CPF: ')
        tel=input('digite seu telefone para contato: ')
        mail=input('digite seu E-mail')
        endereço=input('digite seu endereço')
        cadastro=[cliente,CPF,tel,mail,endereço]
        consumidores.append(cadastro)
        print('cadastro concluido')
    elif seletor==2:
        print('cadastro de produtos')
        marca=input('escreva o nome da marca: ')
        nomep=input('escreva o nome do produto: ')
        preço=int(input('escreva o preço de mercado do produto: '))
        valor=int(input('escreva o valor do produto para seus clientes: '))
        estoque=int(input('digite o quantidade desse produto no seu estoque: '))
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    elif seletor==3:
        print(' aqui estria a lista dos produtos')
        seletorp=int(input('''
        digite 1 para alterar a quantidade de produtos em estoque
        digite 2 para para remover produto da lista
        digite 3 para declarar a quantidade de produtos vendidos
        digite 4 para ver seus lucros
        '''))
        msg=input('esta parte está em desenvolvimento digite ENTER para sair ')
    elif seletor==4:
        escolha=int(input('''
        digite 1 para lista de clientes
        digite 2 para lista de produtos
        digite 3 para lista de vendas
        '''))
        tamc=len(consumidores)
        tamv=len(vendas)
        tamp=len(produtos)
        if escolha==1:
            for i in range (tamc):
                print(i+1,'°- nome do cliente: ',consumidores[i][0])
                while escolha==1:
                    escolha=int(input('para ver mais dados de um cliente digite o numero de sua posição'))
                    print(consumidores[escolha-1])
                    retorno=input('gostaria de re-ver a lista de clientes? S/N ')
                    if retorno=='s' or retorno=='S':
                        for i in range (tamc):
                            print(i+1,'°- nome do cliente: ',consumidores[i][0])
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
        print()
    else:
        erro=input('comando invalido digite ENTER para voltar a seleção: ')
print('fim do programa')