def notas(*n, situaçao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param situaçao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situaçao:
        if r['media'] >= 7:
            r['situaçao: BOA!']
        elif r['media'] >= 5:
            r['situaçao: RAZOAVEL']
        else:
            r['situaçao: RUIM!']
    return r
resposta = notas(5.5, 6.9, 7.8, True)
print(resposta)