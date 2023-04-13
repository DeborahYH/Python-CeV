# Crie a função notas(), que recebe várias notas de alunos e retorna um dicionário com as seguintes informações:
# - A quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*notas, status=False):
    """
    Função recebe as notas de uma sala e calcula a média.
    Com base nesta média, é definida a situação desta sala.
    :param notas: notas dos alunos (pode aceitar várias notas)
    :param status: define se a situação da sala avaliada será exibido
    :return: dicionário conténdo informações sobre a sala
    """
    dicionario = {}
    maior = 0
    menor = 0
    media = 0
    situacao = ""

    for nota in notas:
        menor = nota
        if nota < menor:
            menor = nota
        if nota > maior:
            maior = nota

    media = sum(notas)/len(notas)
    if status:
        if media < 5:
            situacao = 'Desfavorável'
        elif media >=5 and media < 7:
            situacao = 'Neutra'
        else:
            situacao = 'Favorável'

    dicionario['total_notas'] = len(notas)
    dicionario['maior_nota'] = maior
    dicionario['menor_nota'] = menor
    dicionario['media_final'] = media
    dicionario['situacao'] = situacao
    return dicionario


help(notas)

sala1 = notas(2, 5, 8, 3)
sala2 = notas(5, 7, 2, 9, 6, 4, status=True)
sala3 = notas(4, 7, 8, 1, 2, status=True)
sala4 = notas(6, 9, 6, 7, status=True)
print(sala1)
print(sala2)
print(sala3)
print(sala4)

