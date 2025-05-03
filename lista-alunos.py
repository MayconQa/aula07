

alunos = ['Maycon  ', 'aNDRESSA', 'murilo',  'Nala  ', 'Mauricio', 'neMO   ']

def tratarTexto(texto):
    '''
    Função que recebe um texto e retorna o texto em letras maiúsculas, sem espaços no início e no final.
    '''
    texto = texto.upper()
    texto = texto.strip()
    return texto


# exemplo 1
texto = 'Maycon'

texto = tratarTexto(texto)
print(f'Exemplo 1: {texto}')

# exemplo 2
for aluno in alunos:
    aluno = tratarTexto(aluno)
    print(f'Exemplo 2: {aluno}')
