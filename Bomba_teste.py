from BombaCombustivel import BombaCombustivel
from Veiculo import veiculo
bomba1=BombaCombustivel("Gasolina",9.50,2000)
veiculo1=veiculo("Carro",300)
bomba1.abastecerPorLitro(veiculo1)
print("Bomba: {}".format(bomba1.get_quantidadeCombustivel()))
print("veiculo: {}".format(veiculo1.get_quantidadeCombustivel()))
bomba1.abastecerPorValor(veiculo1)
print(bomba1.get_quantidadeCombustivel())
print("veiculo: {}".format(veiculo1.get_quantidadeCombustivel()))
bomba1.alterarQuantidadeCombustivel(2,2)
print(bomba1.get_quantidadeCombustivel())
bomba1.alterarCombustivel("álcool")
bomba1.get_tipoCombustivel()
bomba1.alterarValor(10)
bomba1.get_valorLitro()

