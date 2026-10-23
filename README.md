# Questionário — Inserção em Árvores Balanceadas (AVL × Rubro-Negra)

**Curso:** Engenharia de Software — Universidade de Vassouras
**Disciplina:** Estrutura de Dados Avançados
**Professor:** Márcio Alexandre Dias Garrido

Para cada uma das 6 questões, o trabalho decide qual árvore implementar (AVL ou Rubro-Negra)
a partir do perfil de carga e **prova a escolha com medições** de altura e de rotações.

## Por onde começar

**Rode primeiro o `gerar_arvores.py`:**

```bash
python gerar_arvores.py
```

Ele gera o arquivo `arvores.html` e abre no navegador. Essa página é o resumo visual do trabalho:
mostra, para cada questão, a sequência inserida, **a resposta**, e as duas árvores desenhadas
(AVL e Rubro-Negra), com altura, rotações e recolorações.

Se o navegador não abrir sozinho, abra o `arvores.html` com duplo clique (já vem pronto na pasta).

## Depois, aprofunde em cada questão

1. Rode o script da questão para ver os números medidos no terminal: `python questao1.py` (e assim até a 6).
2. Leia o `README_questaoN.md` correspondente, com o enunciado, as pistas de carga, as tabelas e a justificativa.

## Respostas

| Questão | Tema | Carga dominante | Resposta |
|---|---|---|---|
| 1 | Catálogo de produtos da loja | busca, ordem crescente | **AVL** |
| 2 | Log de eventos do app Mumbuca | escrita, chaves crescentes | **Rubro-Negra** |
| 3 | Tabela de símbolos de um compilador | busca, ordem aleatória | **AVL** |
| 4 | Índice de sessões ativas | escrita, ordem aleatória | **Rubro-Negra** |
| 5 | Importação de cadastro já ordenado | busca, dados ordenados | **AVL** |
| 6 | Fila de processos do escalonador | escrita extrema | **Rubro-Negra** |

A regra que guia tudo: **leitura pesada favorece a AVL** (árvore mais baixa, busca mais rápida);
**escrita pesada favorece a Rubro-Negra** (menos trabalho de reequilíbrio por inserção).

## Requisitos

- Python 3.8 ou superior.
- Nenhuma biblioteca externa. Tudo usa apenas a biblioteca padrão.

## Arquivos

| Arquivo | Função |
|---|---|
| `README.md` | este guia |
| `gerar_arvores.py` | gera e abre a página `arvores.html` com as árvores de todas as questões |
| `arvores.html` | página pronta, com os desenhos e as respostas |
| `arvores.py` | implementação da AVL e da Rubro-Negra, com contadores de rotações, recolorações e verificações |
| `experimentos.py` | tabelas e experimento com ordens aleatórias (usado nas questões 3, 4 e 6) |
| `questao1.py` a `questao6.py` | um script por questão; cada um guarda a sequência do enunciado e mostra os números medidos |
| `README_questao1.md` a `README_questao6.md` | a análise de cada questão |

Mantenha todos os arquivos na **mesma pasta**: os scripts importam o `arvores.py`, e o
`gerar_arvores.py` lê a sequência de cada `questaoN.py`.

## Como ler os resultados

- **Altura:** número de níveis da árvore. No pior caso, é o número de comparações de uma busca.
- **Rotações:** quantas vezes a árvore precisou girar nós para se reequilibrar.
- **Recolorações:** só na Rubro-Negra; é o Caso 1, que corrige trocando cores, sem mover nós.
- **Verificações:** métrica própria deste trabalho para medir o custo de reequilíbrio por inserção.
  Na AVL, é quantos ancestrais tiveram a altura recalculada e o fator conferido; na Rubro-Negra,
  quantos passos o laço de correção deu.

## Observações

- Nas questões 3, 4 e 6 as sequências do enunciado, sozinhas, empatam (altura 4 e nenhuma rotação
  nas duas árvores). Por isso os scripts também sorteiam muitas ordens aleatórias (semente fixa 42),
  e a escolha é sustentada por essas médias.
- As questões 3, 4 e 6 usam o mesmo experimento, porque o perfil das chaves é o mesmo. O que muda
  entre elas é a carga (busca na 3, escrita na 4 e na 6).
- Na Q3 a vantagem de altura da AVL é pequena na média. A escolha vale porque o custo extra de
  montagem da AVL é pago uma só vez, e o README da questão explica isso.
