class Produto:
    def __init__(self, codigo: int, descricao: str, valor: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    def exibir_detalhes(self):
        return "Código: {}, Descrição: {}, Valor: R${:.2f}".format(self.codigo, self.descricao, self.valor)

class Eletronico(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, voltagem: int):
        super().__init__(codigo, descricao, valor)
        self.voltagem = voltagem

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Voltagem: {}V".format(self.voltagem)

class Vestuario(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str):
        super().__init__(codigo, descricao, valor)
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Nome: {}, Cor: {}, Tamanho: {}".format(self.nome, self.cor, self.tamanho)

class Calcado(Vestuario):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str, 
                 materialsola: str, materialpartesuperior: str, materialinterno: str):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.materialsola = materialsola
        self.materialpartesuperior = materialpartesuperior
        self.materialinterno = materialinterno

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Material da Sola: {}, Material Parte Superior: {}, Material Interno: {}".format(
            self.materialsola, self.materialpartesuperior, self.materialinterno
        )

class Roupa(Vestuario):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str, tecido: str):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.tecido = tecido

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Tecido: {}".format(self.tecido)


# Classe Loja
class Loja:
    def __init__(self):
        self.numero_venda = 1 
        self.total_venda = 0  

    def vender_produto(self, produto, quantidade):
        valor_venda = produto.valor * quantidade
        self.total_venda += valor_venda  

    def imprimir_recibo(self):
        print(f"Venda Número: {self.numero_venda}")
        print(f"Total de Vendas: R${self.total_venda:.2f}")
        
        self.numero_venda += 1
        self.total_venda = 0

eletronico = Eletronico(101, "Smartphone", 2500.0, 110)

calcado = Calcado(201, "Tênis esportivo", 300.0, "Tênis", "Preto", "42", "Borracha", "Tecido sintético", "Espuma")

roupa = Roupa(301, "Camiseta básica", 50.0, "Camiseta", "Branca", "M", "Algodão")

loja = Loja()

loja.vender_produto(eletronico, 2)  
loja.vender_produto(calcado, 3) 
loja.vender_produto(roupa, 5)  

loja.imprimir_recibo()

loja.vender_produto(eletronico, 1)
loja.vender_produto(calcado, 2)  

loja.imprimir_recibo()
