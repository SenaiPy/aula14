class Produto:
    #Atributos
    nome:str
    preco:float
    saldo:int  #saldo é na verdade a quantidade em estoque

    #Construtor
    def __init__(self, nome:str, preco:float, saldo:int): #dois underline antes e depois do init
        self.nome = nome  #self.nome = objetos da classe Produto | nome = parâmetro da função init
        self.preco = preco
        self.saldo = saldo


    #Metodos
    def valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    def adicionarProdutos(self, quantidade) -> int:
        self.saldo = self.saldo + quantidade
        return self.saldo
    def removerProdutos(self, quantidade) -> int:
        self.saldo = self.saldo - quantidade
        return self.saldo
    def dadosDoProduto(self) -> str:
        saida = f'''
                Dados do produto:
                \tNome do produto: {self.nome}
                \tValor de compra do produto: R$ {self.preco}
                \tQuantidade em estoque: {self.saldo}
                \tValor total em estoque: R$ {self.valorTotalEmEstoque():.2f}
                '''
        return saida