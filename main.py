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

    else:

        print("Essa opção ainda não existe")
