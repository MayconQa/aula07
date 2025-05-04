
nota1 = int(input('Informe a primeira nota 1: '))
nota2 = int(input('Informe a primeira nota 2: '))
nota3 = int(input('Informe a primeira nota 3: '))
nota4 = int(input('Informe a primeira nota 4: '))

def calcularMedia(n1: int, n2: int, n3: int, n4: int) -> int:
    media = (n1 + n2 + n3 + n4) / 4
    return media

resultadoMedia = calcularMedia(nota1, nota2, nota3, nota4)

print(f'A media é: {resultadoMedia}')
  