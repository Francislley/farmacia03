from estoque.models import Estoque

class calculacao():

    def __init__(self, nome, produto, venda):
        self._nome_produto = nome
        self._quantidade_produto = produto
        self._quantidade_venda = venda
        


    def calcular_quantidade(self, ):
        
        self.res = self._quantidade_produto - self._quantidade_venda
        if self.res >= 0:
            
            return self.res
        return False


    def calcular_valor(self, preco):
        self._preco = preco
        self.res_preco = self._quantidade_venda * self._preco
        if self.res_preco:
            return self.res_preco
        return False