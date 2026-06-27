# @title
import pickle
import validações
vcpfetor=1
escolha='s'
seletor=''
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
        '123' : ["Homer Simpson",'0933863826', "homer@springfield.com",'rua', "99999-9999",'True'],
        '234' : ["Marge Simpson",'0933863826', "marge@springfield.com",'rua', "88888-8888",'True'],
        '345' : ["Bart Simpson",'0933863826', "bart@springfield.com",'rua', "77777-7777",'True'],
        '456' : ["Lisa Simpson",'0933863826', "lisa@springfield.com",'rua', "66666-6666",'True'],
        '567' : ["Maggie Simpson",'0933863826', "maggie@springfield.com",'rua', "55555-5555",'True']
    }
    arq_clientes = open("clientes.py", "wt", encoding="utf-8")
    for posc, dados in clientes.items():
        arq_clientes.write(f"{posc},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
    arq_clientes.close()

produtos={}
try:
    arq_produtos = open("produtos.py", "rt", encoding="utf-8")
    for linha in arq_produtos:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            posp= campos[0]
            marca= campos[1]
            nomep= campos[2]
            preco= campos[3]
            valor= campos[4]
            estoque= campos[5]
            cad= campos[6]
            produtos[posp]=[marca,nomep,preco,valor,estoque,cad,]
    arq_produtos.close()
except:
    produtos={
        '001' : [",Ivone",'Perfume a', "15.00",'20.00', "10",'True'],
        '002' : [",Ivone",'Perfume b', "15.00",'20.00', "10",'True'],
        '003' : [",Ivone",'Perfume c', "15.00",'20.00', "10",'True'],
        '004' : [",Ivone",'Perfume d', "15.00",'20.00', "10",'True'],
        '005' : [",Ivone",'Perfume e', "15.00",'20.00', "10",'True']
    }
    arq_produtos = open("produtos.py", "wt", encoding="utf-8")
    for posp, dados in produtos.items():
        arq_produtos.write(f"{posp},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
    arq_produtos.close()

vendas={}
try:
    arq_vendas = open("vendas.py", "rt", encoding="utf-8")
    for linha in arq_vendas:
        linha = linha.strip()
        if linha:
            campos = linha.split(",")
            posv= campos[0]
            nomev= campos[1]
            marcav= campos[2]
            nomepv= campos[3]
            valorv= campos[4]
            cad= campos[5]
            vendas[posv]=[nomev,marcav,nomepv,valorv,cad,]
    arq_vendas.close()
except:
    vendas={
        '001' : [clientes['123'][0],produtos['001'][0],produtos['001'][1],10.00,'True'],
        '002' : [clientes['234'][0],produtos['002'][0],produtos['002'][1],10.00,'True'],
        '003' : [clientes['345'][0],produtos['003'][0],produtos['003'][1],10.00,'True'],
        '004' : [clientes['567'][0],produtos['004'][0],produtos['004'][1],10.00,'True'],
}
    arq_vendas = open("vendas.py", "wt", encoding="utf-8")
    for posv, dados in vendas.items():
        arq_vendas.write(f"{posv},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]}\n")
    arq_vendas.close()

while seletor!=0:
    seletor=int(input('''
    para sair digite 0
    digite 1 para ir para o modulo clientes
    digite 2 para ir para o modulo produtos
    digite 3 para ir para o modulo vendas
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
            posc=input('digite a posição que esse cliente ocupará: ')
            nome=input('digite o nome completo: ')
            while validações.vcpf(cpf)!=True:
                cpf=input('digite o CPF: ')
                if validações.vcpf(cpf)!=True:
                    print('CPF innvalido')
            while validações.vtel(tel)!=True:
                tel=input('digite o telefone para contato: ')
                if validações.vtel(tel)!=True:
                    print('Telefone innvalido')
            tel=input('digite o telefone para contato: ')
            while validações.vmail(mail)!=True:
                mail=input('digite o email: ')
                if validações.vmail(mail)!=True:
                    print('E-mail innvalido')
            endereco=input('digite o endereço: ')
            clientes[posc]=[nome,cpf,mail,endereco,tel,'True']
            print('cadastro de cliente concluido')
            print('cadastro concluido')         
        elif seletorc==2:
            posc=input('digite a numeração do cliente cadastado: ')
            if posc in clientes and clientes[posc][5]=='True':
                print(' Dados atuais do cliente:')
                print(' Nome     :', clientes[posc][0])
                print(' CPF    :', clientes[posc][1])
                print('Email  :', clientes[posc][2])
                print('Endereço : ',clientes[posc][3])
                print('Telefone : ',clientes[posc][4])
                print()
                nome=input('digite o nome completo: ')
                while validações.vcpf(cpf)!=True:
                    cpf=input('digite o CPF: ')
                    if validações.vcpf(cpf)!=True:
                        print('CPF innvalido')
                while validações.vtel(tel)!=True:
                    tel=input('digite o telefone para contato: ')
                    if validações.vtel(tel)!=True:
                        print('Telefone innvalido')
                tel=input('digite o telefone para contato: ')
                while validações.vmail(mail)!=True:
                    mail=input('digite o email: ')
                    if validações.vmail(mail)!=True:
                        print('E-mail innvalido')
                endereco=input('digite o endereço')
                clientes[posc]=[nome,cpf,mail,endereco,tel,'True']
                print('alteração concluida')
            else:
                print('cliente não encontrado')         
        elif seletorc==3:
            posc=input('digite a numeração do cliente que você quer deletar: ')
            if posc in clientes and clientes[posc][5]=='True':
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    clientes[posc][5]='False'
                    print('cliente removido com sucesso')
                else:
                    print('exclusão cancelada')         
        elif seletorc==4:
            posc=input('digite a numeração do cliente que você quer visualizar: ')
            if posc in clientes and clientes[posc][5]=='True':
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
            estoque=''
            print('cadastro de produtos')
            posp=input('digite a posição deste produto: ')
            marca=input('escreva o nome da marca: ')
            nomep=input('escreva o nome do produto: ')
            preco=float(input('escreva o preço de mercado do produto: '))
            valor=float(input('escreva o valor do produto para seus clientes: '))
            while estoque<=0:
                estoque=int(input('digite o quantidade desse produto no o estoque: '))
                if estoque<=0:
                    print('este valor não é permitido')
            produtos[posp]=[marca,nomep,preco,valor,estoque,'True']

        elif seletorp==2:
            posp=input('digite a numeração do produto cadastado: ')
            if posp in produtos and produtos[posp][5]=='True':
                print(' Dados atuais do produto:')
                print(' Marca     :', produtos[posp][0])
                print(' Nome    :', produtos[posp][1])
                print('Valor de mercado  :', produtos[posp][2])
                print('Valor de venda : ',produtos[posp][3])
                print('Estoque : ',produtos[posp][4])
                print()
                marca=input('escreva o nome da marca: ')
                nomep=input('escreva o nome do produto: ')
                preco=float(input('escreva o preço de mercado do produto: (utilize .) '))
                valor=float(input('escreva o valor do produto para seus clientes : (utilize .) '))
                estoque=int(input('digite o quantidade desse produto no o estoque: '))
                produtos[posp]=[marca,nomep,preco,valor,estoque,'True']
                print('alteração concluida')
            else:
                print('produto não encontrado')

        elif seletorp==3:
            posp=(input('digite a numeração do produto que você quer deletar: '))
            if posp in produtos and produtos[posp][5]=='True':
                salvador=input(' você tem certeza? S/N ')
                if salvador=='s' or salvador=='S':
                    produtos[posp][5]='False'
                    print('produto removido com sucesso')
                else:
                    print('exclusão cancelada')
            else:
                print('produto não encontrado')

        elif seletorp==4:
            posp=input('digite a numeração do produto que você quer visualizar: ')
            if posp in produtos and produtos[posp][5]=='True':
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
        digite 1 para cadastrar vendas
        digite 2 para alterar venda cadastrada
        digite 3 para deletar venda cadastrada
        digite 4 para pesquisar vendas
        '''))

        if seletorv==1:
            posv=input('digite a numerção da venda')
            for posp in produtos:
                print(f'Nome do produto: {produtos[posp][1]} | Posição: {posp}')
            posp=input('digite a numerção do produto')
            for posc in clientes:
                print(f'Nome do cliente: {clientes[posc][0]} | Posição: {posc}')
            posc=input('digite a numerção do cliente que comprou')
            if posp in produtos and posc in clientes:
                valorv=input('digite o valor da venda')
                vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,'True']

        elif seletorv==2:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas and vendas[posv][4]=='True':
                    print(' Dados atuais da venda:')
                    print(' Nome do cliente     :', vendas[posv][0])
                    print(' Marca do produto    :', vendas[posv][1])
                    print('Produto  :', vendas[posv][2])
                    print('Valor da venda : ',vendas[posv][3])
                    print()
                    for posp in produtos:
                        if produtos[posp][5]=='True':
                            print(f'Nome do produto: {produtos[posp][1]} | Posição: {posp}')
                    posp=input('digite a numerção do produto')
                    for posc in clientes and clientes[posc][5]=='True':
                        if clientes[posc][5]=='True':
                            print(f'Nome do cliente: {clientes[posc][0]} | Posição: {posc}')
                    posc=input('digite a numerção do cliente que comprou')
                    if posp in produtos and posc in clientes and produtos[posp][5]=='True' and clientes[posc][5]=='True':
                        valorv=input('digite o valor da venda')
                        vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,'True']
                        print('venda alterada com sucesso')
                    else:
                        print('houve algum erro, digite a posição corretamente e de clientes/produtos cadastrados')

        elif seletorv==3:
                posv=(input('digite a numeração da venda que você quer deletar: '))
                if posv in vendas and vendas[posv][4]=='True':
                    salvador=input(' você tem certeza? S/N ')
                    if salvador=='s' or salvador=='S':
                        vendas[posv][4]='False'
                        print('venda removida com sucesso')
                    else:
                        print('exclusão cancelada')
                else:
                    print('venda não encontrada')

        elif seletorv==4:
                posv=input('digite a numerção da venda que você que alterar: ')
                if posv in vendas and vendas[posv][4]=='True':
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
                        vendas[posv]=[clientes[posc][0],produtos[posp][0],produtos[posp][1],valorv,'True']
                msg=input('esta parte está em desenvolvimento digite ENTER para sair ')

    elif seletor==4:
        seletorl=int(input('''
        digite 1 para lista de clientes
        digite 2 para lista de produtos
        digite 3 para lista de vendas
        '''))
        if seletorl==1:
            for posc in clientes:
                if clientes[posc][5]=='True':
                    print(f'''nome:{clientes[posc][0]} | Posição: {posc} | Status: cadastrado''')
                elif clientes[posc][5]=='False':
                    print(f'''nome:{clientes[posc][0]} | Posição: {posc} | Status: excluido''')
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar cliente excluidos
        digite 2 para mais informações dos clientes
        '''))
            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar algum cliente excluido? S/N')
                    if recad=='S' or recad=='s':
                        posc=input('digite a posição do cliente:')
                        if posc in clientes and clientes[posc][5]=='True':
                            print('o cliente já é cadastrado, escolha um que foi excluido')
                        if posc in clientes and clientes[posc][5]=='False':
                            clientes[posc][5]='True'
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
            for posp in produtos:
                if produtos[posp][5]=='True':
                    print(f'''Nome:{produtos[posp][1]} | Posição: {posp} | Status: cadastrado''')
                elif produtos[posp][5]=='False':
                    print(f'''Nome:{produtos[posp][1]} | Posição: {posp} | Status: excluido''')
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar produtos excluidos
        digite 2 para mais informações de produtos
        '''))
            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar algum produto excluido? S/N ')
                    if recad=='S' or recad=='s':
                        posp=input('digite a posição do produto:')
                        if posp in produtos and produtos[posp][5]=='True':
                            print('o produto já é cadastrado, escolha um que foi excluido')
                        elif posp in produtos and produtos[posp][5]=='False':
                            produtos[posp][5]='True'
                            print('produto re-cadastrado com sucesso')
                    elif recad!='n' and recad!='n':
                        print(' opção invalida')
            elif opcoes==2:
                decision=''
                while decision !='n' and decision!='N':
                    posp=input('digite a posição do produto')
                    if posp in produtos:
                        print('Marca: ',produtos[posp][0])
                        print('Nome: ', produtos[posp][1])
                        print('Preço de mercado: ',produtos[posp][2])
                        print('Valor de venda: ',produtos[posp][3])
                        print('Estoque: ',produtos[posp][4])
                        decision=input('gostaria de continuar selecionando produtos?')
                    else:
                        print('produto não encontrado')
                        decision=input('gostaria de continuar selecionando produtos?')

        if seletorl==3:
            for posv in vendas:
                if vendas[posv][4]=='True':
                  print(f'''Nome do cliente: {vendas[posv][0]} | Nome do produto: {vendas[posv][2]} | Posição: {posv} | Valor da venda: {vendas[posv][3]} | posição da venda {posv} | Status: cadastrada''')
                elif vendas[posv][4]=='False':
                  print(f'''Nome do cliente: {vendas[posv][0]} | Nome do produto: {vendas[posv][2]} | Posição: {posv} | Valor da venda: {vendas[posv][3]} | posição da venda {posv} | Status: excluida''')
            opcoes=int(input('''
        digite 0 para sair
        digite 1 para recadastrar vendas excluidas
        digite 2 para mais informações de vendas
        '''))
        
            if opcoes==1:
                recad=''
                while recad != 'n' and recad != 'N':
                    recad=input('gostaria de re-cadastrar alguma venda excluida? S/N ')
                    if recad=='S' or recad=='s':
                        posv=input('digite a posição da venda:')
                        if posv in vendas and vendas[posv][4]=='True':
                            print('a venda já é cadastrada, escolha uma que foi excluida')
                        if posv in vendas and vendas[posv][4]=='False':
                            vendas[posv][4]='True'
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

arq_produtos= open("produtos.py", "wt", encoding="utf-8")
for posp, dados in produtos.items():
    arq_produtos.write(f"{posp},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]}\n")
arq_produtos.close()

arq_vendas= open("vendas.py", "wt", encoding="utf-8")
for posv, dados in vendas.items():
    arq_vendas.write(f"{posv},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]}\n")
arq_vendas.close()
