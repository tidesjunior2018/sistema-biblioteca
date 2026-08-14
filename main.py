import json
from colorama import Fore,Style,init
from datetime import datetime
#ligue as cores e depois volte ao normal
init(autoreset=True)

#Sistema de biblioteca

ARQUIVO="biblioteca.json"

#===============================ARQUIVO==========================
def carregar_dados():
    try:
        #abre o arquivo e le os dados que estão nele(formato json)
        with open(ARQUIVO,"r",encoding="utf-8") as f:
            return json.load(f)
    
    #se der erro,nao consegue abrir o arquivo e retorna a lista vazia
    except:
        return[]

def salvar_dados(biblioteca):

    with open(ARQUIVO,"w",encoding="utf-8") as f:
            #salva os dados da variavel biblioteca dentro de um arquivo f, com identaçao e mantem os acentos.
            json.dump(biblioteca,f,indent=4,ensure_ascii=False)

biblioteca=carregar_dados()

#===============================VALIDAÇÕES========================

def validar_nome(nome):
    #verfica se a variavel nome não está vazia(nem so com os espaços)
    # pergunta: o mome tem texto de verdade ou está vazio? 
    return nome.strip()!=""

def validar_ano(ano):
    #ano.isdigit()=verifica se o ano só tem numeros
    #0 < int(ano) <= datetime.now().year = converte o ano para numero inteiro e verifica:
    #se maior que 0
    #e é menor que ano atual
    return ano.isdigit() and 0 < int(ano) <= datetime.now().year

def validar_data(data,ano):
    formatos=[
        "%d/%m/%Y",#26/07/2025
        "%d %m/%Y"#26 07/2025
    ]
    # juntar a data e o ano
    data_completa=f"{data}/{ano}"

    for formato in formatos:
        try:
            # datetime.strptime()=transforma o texto em um data de verdade
            data_publicacao=datetime.strptime(data_completa,formato)
            # nao permite datas futuras
            if data_publicacao>datetime.now():
                return False
            return True
        except ValueError:
            pass
    return False

def livro_existe(nome):

    #verifica se ja existe um livro com esse nome ignorando maiscula e minuscula
    return any(livro["nome"].strip().lower() == nome.strip().lower() for livro in biblioteca)

#==================================FUNÇÕES==================================================
def cadastrar_livro():
    print(Fore.CYAN + "\n=== CADASTRAR LIVRO ===")

    nome = input("Digite o nome do livro: ")

    while not validar_nome(nome):
            print(Fore.RED + "Nome não pode ser vazio.\n")
            nome = input("digite o nome do livro novamente:")

    if livro_existe(nome):
            print(Fore.YELLOW + "Livro ja cadastrado.\n")
            return

    #data
    data= input("Digite a data e o mês que publicado o livro: ")
    #ano
    ano=input("Digite o ano que o livro foi publicado:")
    #valida o ano
    while not validar_ano(ano):
            print(Fore.RED + "Ano inválido.\n")
            ano = input("Digite o ano novamente: ")
    #valida a data +ano
    while not validar_data(data,ano):
        print(Fore.RED + "Data inválida ou maior que a data de hoje.\n")
        data = input("Digite a data no formato dd/mm:")
        ano = input("Digite o ano novamente:")

    
    livro={
        "nome": nome,
        "data": data,
        "ano": ano
    }

    biblioteca.append(livro)
    salvar_dados(biblioteca)

    print(Fore.GREEN + "✔ Livro cadrastado com sucesso!.\n")


def listagem_de_livros():
    print(Fore.CYAN + "\n ===LISTAGEM DE LIVROS=== ")
    if not biblioteca:
        print(Fore.YELLOW + " Nenhum livro cadastrado.\n")
        return
    for i,livro in enumerate(biblioteca):
        print(Fore.WHITE +f"{i+1}.{livro['nome']}-{livro['data']}-{livro['ano']}")
    print()

def pesquisar_livro():
    print(Fore.CYAN + "\n ===PESQUISAR LIVRO===")
    
    nome=input("Digite o nome do livro para pesquisar:")

    encontrados=[livro for livro in biblioteca if nome.lower() in livro["nome"].lower()]
    
    if encontrados:
        print(Fore.GREEN + "\nLivros encontrados:")
        for livro in encontrados:
            print(Fore.WHITE + f"{livro['nome']}-{livro['data']}-{livro['ano']}")
    else:
        print(Fore.RED + "✘ Livro não encontrado")
    print()

def quantidade_livros():
    print(Fore.BLUE + f"Quantidade total de livros:{len(biblioteca)}\n")

def excluir_livro():
    print(Fore.CYAN + "\n===EXCLUIR LIVRO")
    listagem_de_livros()
    #se a biblioteca estiver vazia,nada mais e executado depois disso.
    if not biblioteca:
        return
    
    try:
        indice=int(input("Digite o número do livro para excluir:"))-1
        if 0<=indice<len(biblioteca):
            confirmacao=input(Fore.YELLOW+"Tem certeza que deseja excluir ? (s/n): ").lower()

            if confirmacao=="s":
                #o .pop apaga o livro da lista biblioteca
                removido=biblioteca.pop(indice)
                salvar_dados(biblioteca)
                print(Fore.GREEN+f"✔ '{removido['nome']}' removido com sucesso!\n ")
            else:
                print(Fore.YELLOW+"operação cancelada.\n")
        else:
            print(Fore.RED + "índice inválido\n")
    except ValueError:
        print(Fore.RED + "Digite o número válido\n")

def excluir_todos_os_livros():
    print(Fore.CYAN+"\n===EXCLUIR TODOS OS LIVROS===")

    if not biblioteca:
        print(Fore.YELLOW+"Não existem livros cadastrados")
        return

    #mostra todos os livros antes de excluir
    listagem_de_livros()
    
    print(Fore.RED+f"Você está prestes a excluir {len(biblioteca)} livro(s).")

    confirmacao=input(Fore.YELLOW+"Tem certeza que deseja excluir todos os livros?(s/n):").lower()

    if confirmacao=="s":
        #.clear()=ela limpa a lista que já existe
        biblioteca.clear()
        #e depois salva a a lista vazia na biblioteca,ai quando voce fecha e abre programa novamente os livros
        #continua excluido
        salvar_dados(biblioteca)

        print(Fore.GREEN+"✔ Todos os livros foram excluídos com sucesso!\n")
    else:
        print(Fore.YELLOW+"Operação cancelada.\n")

#========================================MENU============================================================
def menu():
    while True:
        print(Fore.MAGENTA + Style.BRIGHT +"===Sistema de Biblioteca===")
        print(Fore.YELLOW +"1 - Cadastrar Livro")
        print(Fore.YELLOW +"3 - Pesquisar livro")
        print(Fore.YELLOW +"4 - Quantidade de livros")
        print(Fore.YELLOW +"5 - Excluir livro")
        print(Fore.YELLOW +"6 - Excluir todos os livros")
        print(Fore.YELLOW +"0 - Sair")

        opcao=input(Fore.WHITE + "Escolha uma opção: ")

        if opcao=="1":
            cadastrar_livro()
        elif opcao=="2":
            listagem_de_livros()
        elif opcao=="3":
            pesquisar_livro()
        elif opcao=="4":
            quantidade_livros()
        elif opcao=="5":
            excluir_livro()
        elif opcao=="6":
            excluir_todos_os_livros()
        elif opcao=="0":
            print("Saindo do sistema....")
            break
        else:
            print("Opção inválida \n")

#executar o sistema
menu()