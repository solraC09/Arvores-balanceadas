import webbrowser
from html import escape
from importlib import import_module
from pathlib import Path
from arvores import ArvoreAVL, ArvoreRubroNegra, RED

TITULOS = {
    1: "Catálogo de produtos da loja",
    2: "Log de eventos do app Mumbuca",
    3: "Tabela de símbolos de um compilador",
    4: "Índice de sessões ativas",
    5: "Importação de cadastro já ordenado",
    6: "Fila de processos do escalonador",
}

RESPOSTAS = {1: "AVL", 2: "Rubro-Negra", 3: "AVL", 4: "Rubro-Negra", 5: "AVL", 6: "Rubro-Negra"}

DX, DY, RAIO, MARGEM = 44, 66, 17, 30


def posicionar(no, vazio, profundidade, contador, pontos):
    if no is None or no is vazio:
        return
    posicionar(no.esq, vazio, profundidade + 1, contador, pontos)
    pontos[id(no)] = (MARGEM + contador[0] * DX, MARGEM + profundidade * DY, no)
    contador[0] += 1
    posicionar(no.dir, vazio, profundidade + 1, contador, pontos)


def svg_arvore(raiz, vazio, estilo):
    pontos = {}
    posicionar(raiz, vazio, 0, [0], pontos)
    largura = 2 * MARGEM + (len(pontos) - 1) * DX
    altura = 2 * MARGEM + (max(y for _, y, _ in pontos.values()) - MARGEM) + 14
    linhas, nos = [], []
    for x, y, no in pontos.values():
        for filho in (no.esq, no.dir):
            if filho is not None and filho is not vazio:
                fx, fy, _ = pontos[id(filho)]
                linhas.append(f'<line x1="{x}" y1="{y}" x2="{fx}" y2="{fy}" class="aresta"/>')
        if estilo == "avl":
            cor, extra = "no-avl", f'<text x="{x}" y="{y + RAIO + 13}" class="rotulo-h">h{no.altura}</text>'
        else:
            cor, extra = ("no-rubro" if no.cor == RED else "no-negro"), ""
        nos.append(
            f'<circle cx="{x}" cy="{y}" r="{RAIO}" class="{cor}"/>'
            f'<text x="{x}" y="{y + 4}" class="chave">{no.chave}</text>{extra}'
        )
    return (
        f'<svg viewBox="0 0 {largura} {altura}" width="{largura}" height="{altura}" '
        f'role="img">{"".join(linhas)}{"".join(nos)}</svg>'
    )


def secao(numero):
    sequencia = list(import_module(f"questao{numero}").SEQUENCIA)
    avl, rn = ArvoreAVL(), ArvoreRubroNegra()
    for chave in sequencia:
        avl.inserir(chave)
        rn.inserir(chave)
    return f"""
<section>
  <h2>Questão {numero} — {escape(TITULOS[numero])}
    <span class="resposta">Resposta: {RESPOSTAS[numero]}</span></h2>
  <p class="sequencia">Sequência inserida: {", ".join(map(str, sequencia))}</p>
  <div class="par">
    <figure>
      <figcaption><strong>AVL</strong> · altura {avl.altura()} · {avl.rotacoes} rotações
        <br><small>número no círculo = chave; hN = altura do nó</small></figcaption>
      <div class="rolagem">{svg_arvore(avl.raiz, None, "avl")}</div>
    </figure>
    <figure>
      <figcaption><strong>Rubro-Negra</strong> · altura {rn.altura()} · {rn.rotacoes} rotações
        · {rn.recoloracoes} recolorações
        <br><small>vermelho = rubro, preto = negro</small></figcaption>
      <div class="rolagem">{svg_arvore(rn.raiz, rn.NIL, "rn")}</div>
    </figure>
  </div>
</section>"""


CSS = """
:root { color-scheme: light; --fundo:#faf8f6; --texto:#2a1f1f; --suave:#6b5d5d; --linha:#c9bfbf;
        --grena:#6b2a22; --rubro:#c0222e; --negro:#1f1b1a; --avl:#2b5d8a; }
* { box-sizing: border-box; }
body { margin:0; padding:28px 20px 60px; background:var(--fundo); color:var(--texto);
       font-family: "Segoe UI", system-ui, -apple-system, Arial, sans-serif; line-height:1.45; }
header, section { max-width: 1180px; margin: 0 auto; }
h1 { color:var(--grena); margin:0 0 4px; font-size:1.7rem; }
header p { margin:0 0 26px; color:var(--suave); }
section { background:#fff; border:1px solid #e6dcd6; border-radius:12px; padding:18px 20px 22px; margin-bottom:22px; }
h2 { margin:0 0 4px; font-size:1.2rem; color:var(--grena); display:flex; flex-wrap:wrap; gap:6px 14px; align-items:baseline; }
.resposta { font-size:.85rem; font-weight:600; color:#fff; background:var(--grena); padding:2px 10px; border-radius:999px; }
.sequencia { margin:0 0 14px; color:var(--suave); font-size:.92rem; }
.par { display:grid; grid-template-columns: 1fr; gap:16px; }
@media (min-width: 1000px) { .par { grid-template-columns: 1fr 1fr; } }
figure { margin:0; border:1px solid #eee4de; border-radius:10px; padding:10px 12px; background:#fffdfc; min-width:0; }
figcaption { margin-bottom:8px; font-size:.95rem; }
figcaption small { color:var(--suave); }
.rolagem { overflow-x:auto; }
svg { display:block; margin:0 auto; max-width:none; }
.aresta { stroke:var(--linha); stroke-width:2; }
.no-avl { fill:var(--avl); } .no-rubro { fill:var(--rubro); } .no-negro { fill:var(--negro); }
.chave { fill:#fff; font-size:12px; font-weight:700; text-anchor:middle; }
.rotulo-h { fill:var(--suave); font-size:10px; text-anchor:middle; paint-order:stroke; stroke:#fffdfc; stroke-width:3px; }
"""


def main():
    pasta = Path(__file__).resolve().parent
    corpo = "".join(secao(n) for n in range(1, 7))
    pagina = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Árvores do questionário — AVL × Rubro-Negra</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Árvores do questionário — AVL × Rubro-Negra</h1>
  <p>Estrutura de Dados Avançados · Universidade de Vassouras · árvores resultantes da sequência de cada questão</p>
</header>
{corpo}
</body>
</html>
"""
    destino = pasta / "arvores.html"
    destino.write_text(pagina, encoding="utf-8")
    print(f"Arquivo gerado: {destino}")
    webbrowser.open(destino.as_uri())


if __name__ == "__main__":
    main()
