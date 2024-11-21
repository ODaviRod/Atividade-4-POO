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
        self.estoque = []  

    def adicionar_produto(self, produto):
        self.estoque.append(produto)

    def exibir_produtos(self):
        if not self.estoque:
            print("Não há produtos no estoque.")
        else:
            for produto in self.estoque:
                print(produto.exibir_detalhes())


def main():
    eletronico = Eletronico(101, "Smartphone", 2500.0, 110)
    calcado = Calcado(201, "Tênis esportivo", 300.0, "Tênis", "Preto", "42", "Borracha", "Tecido sintético", "Espuma")
    roupa = Roupa(301, "Camiseta básica", 50.0, "Camiseta", "Branca", "M", "Algodão")

    loja = Loja()

    loja.adicionar_produto(eletronico)
    loja.adicionar_produto(calcado)
    loja.adicionar_produto(roupa)

    print("Produtos no Estoque:")
    loja.exibir_produtos()

if __name__ == "__main__":
    main()
