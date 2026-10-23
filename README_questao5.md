# Questão 5 — Importação de cadastro já ordenado

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**AVL.**

## O problema

A prefeitura exporta o cadastro de IPTU já ordenado pela inscrição imobiliária. Ele será
importado para uma árvore em memória que, depois de carregada, será consultada o dia todo pelo
atendimento ao cidadão. A importação é feita uma vez; a consulta é permanente. Inserir em
ordem crescente numa BST comum a faria degenerar numa lista (O(n)).

Sequência inserida: `1, 2, 3, 4, 5, 6, 7` (7 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Consultada o dia todo" | carga de **busca** |
| "Importação uma vez" | inserção só na carga |
| Dados já ordenados | pior caso de degeneração; balanceamento obrigatório |

## Resultados medidos

Sequência do enunciado:

|   Árvore    | Altura | Rotações | Recolorações | Verificações |
|-------------|--------|----------|--------------|--------------|
|     AVL     |    3   |     4    |      —       |      14      |
| Rubro-Negra |    4   |     3    |      2       |      5       |


Para ver o comportamento com um cadastro de tamanho real, o script importa mais inscrições em
ordem crescente:

| Inscrições | Árvore | Altura | Rotações | Verificações |
|---:|---|---:|---:|---:|
| 100 | AVL | 7 | 93 | 573 |
| 100 | Rubro-Negra | 11 | 89 | 176 |
| 1.000 | AVL | 10 | 990 | 8.977 |
| 1.000 | Rubro-Negra | 17 | 983 | 1.961 |
| 10.000 | AVL | 14 | 9.986 | 123.617 |
| 10.000 | Rubro-Negra | 24 | 9.976 | 19.947 |
| 100.000 | AVL | 17 | 99.983 | 1.568.929 |
| 100.000 | Rubro-Negra | 31 | 99.969 | 199.933 |

Uma BST comum teria altura igual ao número de chaves (100.000 níveis no último caso).

## Prova pela altura

- Em ordem crescente a AVL produz uma árvore praticamente perfeita: 3 níveis com 7 chaves,
  17 com 100.000 (log₂ 100.000 ≈ 16,6).
- A Rubro-Negra fica bem mais alta: 4 níveis com 7 chaves e 31 com 100.000.
- No pior caso, cada consulta custa **17 comparações na AVL contra 31 na Rubro-Negra**,
  cerca de 45% menos. O atendimento consulta o dia todo, então isso se repete o tempo todo.

## Prova pelas rotações

- As rotações são praticamente iguais nas duas (99.983 contra 99.969 com 100.000 inscrições,
  perto de 1 por inserção).
- A AVL verifica mais ancestrais para montar (1,57 milhão contra 200 mil), mas isso ocorre
  **uma única vez**, na importação.

## Conclusão

O custo extra da AVL é pago uma vez, na carga; a vantagem dela, uma árvore bem mais baixa,
se repete em cada consulta. Portanto, **AVL**.

> Observação: como os dados já chegam ordenados, existe ainda a opção de montar a árvore
> direto a partir da lista, sem inserir um a um. Fica fora do escopo da questão, que pede
> a escolha entre as duas árvores.

## Como executar

```bash
python questao5.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | AVL e Rubro-Negra com contadores |
| `experimentos.py` | impressão das tabelas |
| `questao5.py` | roda a sequência do enunciado e as importações maiores |
