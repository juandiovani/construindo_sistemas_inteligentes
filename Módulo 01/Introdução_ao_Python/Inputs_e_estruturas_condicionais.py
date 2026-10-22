# Recebendo dados com input()
"""
A funcao input() mostra uma mensagem, espera a pessoa digitar e devolve o texto informado quando ela pressiona ENTER. 
"""
nome = input("Qual e o seu nome? ")
print("Ola",nome)

"""
O texto entre aspas é a pergunta. A resposta é guardada na variável nome.
"""

nome = input("Nome: ")
cidade = input("Cidade: ")

print("=== CADASTRO ===")
print("Nome:", nome)
print("Cidade:", cidade)

"""
input() sempre devolve uma string
Mesmo que a pessoa digite números, o resultado de input() é do tipo str.
"""
idade = input("Digite sua idade: ")
print(idade)
print(type(idade))

"""
O valor guardado é "18", e não o inteiro 18.

Isso muda o significado de algumas operações:
"""

numero1 = input("Primeiro número: ")
numero2 = input("Segundo número: ")
print(numero1 + numero2)

'''
Convertendo entradas para números
Números inteiros com int()
'''

idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)
print("No próximo aniversário você terá", idade + 1, "anos.")

# Também podemos escrever a leitura e a conversão na mesma linha:
idade = int(input("Digite sua idade:"))

# A execução ocorre de dentro para fora:
# input() recebe "18" → int() converte para 18 → idade recebe 18

# Números decimais com float()
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))
total = preco * quantidade 
print("Total da compra:", total)

