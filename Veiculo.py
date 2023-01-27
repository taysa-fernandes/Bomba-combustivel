class veiculo:
    def __init__(self,tipoVeiculo,quantidadeCombustivel):
        self.__tipoVeiculo=tipoVeiculo
        self.__quantidadeCombustivel=quantidadeCombustivel
    def get_tipoVeiculo(self):
        return self.__tipoVeiculo
    def set_tipoVeiculo(self,tipoVeiculo):
        self.__tipoVeiculo=tipoVeiculo
    def get_quantidadeCombustivel(self):
        return self.__quantidadeCombustivel
    def set_quantidadeCombustivel(self, quantidadeCombustivel):
        self.__quantidadeCombustivel=quantidadeCombustivel
    def abastecer(self,valor):
        self.set_quantidadeCombustivel(self.get_quantidadeCombustivel()+valor)


