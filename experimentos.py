import random
from arvores import comparar_detalhado


def imprimir(linhas):
    print(f"{'Arvore':<14}{'Altura':>8}{'Rotacoes':>10}{'Recolor.':>10}{'Verific.':>10}")
    for nome, altura, rotacoes, recolor, verif in linhas:
        print(f"{nome:<14}{altura:>8}{rotacoes:>10}{recolor:>10}{verif:>10}")


def aleatorio(n, tentativas, semente=42):
    sorteio = random.Random(semente)
    acumulado = {}
    for _ in range(tentativas):
        sequencia = sorteio.sample(range(10 * n), n)
        for nome, altura, rotacoes, _, verif in comparar_detalhado(sequencia):
            dados = acumulado.setdefault(nome, {"h": [], "rot": [], "ver": []})
            dados["h"].append(altura)
            dados["rot"].append(rotacoes)
            dados["ver"].append(verif)
    linhas = []
    for nome, d in acumulado.items():
        linhas.append((
            nome,
            sum(d["h"]) / tentativas,
            max(d["h"]),
            sum(d["rot"]) / tentativas / n,
            sum(d["ver"]) / tentativas / n,
        ))
    return linhas


def imprimir_aleatorio(n, tentativas):
    print(f"\n{n} chaves em ordem aleatoria ({tentativas} sorteios):")
    print(f"{'Arvore':<14}{'Alt.media':>10}{'Alt.max':>9}{'Rot/ins':>9}{'Verif/ins':>11}")
    for nome, media, maximo, rot, ver in aleatorio(n, tentativas):
        print(f"{nome:<14}{media:>10.2f}{maximo:>9}{rot:>9.3f}{ver:>11.2f}")
