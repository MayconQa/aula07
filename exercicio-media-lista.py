from typing import List

valores = [9,4,5,6,8]


def calcularMediaLista(valores: List[float]) -> float:
    return sum(valores) / len(valores)

media = calcularMediaLista(valores)
print(f"A média é: {media:.2f}")