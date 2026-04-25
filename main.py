from colorama import Fore,Style,init

#ligue as cores e depois volte ao normal
init(autoreset=True)

#Sistema de biblioteca

biblioteca=[]

def cadastrar_livro():
    print(Fore.CYAN + "\n=== CADASTRAR LIVRO ===")
    nome=input("Digite o nome do livro:")
    data=input("Digite a data e o mes:(dd/mm)")
    ano=input("Digite o ano:")

    livro={
        "nome":nome,
        "data":data,
        "ano":ano
    }

    biblioteca.append(livro)
    print(Fore.GREEN + "✔ Livro cadastrado com sucesso!\n")


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
            #remove o livro a partir do indice
            removido=biblioteca.pop(indice)
            print(Fore.GREEN + f"✔ Livro '{removido['nome']}'removido com sucesso!\n")
        else:
            print(Fore.RED + "índice inválido\n")
    except ValueError:
        print(Fore.RED + "Digite o número válido\n")

def menu():
    while True:
        print(Fore.MAGENTA + Style.BRIGHT +"===Sistema de Biblioteca===")
        print(Fore.YELLOW +"1 - Cadastrar Livro")
        print(Fore.YELLOW +"2-  Listagem de livros")
        print(Fore.YELLOW +"3 - Pesquisar livros")
        print(Fore.YELLOW +"4 - Quantidade de livros")
        print(Fore.YELLOW +"5 - Excluir Livro")
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