'''
Digite 19.90, com ponto, para informar um valor decimal.

Informação	Leitura sugerida	Exemplo de entrada
Nome	input()	Marina
Quantidade de livros	int(input())	4
Temperatura	float(input())	23.5
Note

int("dez"), int("2.5") e float("2,5") geram ValueError. Nesta aula, considere que a pessoa digitará números no formato solicitado. O tratamento de entradas não numéricas será estudado depois.

5. Por que um programa precisa tomar decisões?
Até aqui, as instruções eram executadas em sequência. Mas muitas situações dependem de uma condição:

se houver estoque, permitir uma compra;
se a energia acabar, encerrar uma missão;
se a média atingir o mínimo, informar aprovação.
Uma condição é uma expressão que pode ser avaliada como verdadeira ou falsa.

idade = 20

print(idade >= 18)
Saída:

True
Vamos usar esse resultado para escolher quais instruções executar.

6. Operadores de comparação
Operador	Significado	Exemplo	Resultado
==	Igual a	5 == 5	True
!=	Diferente de	5 != 5	False
>	Maior que	8 > 3	True
<	Menor que	8 < 3	False
>=	Maior ou igual a	7 >= 7	True
<=	Menor ou igual a	4 <= 2	False
Compare:

idade = 18          # Atribui um valor.
print(idade == 18)   # Compara o valor e mostra True.
= atribui; == compara.

Também podemos comparar textos:

resposta = input("Deseja continuar? Digite sim ou nao: ")

print(resposta == "sim")
Essa comparação distingue maiúsculas de minúsculas: "sim" é diferente de "Sim". Espaços digitados também fazem parte da entrada. Por enquanto, digite as opções exatamente como forem solicitadas.

7. Uma decisão simples com if
if significa se.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você atingiu a maioridade.")

print("Consulta encerrada.")
Se a condição for verdadeira, o bloco dentro do if será executado. Se for falsa, ele será pulado.

A última mensagem aparece nos dois casos, pois está fora do bloco.

Entrada	Mensagens exibidas após a leitura
18	Você atingiu a maioridade. e Consulta encerrada.
15	Apenas Consulta encerrada.
8. Dois-pontos e indentação
Em Python, a estrutura condicional termina sua primeira linha com :. As instruções pertencentes ao bloco ficam recuadas, normalmente com quatro espaços.

energia = int(input("Energia do robô: "))

if energia < 20:
    print("Energia baixa.")
    print("Procure uma estação de recarga.")

print("Verificação concluída.")
As duas mensagens recuadas pertencem ao if. A última está fora dele.

Tip

Mantenha o mesmo recuo dentro de cada bloco. O editor geralmente indenta a próxima linha automaticamente depois dos dois-pontos. Evite misturar tabulações e espaços.

9. Dois caminhos com if e else
else significa senão. Ele define o que acontece quando a condição do if é falsa.

quantidade = int(input("Quantidade disponível em estoque: "))

if quantidade > 0:
    print("Produto disponível.")
else:
    print("Produto indisponível.")
Neste exemplo, considere uma quantidade não negativa. Apenas um dos dois blocos será executado.

quantidade > 0?
    ├── Verdadeiro → Produto disponível.
    └── Falso      → Produto indisponível.
O else não recebe uma condição: ele cobre o caminho restante.

10. Mais de dois caminhos com elif
elif permite testar outra condição quando as anteriores forem falsas.

media = float(input("Digite a média de 0 a 10: "))

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Em recuperação.")
else:
    print("Reprovado.")
Considere uma média válida entre 0 e 10. A regra deste exemplo é:

Média	Situação
A partir de 7	Aprovado
A partir de 5 e abaixo de 7	Em recuperação
Abaixo de 5	Reprovado
Python testa de cima para baixo. Ao encontrar uma condição verdadeira, executa aquele bloco e pula os demais blocos da mesma cadeia.

Se a média for 8, a condição media >= 5 também seria verdadeira, mas ela nem será avaliada: o primeiro caminho já foi escolhido.

A ordem das condições importa. Se testássemos primeiro media >= 5, uma média 8 seria classificada como recuperação.

11. Vários if ou uma cadeia com elif?
Use if independentes quando mais de uma ação puder acontecer:

temperatura = float(input("Temperatura: "))

if temperatura >= 30:
    print("Dia quente.")

if temperatura >= 35:
    print("Calor intenso.")
Para 36, as duas mensagens aparecem. Cada if faz seu próprio teste.

Use uma cadeia if / elif / else quando quiser escolher apenas um caminho entre as alternativas:

temperatura = float(input("Temperatura: "))

if temperatura >= 35:
    print("Calor intenso.")
elif temperatura >= 30:
    print("Dia quente.")
else:
    print("Temperatura abaixo de 30 graus.")
Para 36, apenas Calor intenso. aparece.

12. Combinando condições com and
and significa e: as duas condições precisam ser verdadeiras.

Uma oficina aceita pessoas a partir de 14 anos, desde que exista vaga:

idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.")
Ter a idade mínima não basta se as vagas acabaram.

13. Alternativas com or
or significa ou: basta que pelo menos uma condição seja verdadeira.

Neste exemplo, estudantes ou professores recebem um desconto:

categoria = input("Categoria (estudante, professor ou visitante): ")

if categoria == "estudante" or categoria == "professor":
    print("Desconto disponível.")
else:
    print("Sem desconto.")
Cada lado do or precisa representar a comparação desejada. Escreva categoria == "professor" por completo.

Condição A	Condição B	A and B	A or B
True	True	True	True
True	False	False	True
False	True	False	True
False	False	False	False
Ao misturar and e or, use parênteses para explicitar o agrupamento desejado:

idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")
14. Invertendo uma condição com not
not significa não. Ele transforma True em False e False em True.

resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")
Neste exemplo, considere somente as respostas sim e nao. A comparação cria um valor booleano, que é guardado em em_manutencao.

Note

Não use bool(input()) para interpretar respostas como sim e nao. Todo texto não vazio, incluindo "nao" e "False", é convertido para True. Compare a resposta com o texto esperado.


'''

# Condicionais dentro de condicinais
'''
Podemos fazer uma segunda decisão dentro da primeira. Isso é chamado de aninhamento
'''
quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado.")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero")
             