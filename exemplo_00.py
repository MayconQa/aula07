
valor_1 = 25
valor_2 = 9
valor_3 = 7
valor_4 = 3

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma função simple que soma os números do tipo float que rertorna float
    """
    resultado_soma = valor_1_para_somar * valor_2_para_somar
    return resultado_soma

valor_10 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
print(valor_10)

def subtracao(valor_number_one: float, valor_number_dow: float) -> float:
    resultado_sub = valor_1 - valor_2
    return resultado_sub

resultado = subtracao(valor_number_one=valor_1, valor_number_dow=valor_2)
print(resultado)
