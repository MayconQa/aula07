
def Calcular_Desvio_Padrão_Lista(lista:list) -> float:
    """
    Função para calcular o desvio padrão de uma lista de números.
    
    Parâmetros:
    lista (list): Lista de números.
    
    Retorna:
    float: Desvio padrão da lista.
    """
    n = len(lista)
    if n == 0:
        return 0.0
    
    media = sum(lista) / n
    soma_quadrados = sum((x - media) ** 2 for x in lista)
    
    desvio_padrao = (soma_quadrados / n) ** 0.5
    return desvio_padrao

lista = [10, 12, 23, 23, 16, 23, 21, 16]
resultado = Calcular_Desvio_Padrão_Lista(lista)
print(f"Desfio Padrão: {resultado:.2f}") 
