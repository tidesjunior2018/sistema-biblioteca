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

def validar_data(data):
    #verifica se a foi digitada no formato correto
    # 25/12 ou 07/03 ou 25 12 ou 07 03
    formatos=["%d%m","%d %m"]

    for formato in formatos:
        try:#deu certo
            #essa linha pega o texto que está em data e tenta transformar em uma data,seguindo no formato dia/mês
            #datetime=ferramenta do python para trabalhar com datas
            #.strptime()=lê um texto e tenta entender como data
            datetime.strptime(data,formato)
            return True
        except ValueError:#captura o erro de valor inválido
            pass #ignora esse erro e continua o programa
    return False
    
def livro_existe(nome):

    #verifica se ja existe um livro com esse nome ignorando maiscula e minuscula
    return any(livro["nome"].strip().lower() == nome.strip().lower() for livro in biblioteca)

#==================================FUNÇÕES==================================================
def cadastrar_livro():
    print(Fore.CYAN + "\n=== CADASTRAR LIVRO ===")

    nome = input("Digite o nome do livro: ")

    if not validar_nome(nome):
        print(Fore.RED + "Nome não pode ser vazio.\n")
        nome = input("digite o nome do livro novamente:")
    
    if livro_existe(nome):
        print(Fore.YELLOW + "Livro ja cadastrado.\n")
        return

    data= input("Digite a data e o mês que publicado o livro: ")

    while not validar_data(data):
        print(Fore.RED + "Data inválida.Use o formato dd/mm.\n")
        data = input("Digite a data no formato dd/mm:")

    ano=input("Digite o ano que o livro foi publicado:")

    while not validar_ano(ano):
        print(Fore.RED + "Ano inválido.\n")
        ano = input("Digite o ano novamente: ")
    
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

#========================================MENU============================================================
def menu():
    while True:
        print(Fore.MAGENTA + Style.BRIGHT +"===Sistema de Biblioteca===")
        print(Fore.YELLOW +"1 - Cadastrar Livro")
        print(Fore.YELLOW +"2 - Listar Livros")
        print(Fore.YELLOW +"3 - Pesquisar livro")
        print(Fore.YELLOW +"4 - Quantidade de livros")
        print(Fore.YELLOW +"5 - Excluir livro")
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
        elif opcao=="0":
            print("Saindo do sistema....")
            break
        else:
            print("Opção inválida \n")

#executar o sistema
menu()