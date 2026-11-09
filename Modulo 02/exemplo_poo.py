class Produto:
    def __init__(self,nome, preco, estoque):
         self.nome = nome
         self.preco = preco
         self.estoque = estoque

    def resumo(self):
         print(f"Nome do produto: {self.nome}")
         print(f"Preço: R$ {self.preco}")
         print(f"Qtd. Estoque: {self.estoque}")
produto_5 = Produto("PS4 fat com 8 jogos", 2200.00, 10)         


produto_1 = Produto("Caderno", 12.0, 5)
produto_2 = Produto("Caneta", 3.0, 10)
produto_3 = Produto(8, "Folha", 6.0)
produto_7 = Produto("CR7", 7.0, 680)
produto_4 = Produto("God of War PS4", 120.0, 1)



print("Nome do produto", produto_1.nome)
print("Nome do produto", produto_2.nome)
print("Nome do produto", produto_3.nome)

print(f"Nome do produto: {produto_7.nome}")
print(f"Nome do produto: {produto_4.nome}")
