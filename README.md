# biblioteca-de-livros

O projeto se chama "biblioteca-de-livros", onde cria-se uma biblioteca funcional com base nas informações do livro, contendo especialidades como: cadastrar, listar, buscar, ordenar, emprestar e devolver os livros. O projeto é organizado com funções, tendo cada função representante por cada especialidade principal do programa, ex: `cadastrar_livro()`.

Os livros ficam salvos em um arquivo `livros.csv`, então os dados não são perdidos quando o programa é fechado.

Ele permite que os dados sejam recuperados quando o programa for executado novamente, há duas funções responsaveis pelo livros.csv:

`def salvar_livros(livros)`
`def carregar_livros()`

## Como executar

Para executar, abra a pasta do projeto no terminal e use:

`python main.py`

Depois é só escolher uma das opções do menu.

As opções citadas acima e para escolher cada uma você digita um número:

1. Cadastro
2. Emprestar livros
3. Devolver livros
4. Listar livros
5. Buscar por título ou autor
6. Ordenar por título, autor ou ano
7. Fechar o programa

## Lista de requisitos técnicos aplicados

* **Menu com if, elif e else** — usado no menu principal para escolher as funções do sistema.

* **while** — usado para manter o menu funcionando até o usuário escolher a opção de sair.

* **Funções com parâmetros e retorno** — usadas nas funções de cadastro, listagem, empréstimo, devolução, busca e ordenação.

* **Lista de dicionários** — a lista `livros` armazena os livros, e cada livro é um dicionário com suas informações.

* **Persistência em arquivo** — as funções `salvar_livros()` e `carregar_livros()` salvam e recuperam os dados do arquivo `livros.csv`.

* **Biblioteca padrão do Python** — foi utilizado o módulo `csv`, sem instalação de pacotes externos.

* **Estruturas de repetição for** — usadas para percorrer os livros durante a listagem, busca, empréstimo e devolução.

* **.sort() e lambda** — usados na função `ordenar_livros()` para ordenar por título, autor ou ano.

* try e except — usados na função `carregar_livros()` para tratar o caso em que o arquivo `livros.csv` ainda não existe.

* .lower() — usado na função de busca para não diferenciar letras maiúsculas e minúsculas.
