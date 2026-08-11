import csv
#lista dos livros
livros = []
'''função do csv para salvar livros em um arquivo, onde cada linha vai ser um livro e as colunas vao conter as informações
o newline="" serve para não colocar uma linha em branco entre cada livro, e o encoding="utf-8" serve para que os caracteres especiais sejam salvos corretamente
o enconding utf-8 faz uma transcrição exata do que voce esta escrevendo e não vai ter problema com acentos e caracteres especiais, como ç, ã, etc.
'''

def salvar_livros(livros):
    def salvar_livros(livros):

     with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:

        campos = ["titulo", "autor", "ano", "isbn", "status"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(livros)

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
    salvar_livros(livros)
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

def buscar_livro(livros):
    print("\n --- buscar livros ---")
    busca = input("Digite o título ou o autor do livro:  ").lower()
    encontrado = False
    for livro in livros:
        #busca e ve se oq foi escrito tem no nome dos livros ou no dos autores.
        #o .lower serve para considerar a pesquisa maiascula e minuscula, porque tranforma tudo em minusculo
        if busca in livro["titulo"].lower() or busca in livro["autor"].lower():
            print("_______________________")
            print ("Título: ", livro["titulo"])
            print ("Autor: ", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status: ", livro["status"])

            encontrado = True 
    if encontrado == False: 
        print("Nenhum livro foi encontrado.")
    return livros  

# funcao para ordenar todos os livros
def ordenar_livros(livros):
    print("\n ---ORDENAR LIVROS--- ")
    print("1 - por título")
    print("2 - por autor")
    print("3 - por ano")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        #.sort usado para colocar o comando de lista em ordem e o lambda diz qual
        #informação do livro deve ser usada para a ordem 
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("livros ordenados por título.")
    elif opcao == "2":  
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("livros ordenados por autor.")
    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])
        print("livros ordenados por ano.")
    else:
        print("operação invalida.")
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

    elif opcao == "5":
        livros = buscar_livro(livros)    
      
    elif opcao == "6":
        livros = ordenar_livros(livros)  
    else:

        print("Essa opção ainda não existe")
        break 


