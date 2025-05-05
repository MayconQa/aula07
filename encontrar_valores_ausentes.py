from typing import List
'''
Este código define uma função que encontra os valores ausentes em uma sequência de números inteiros.
A função `encontrar_valores_ausentes` recebe uma lista de inteiros como entrada e retorna uma lista com os valores ausentes na sequência. A função utiliza um conjunto para determinar os valores ausentes, comparando o conjunto completo de números esperados com o conjunto dos números presentes na sequência.
'''

def encontrar_valores_ausentes(sequence: List[int]) -> List[int]:
    completo = set(range(min(sequence), max(sequence) + 1))
    return list(completo - set(sequence))

sequence = [1, 2, 4, 6, 7, 9, 10, 15, 20]
ausentes = encontrar_valores_ausentes(sequence)
print(f'Valores ausentes: {ausentes}')
# Saída: Valores ausentes: [3, 5, 8, 11, 12, 13, 14, 16, 17, 18, 19]    
 