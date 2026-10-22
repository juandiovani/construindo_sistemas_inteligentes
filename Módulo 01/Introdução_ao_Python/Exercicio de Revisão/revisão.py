"""
Exercícios de revisão — Introdução ao Python
Data: 08/10/2026
Base: Aula 01 — Introdução ao Python, print() e variáveis.

Orientações
Crie um arquivo .py para cada exercício, utilizando os nomes sugeridos. Escreva os valores diretamente no código e utilize apenas os recursos estudados: variáveis, atribuições, print(), type(), comentários e as operações +, -, * e /.

Utilize nomes de variáveis em snake_case, ponto para os números decimais e True ou False para valores booleanos.

12 — Texto ou cálculo?
Arquivo: 12_texto_ou_calculo.py

Antes de executar, escreva em comentários o que acredita que cada linha mostrará:

print("12 + 3")
print(12 + 3)
print("Resultado:", 12 + 3)
print("12", "3")
Depois execute e compare suas previsões com a saída. Explique em um comentário por que as duas primeiras linhas produzem resultados diferentes.

13 — Cadastro de uma oficina
Arquivo: 13_cadastro_oficina.py

Uma escola oferece uma oficina de robótica. Crie variáveis para armazenar:

nome da oficina: "Robótica para iniciantes";
sala: "Laboratório 2";
quantidade de vagas: 24;
duração em horas: 2.5;
inscrições abertas: True.
Mostre uma ficha com um título e uma informação por linha. Em seguida, mostre o tipo de cada variável com type() e escreva comentários explicando o que str, int, float e bool representam nesse cadastro.

14 — Dividindo a conta
Arquivo: 14_dividindo_conta.py

Quatro amigos compraram uma pizza de R$ 48.00 e uma bebida de R$ 12.00. A conta será dividida igualmente.

Crie variáveis para o preço da pizza, o preço da bebida e a quantidade de amigos.
Calcule o total da conta em uma nova variável.
Calcule quanto cada amigo deverá pagar.
Mostre o total e o valor por pessoa com descrições.
Use type() para mostrar o tipo do valor por pessoa.
Para pensar: o resultado da divisão é um int ou um float, mesmo quando não há centavos?

15 — Estoque da biblioteca
Arquivo: 15_estoque_biblioteca.py

A biblioteca começa o dia com 40 livros disponíveis. Nesta ordem:

recebe 12 livros novos;
empresta 9 livros;
recebe a devolução de 4 livros;
empresta mais 6 livros.
Crie uma variável livros_disponiveis e atualize essa mesma variável após cada acontecimento. Mostre a quantidade inicial e a quantidade após cada atualização, identificando a etapa.

Antes de executar, anote em comentários suas previsões para cada etapa. Compare com o resultado do programa.

16 — Boletim de notas
Arquivo: 16_boletim_notas.py

Um aluno recebeu as notas 7.5, 8.0 e 9.5 em três atividades de mesmo peso.

Guarde o nome do aluno e cada nota em variáveis separadas.
Calcule a soma das notas em uma variável soma_notas.
Calcule a média dividindo a soma pela quantidade de atividades.
Mostre o nome, as três notas e a média.
Troque apenas a segunda nota por 6.5 no código e execute novamente.
O programa deve recalcular a média a partir das variáveis. Não escreva a média pronta no código. Não é necessário informar aprovação ou reprovação.

17 — Oficina de correção
Arquivo: 17_corrigindo_codigo.py

O programa abaixo deveria mostrar o nome de um curso, o valor da mensalidade e se a matrícula está ativa, mas contém erros:

nome curso = "Python básico"
mensalidade = 89,90
matricula_ativa = true

print("Curso:", nome_curso)
print("Mensalidade:", Mensalidade)
print("Matrícula ativa:", matricula_ativa)
Reescreva o código corrigindo:

o nome da variável que contém um espaço;
a escrita do número decimal;
a escrita do valor booleano;
a diferença entre maiúsculas e minúsculas no nome da variável.
Para cada correção, escreva um comentário explicando a regra da aula que foi aplicada. Ao final, mostre também type(mensalidade) para verificar se o valor é um float.

18 — Guardando o valor anterior
Arquivo: 18_valor_anterior.py

Leia o programa sem executá-lo:

saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)
Anote em comentários os valores que serão mostrados.
Execute o código para conferir.
Explique por que saldo_anterior mantém o valor que recebeu na atribuição, mesmo depois das mudanças em saldo.
Acrescente uma despesa de 15 ao saldo atual e mostre novamente as duas variáveis.
19 — Orçamento do passeio
Arquivo: 19_orcamento_passeio.py

Uma turma com 20 alunos fará um passeio. O ônibus custa R$ 600.00 para toda a turma. Cada ingresso custa R$ 15.00 e cada lanche custa R$ 10.00 por aluno.

Crie variáveis para os dados e calcule, em variáveis separadas:

o custo de todos os ingressos;
o custo de todos os lanches;
o custo total do passeio, incluindo o ônibus uma única vez;
o valor que cada aluno deverá pagar, dividindo o custo total igualmente.
Mostre um relatório com a quantidade de alunos e todos os custos. Depois altere a quantidade de alunos para 25 e execute novamente sem modificar as fórmulas.

Para pensar: por que o custo total aumenta, mas o valor por aluno diminui?

20 — Uma variável, diferentes tipos
Arquivo: 20_mudando_tipos.py

Crie uma variável chamada informacao. Ela deverá receber, nesta ordem:

o texto "42";
o número inteiro 42;
o número decimal 42.0;
o valor booleano False.
Após cada atribuição, mostre o valor e o resultado de type(informacao).

Escreva um comentário explicando a diferença entre "42" e 42. Ao final, explique se a variável guarda os quatro valores ao mesmo tempo ou apenas o último valor atribuído.
"""