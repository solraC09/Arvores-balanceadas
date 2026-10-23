# Questão 2 — Log de eventos do app Mumbuca

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**Rubro-Negra.**

## O problema

O aplicativo da moeda Mumbuca registra cada transação num índice em memória, ordenado pelo
timestamp (que, por natureza, só cresce). O sistema insere um novo evento a cada poucos
milissegundos, o dia inteiro; relatórios que percorrem o índice são gerados uma vez por dia,
de madrugada.

Sequência inserida: `5, 10, 15, 20, 25, 30, 35, 40, 45, 50` (10 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Insere a cada poucos milissegundos" | carga dominada por **escrita** (inserção) |
| "Relatório uma vez por dia" | **busca é rara** |
| Timestamps só crescem | inserção **sempre à direita**, o pior caso de desbalanceamento |

Aqui a conta é o oposto da Q1: como a escrita domina, o que importa é o **custo de cada
inserção**. A altura da árvore quase não pesa, porque quase ninguém busca.

## Resultados medidos

Execução de `questao2.py` (altura contada em níveis de nós):

|   Árvore    | Altura | Rotações | Recolorações | Verificações |
|-------------|--------|----------|--------------|--------------|
|     AVL     |    4   |     6    |      —       |      25      |
| Rubro-Negra |    5   |     5    |      5       |      10      |

**Verificações** é uma métrica que o código mede para comparar o trabalho de reequilíbrio:
na AVL, quantos ancestrais tiveram a altura recalculada e o fator conferido; na Rubro-Negra,
quantos passos o laço de correção deu.

Com 10 chaves a diferença é pequena. Como o app insere o dia inteiro, o script também roda
o mesmo cenário (timestamps crescentes) com mais eventos:

| Eventos | Árvore | Altura | Rotações | Verificações |
|---:|---|---:|---:|---:|
| 100 | AVL | 7 | 93 | 573 |
| 100 | Rubro-Negra | 11 | 89 | 176 |
| 1.000 | AVL | 10 | 990 | 8.977 |
| 1.000 | Rubro-Negra | 17 | 983 | 1.961 |
| 10.000 | AVL | 14 | 9.986 | 123.617 |
| 10.000 | Rubro-Negra | 24 | 9.976 | 19.947 |

## Prova pelas rotações

As rotações **empatam**: nas duas árvores, com timestamps crescentes, é cerca de 1 rotação
por inserção (9.986 contra 9.976 em 10.000 eventos). Por isso o argumento não está nelas.
Vale registrar que a Rubro-Negra garante no máximo 2 rotações por inserção, e as correções
do Caso 1 são só recolorações, que não movem nós.

## Prova pelo custo de reequilíbrio

- A AVL, em **toda** inserção, volta pelo caminho inteiro recalculando alturas até a raiz.
  Isso dá em média cerca de 12 verificações por inserção com 10.000 eventos (123.617 / 10.000),
  e cresce com log n.
- A Rubro-Negra para assim que o pai do nó novo é negro, e o trabalho médio fica perto de
  **2 passos por inserção** (19.947 / 10.000), sem crescer de forma relevante com n.
- Com inserção a cada poucos milissegundos, esse trabalho fixo por inserção se acumula
  o dia inteiro.

## Prova pela altura (o que a Rubro-Negra perde)

A AVL é mais baixa: 14 níveis contra 24 com 10.000 eventos. Isso significaria buscas mais
rápidas, mas a busca aqui é **rara** (um relatório por dia, de madrugada). Pagar a rigidez da
AVL a cada inserção para ganhar velocidade em buscas que quase não acontecem não compensa.

## Conclusão

Em carga de escrita pesada com chaves crescentes, as rotações empatam e a Rubro-Negra vence
no trabalho de reequilíbrio por inserção, enquanto a vantagem de altura da AVL só ajudaria
em buscas que quase não existem. Portanto, **Rubro-Negra**.

> Observação: com apenas 10 chaves, a diferença entre as árvores é pequena (6 contra 5
> rotações). A escolha é sustentada pelo comportamento quando o log cresce, que é o cenário
> real do app.

## Como executar

```bash
python questao2.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | implementação da AVL e da Rubro-Negra, com contadores de rotações, recolorações e verificações |
| `questao2.py` | roda a sequência do enunciado e o cenário com mais eventos |
