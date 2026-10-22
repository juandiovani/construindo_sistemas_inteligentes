# Criando variáveis 
nome = "Juan"
idade = 18
# Temos: nome  → "Arthur", idade → 18
print(nome)
print(idade)
 # Essa é uma observação importante para quem está começando.Em matemática:x = 10normalmente significa:x é igual a 10.Em programação podemos pensar:coloque o valor 10 dentro da variável x.Então:x = 10 é uma atribuição.Podemos visualizar:10x.

"""
Essa é uma observação importante para quem está começando.Em matemática:x = 10normalmente significa:x é igual a 10.Em programação podemos pensar:coloque o valor 10 dentro da variável x.Então:x = 10 é uma atribuição.Podemos visualizar:10 x

"""


# Usando variáveis dentro do print()
# Podemos imprimir vários valores 
nome = "Juan"
idade = 17
curso = "Programação"

print("Nome", nome)
print("Idade", idade) # ou podemos usar esse também:
print(nome,idade,curso)

# Tipos de dados
"""
Variáveis podem armazenar diferentes tipos de informação.

Inicialmente trabalharemos principalmente com quatro.

Texto — str
"""

nome = "Naruto"
"""
str vem de string.

Representa texto.

Número inteiro — int
"""
nivel = 10

# exemplos 
idade = 18
quantidade = 50
vidas = 3

# Número decimal - float
altura = 1.75
preco = 29.90
temperatura = 24.5
nota = 8.7

# Booleano - bool, representa verdadeiro ou falso
jogo_ativo = True # ou
jogo_ativo = False

# Nomes de variáveis 
"""
Utilize nomes que expliquem o que a variável representa.

Evite:

x = 150
y = 3
z = x * y

preco = 150
quantidade = 3
total = preco * quantidade
O computador entende os dois.

Quem agradece pelo segundo código é o ser humano que precisar lê-lo depois. 😅

"""
# Algumas regras 
"""
Podemos utilizar:

nome
idade
nome_aluno
nota_final
quantidade_produtos
Não podemos iniciar o nome com número:

2nota = 10
Isso é inválido.

Prefira:

nota2 = 10
Também não utilizamos espaços:

nome aluno = "Carlos"
Errado.

Use:

nome_aluno = "Carlos"
Essa forma é chamada de snake_case.

Coincidentemente bastante apropriada para Python. 🐍

"""
# Python diferencia maiúsculas de minúsculas

"""
Observe:

nome = "Ana"
Nome = "Carlos"
São duas variáveis diferentes.

Python é case-sensitive.

Portanto:

nome
Nome
NOME
podem representar três variáveis diferentes.

Por padrão, prefira nomes minúsculos:

nome_aluno
nota_final
quantidade

"""