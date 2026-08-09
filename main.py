# lista dos livros
livros = []


# função para cadastrar um livro
def cadastrar_livro(livros):

    print("\n  CADASTRAR LIVRO ")

    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano: ")
    isbn = input("Digite o ISBN: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append(livro)
    print("Livro cadastrado.")
    return livros

#essa função vai mostrar os livros cadastrados 
def listar_livros(livros):
    print("\n----LIVROS CADASTRADOS----")
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        #agr percorremos todos os livros
        for livro in livros:
            print("-------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"] )
            print ("ISBN:", livro["isbn"])
            print("status:", livro["status"])
        return livros





# Função para emprestar um livro
def emprestar_livro(livros):

    print("\n----EMPRESTAR LIVRO----")

    isbn = input("Digite o ISBN do livro: ")

    # Procura o livro pelo ISBN
    for livro in livros:

        if livro["isbn"] == isbn:

            # Verifica se ele já está emprestado
            if livro["status"] == "emprestado":
                print("Esse livro já está emprestado.")

            else:
                # Muda o status do livro
                livro["status"] = "emprestado"

                print("Livro emprestado com sucesso!")

            return livros

    print("Livro não encontrado.")

    return livros
    
def devolver_livro(livros):
    print("\n ---DEVOLVER LIVRO--- ")
    isbn = input("Digite o ISBN do livro: ")
    #identificação de qual é o livro
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro ["status"] == "disponível":
                print("Esse livro não foi emprestado e está disponível.")
            else:
                livro["status"] = "disponível"
                print ("Livro devolvido com sucesso.")
            return livros
    print("livro não encontrado.")
    return livros



# aqui é feito o menu da biblioteca
while True:

    print("\n BIBLIOTECA  ")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        livros = cadastrar_livro(livros)

    elif opcao == "7":

        print("Programa encerrado ")
        break
        
    elif opcao == "2":
        livros = emprestar_livro(livros)
        
    elif opcao == "4":
        livros = listar_livros(livros)    

    elif opcao == "3":
        livros = devolver_livro(livros)    
      
    else:

        print("Essa opção ainda não existe")
        break 
