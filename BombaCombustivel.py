from Veiculo import veiculo
class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.__tipoCombustivel=tipoCombustivel
        self.__valorLitro=valorLitro
        self.__quantidadeCombustivel=quantidadeCombustivel
    def get_tipoCombustivel(self):
        return self.__tipoCombustivel
    def get_valorLitro(self):
        return self.__valorLitro
    def set_quantidadeCombustivel(self,quantidadeCombustivel):
        self.__quantidadeCombustivel=quantidadeCombustivel
    def get_quantidadeCombustivel(self):
        return self.__quantidadeCombustivel
    def alterarValor(self,valorLitro):
        self.__valorLitro=valorLitro
        print("O valor do litro agora é de {}".format(self.get_valorLitro()))
    def alterarCombustivel(self,tipoCombustivel):
        self.__tipoCombustivel=tipoCombustivel
        print("O combustível é {}".format(self.get_tipoCombustivel()))
    def alterarQuantidadeCombustivel(self,valor,operacao):
        if operacao==1:
            self.set_quantidadeCombustivel(self.get_quantidadeCombustivel()-valor)
        else:
           self.set_quantidadeCombustivel(self.get_quantidadeCombustivel()+valor)
    def abastecerPorValor(self, veiculo):
        valor=int(input("Digite o valor desejado: "))
        resultado=valor/self.get_valorLitro()
        print("A quantidade abastecida foi: {} litros".format(resultado))
        self.alterarQuantidadeCombustivel(resultado, 1)
        veiculo.abastecer(resultado)
    def abastecerPorLitro(self,veiculo):
        valor=int(input("Digite o valor: "))
        resultado=valor*self.get_valorLitro()
        print("O valor a ser pago é de {} reais".format(resultado))
        self.alterarQuantidadeCombustivel(resultado, 1)
        veiculo.abastecer(resultado)
