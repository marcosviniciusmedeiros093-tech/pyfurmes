# @title
#re fazer os arquivos usando .txt
import pickle

seletor=1
escolha='s'

clientes={}
try:
    arq_clientes = open("clientes.py", "rt", encoding="utf-8")
    for linha in arq_clientes:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            posc = campos[0]
            nome = campos[1]
            cpf= campos[2]
            mail = campos[3]
            endereco= campos[4]
            tel = campos[5]
            cad= campos[6]
            clientes[posc]=[nome,cpf,mail,endereco,tel,cad]
    arq_clientes.close()
except:
    clientes={
        '123' : ["Homer Simpson",'0933863826', "homer@springfield.com",'rua', "99999-9999",True],
        '234' : ["Marge Simpson",'0933863826', "marge@springfield.com",'rua', "88888-8888",True],
        '345' : ["Bart Simpson",'0933863826', "bart@springfield.com",'rua', "77777-7777",True],
        '456' : ["Lisa Simpson",'0933863826', "lisa@springfield.com",'rua', "66666-6666",True],
        '678' : ["Maggie Simpson",'0933863826', "maggie@springfield.com",'rua', "55555-5555",True]
    }
    arq_clientes = open("clientes.py", "wt", encoding="utf-8")
    for posc, dados in clientes.items():
        arq_clientes.write(f"{posc},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
    arq_clientes.close()

produtos={}
vendas={}
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
            clientes[posc]=[nome,cpf,mail,endereco,tel,True]
            print('clientes: ',clientes)
            print('cadastro concluido')

        elif seletorc==2:
            posc=input('digite a numeração do cliente cadastado: ')
            if posc in clientes and clientes[posc][5]==True:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clientes[posc][0])
                print(' CPF    :', clientes[posc][1])
                print('Email  :', clientes[posc][2])
                print('Endereço : ',clientes[posc][3])
                print('Telefone : ',clientes[posc][4])
                print()
                nome=input('digite o nome completo: ')
                cpf=input('digite o CPF: ')
                tel=input('digite o telefone para contato: ')
                mail=input('digite o E-mail')
                endereco=input('digite o endereço')
                clientes[posc]=[nome,cpf,mail,endereco,tel,True]
                print('alteração concluida')
            else:
                print('cliente não encontrado')

        elif seletorc==3:
            posc=input('digite a numeração do cliente que você quer deletar: ')
            if posc in clientes and clientes[posc][5]==True:
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    clientes[posc][5]=False
                    print('cliente removido com sucesso')
                else:
                    print('exclusão cancelada')

        elif seletorc==4:
            posc=input('digite a numeração do cliente que você quer visualizar: ')
            if posc in clientes and clientes[posc][5]==True:
                print(' Dados atuais do cliente:')
                print(' Nome     :', clientes[posc][0])
                print(' CPF    :', clientes[posc][1])
                print('Email  :', clientes[posc][2])
                print('Endereço : ',clientes[posc][3])
                print('Telefone : ',clientes[posc][4])
                print()
            else:
                print('cliente não encontrado')

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
            produtos[posp]=[marca,nomep,preco,valor,estoque,True]

        elif seletorp==2:
            posp=int(input('digite a numeração do produto cadastado: '))
            if posp in produtos and produtos[posp][5]==True:
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
                produtos[posp]=[marca,nomep,preco,valor,estoque,True]
                print('alteração concluida')
            else:
                print('produto não encontrado')

        elif seletorp==3:
            posp=(input('digite a numeração do produto que você quer deletar: '))
            if posp in produtos and produtos[posp][5]==True:
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    produtos[posp][5]=False
                    print('produto removido com sucesso')
                else:
                    print('exclusão cancelada')
            else:
                print('produto não encontrado')

        elif seletorp==4:
            posp=input('digite a numeração do produto que você quer visualizar: ')
            if posp in produtos and produtos[posp][5]==True:
                print(' Dados atuais do produto:')
                print(' Marca     :', produtos[posp][0])
                print(' Nome    :', produtos[posp][1])
                print('Valor de mercado  :', produtos[posp][2])
                print('Valor de venda : ',produtos[posp][3])
                print('Estoque : ',produtos[posp][4])
                print()
            else:
                print('produto não encontrado')

    elif seletor==3:
        seletorv=int(input('''
        digite 0 para sair
        digite 1 para declarar as vendas
        digite 2 para alterar venda declarada
        digite 3 para deletar venda declarada
        digite 4 para pesquisar vendas
        '''))

        if seletorv==1:
            posv=input('digite a numerção da venda')
            for posp in produtos:
                print(f'Nome do produto: {produtos[posp][1]}')
            posp=input('digite a numerção do produto')
            for posc in clientes:
                print(f'Nome do cliente: {clientes[posc][0]}')
            posc=input('digite a numerção do cliente que comprou')
            if posp in produtos and posc in clientes:
                valorv=input('digite o valor da venda')
                vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,True]

        elif seletorv==2:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas and vendas[posv][4]==True:
                    print(' Dados atuais da venda:')
                    print(' Nome do cliente     :', vendas[posv][0])
                    print(' Marca do produto    :', vendas[posv][1])
                    print('Produto  :', vendas[posv][2])
                    print('Valor da venda : ',vendas[posv][3])
                    print()
                    for posp in produtos and produtos[posp][5]==True:
                        print(f'Nome do produto: {produtos[posp][1]}')
                    posp=input('digite a numerção do produto')
                    for posc in clientes and clientes[posc][5]==True:
                        print(f'Nome do cliente: {clientes[posc][0]}')
                    posc=input('digite a numerção do cliente que comprou')
                    if posp in produtos and posc in clientes and produtos[posp][5]==True and clientes[posc][5]==True:
                        valorv=input('digite o valor da venda')
                        vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,True]
                        print('venda alterada com sucesso')

        elif seletorv==3:
                posv=(input('digite a numeração da venda que você quer deletar: '))
                if posv in vendas and vendas[posv][4]==True:
                    salvador=input(' você tem certeza? S/N ')
                    if salvador=='s' or salvador=='S':
                        vendas[posv][4]=False
                        print('venda removida com sucesso')
                    else:
                        print('exclusão cancelada')
                else:
                    print('venda não encontrada')

        elif seletorv==4:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas and vendas[posv][4]==True:
                    print(' Dados atuais da venda:')
                    print(' Nome do cliente     :', vendas[posv][0])
                    print(' Marca do produto    :', vendas[posv][1])
                    print('Produto  :', vendas[posv][2])
                    print('Valor da venda : ',vendas[posv][3])
                    print()
                    for posp in produtos:
                        print(f'Nome do produto: {produtos[posp][1]}')
                    posp=input('digite a numerção do produto')
                    for posc in clientes:
                        print(f'Nome do cliente: {clientes[posc][0]}')
                    posc=input('digite a numerção do cliente que comprou')
                    if posp in produtos and posc in clientes:
                        valorv=input('digite o valor da venda')
                        vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,True]
                msg=input('esta parte está em desenvolvimento digite ENTER para sair ')

    elif seletor==4:
        seletorl=int(input('''
        digite 1 para lista de clientes
        digite 2 para lista de produtos
        digite 3 para lista de vendas
        '''))
        if seletorl==1:
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar cliente excluidos
        digite 2 para mais informações dos clientes
        '''))
            for posc in clientes:
                if clientes[posc][5]==True:
                    print(f'''nome:{clientes[posc][0]} | Posição: {posc} | Status: cadastrado''')
                elif clientes[posc][5]==False:
                    print(f'''nome:{clientes[posc][0]} | Posição: {posc} | Status: excluido''')

            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar algum cliente excluido? S/N')
                    if recad=='S' or recad=='s':
                        posc=input('digite a posição do cliente:')
                        if posc in clientes and clientes[posc][5]==True:
                            print('o cliente já é cadastrado, escolha um que foi excluido')
                        if posc in clientes and clientes[posc][5]==False:
                            clientes[posc][5]=True
                            print('cliente re-cadastrado com sucesso')
                    elif recad != 'n' and recad!='N':
                        print(' opção invalida')

            elif opcoes==2:
                decision=''
                while decision !='n' and decision!='N':
                    posc=input('digite a posição do cliente')
                    if posc in clientes:
                        print('Nome do cliente: ',clientes[posc][0])
                        print('CPF: ', clientes[posc][1])
                        print('Email: ',clientes[posc][2])
                        print('Endereço: ',clientes[posc][3])
                        print('Telefone: ',clientes[posc][4])
                        decision=input('gostaria de continuar selecionando clientes?')
                    else:
                        print('cliente não encontrado')
                        decision=input('gostaria de continuar selecionando clientes?')


        if seletorl==2:
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar produtos excluidos
        digite 2 para mais informações de produtos
        '''))
            for posp in produtos:
                if produtos[posp][5]==True:
                    print(f'''Nome:{produtos[posp][1]} | Posição: {posp} | Status: cadastrado''')
                elif produtos[posp][5]==False:
                    print(f'''Nome:{produtos[posp][1]} | Posição: {posp} | Status: excluido''')

            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar algum produto excluido? S/N ')
                    if recad=='S' or recad=='s':
                        posp=input('digite a posição do produto:')
                        if posp in produtos and produtos[posp][5]==True:
                            print('o produto já é cadastrado, escolha um que foi excluido')
                        elif posp in produtos and produtos[posp][5]==False:
                            produtos[posp][5]=True
                            print('produto re-cadastrado com sucesso')
                    elif recad!='n' and recad!='n':
                        print(' opção invalida')
            elif opcoes==2:
                decision=''
                while decision !='n' and decision!='N':
                    posp=input('digite a posição do produto')
                    if posp in produtos:
                        print('Marca: ',clientes[posc][0])
                        print('Nome: ', clientes[posc][1])
                        print('Preço de mercado: ',clientes[posc][2])
                        print('Valor de venda: ',clientes[posc][3])
                        print('Estoque: ',clientes[posc][4])
                        decision=input('gostaria de continuar selecionando produtos?')
                    else:
                        print('produto não encontrado')
                        decision=input('gostaria de continuar selecionando produtos?')

        if seletorl==3:
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar vendas excluidas
        digite 2 para mais informações de vendas
        '''))
            for posv in vendas:
                if vendas[posv][4]==True:
                    print(f'''Nome do cliente: {vendas[posv][0]} | Nome do produto: {vendas[posv][2]} | Posição: {posv} | Valor da venda: {vendas[posv][3]} | Status: cadastrada''')
                elif vendas[posv][4]==False:
                    print(f'''Nome do cliente: {vendas[posv][0]} | Nome do produto: {vendas[posv][2]} | Posição: {posv} | Valor da venda: {vendas[posv][3]} | Status: excluida''')
            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar alguma venda excluida? S/N ')
                    if recad=='S' or recad=='s':
                        posv=input('digite a posição da venda:')
                        if posv in vendas and vendas[posv][4]==True:
                            print('a venda já é cadastrada, escolha uma que foi excluida')
                        if posv in vendas and vendas[posv][4]==False:
                            vendas[posv][4]=True
                            print('venda re-cadastrada com sucesso')
                    elif recad != 'n' and recad!='N':
                        print(' opção invalida')
            elif opcoes==2:
                decision=''
                while decision !='n' and decision!='N':
                    posp=input('digite a posição do produto')
                    if posp in produtos:
                        print(' Nome do cliente     :', vendas[posv][0])
                        print(' Marca do produto    :', vendas[posv][1])
                        print('Produto  :', vendas[posv][2])
                        print('Valor da venda : ',vendas[posv][3])
                        decision=input('gostaria de continuar selecionando vendas?')
                    else:
                        print('venda não encontrada')
                        decision=input('gostaria de continuar selecionando vendas?')

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
arq_clientes= open("clientes.py", "wt", encoding="utf-8")
for posc, dados in clientes.items():
    arq_clientes.write(f"{posc},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
arq_clientes.close()
