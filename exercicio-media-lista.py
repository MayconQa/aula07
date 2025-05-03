from typing import List

valores = [9,4,5,6,8]

def calcularMediaLista(valores: List[float]) -> float:
'''
Recebe uma lista de valores, calcula a média e imprime 
com duas casas decimais. Ótimo uso de List[float] do módulo 
typing e da função sum().
'''
    return sum(valores) / len(valores)

media = calcularMediaLista(valores)
print(f"A média é: {media:.2f}")