def menu():
    loopmenu = 's'
    while loopmenu == 's':
        opcao = input('''
    *************************************
        PROJETO AGENDA EM PYHON
    *************************************
    MENU:

    [1] CADASTRAR CONTATO
    [2] LISTAR CONTATO
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO
    [5] SAIR

    **************************************
    ESCOLHA UMA OPÇÃO:
    ''')

        if opcao =='1':
            cadastroContato()
        elif opcao =='2':
            listaContato()
        elif opcao =='3':
            deleteContato()
        elif opcao =='4':
            buscaConato()
        else:
            sair()
        loopmenu = input('Deseja voltar ao meu principal? {s/n}' )


def cadastroContato():
   nome = input('Digite o nome do contato: ')
   telefone = input('Digite o telefone do contato: ')
   email = input('Digite o e-mail do contato: ')
   try:
    agenda = open('agenda.txt','a')
    dados = f'{nome};{telefone};{email}\n'
    agenda.write(dados)
    agenda.close()
    print(f'Contato gravado com sucesso.')
   except:
    print('ERRO na gravação do contato')

def listaContato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deleteContato():
     nomedel = input('Digite o nome que deseja deletar: ').lower()
     agenda = open('agenda.txt','r')
     aux = []
     aux2 = []
     for i in agenda:
       aux.append(i)
     for i in range (0, len(aux)):
       if nomedel not in aux[i].lower():
         aux2.append(aux[i])
     agenda = open ('agenda.txt','w')
     for i in aux2:
       agenda.write(i)
     print(f'contato deletado com sucesso.\n')

def buscaConato():
    nome = input(f'Digite o nome procurado: ').upper()
    agenda = open('agenda.txt','r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Agenda encerrada')
    exit()

def main():

    menu()

main()