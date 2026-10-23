# Questão 1 — Catálogo de produtos da loja

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**AVL.**

## O problema

Uma rede de supermercados de Maricá mantém em memória o catálogo de produtos, indexado pelo código.
O cadastro é montado uma vez pela manhã (códigos em ordem crescente, vindos do sistema legado) e,
durante o expediente, o sistema consulta preços milhares de vezes por minuto nos caixas.
Novos produtos quase nunca entram no meio do dia.

Sequência inserida: `10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150` (15 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Consulta milhares de vezes por minuto" | carga dominada por **busca** (leitura) |
| "Montado uma vez pela manhã" | quase nenhuma inserção durante o uso |
| Códigos em ordem crescente | risco de degeneração sem balanceamento |

Como a carga é de leitura, o que mais importa é o **custo de cada busca**, que no pior caso
é a **altura** da árvore. O custo de **montar** a árvore (as rotações) é pago uma única vez.

## Resultados medidos

Execução de `questao1.py` (altura contada em níveis de nós):

|    Árvore   | Altura | Rotações | Recolorações |
|-------------|--------|----------|--------------|
|     AVL     |    4   |    11    |      —       |
| Rubro-Negra |    6   |    9     |      8       |

Sem balanceamento, inserir 15 chaves em ordem crescente numa ABB comum geraria altura **15**
(uma lista encadeada, O(n)). As duas árvores evitam isso.

## Prova pela altura

- A AVL tem altura máxima ≈ 1,44 · log₂(n + 2). Com n = 15, a inserção em ordem crescente
  produz uma árvore **perfeita** de 4 níveis (log₂ 16 = 4).
- A Rubro-Negra tem altura máxima 2 · log₂(n + 1) = 8. Aqui ela chegou a 6.
- Pior caso de uma busca: **4 comparações na AVL contra 6 na Rubro-Negra** (50% a mais).
  Com milhares de consultas por minuto, essa diferença se repete a cada consulta.

## Prova pelas rotações

- A AVL fez **11 rotações**; a Rubro-Negra fez **9 rotações + 8 recolorações**.
- Em ordem crescente, toda inserção cai na ponta direita e força o rebalanceamento,
  então as duas trabalham bastante.
- Esse custo, porém, acontece **só na montagem da manhã**. Durante o expediente quase não há
  inserções, então as rotações a mais da AVL não pesam.

## Conclusão

A vantagem da Rubro-Negra é inserir com menos trabalho de reequilíbrio, mas essa vantagem
quase não é usada neste cenário. A vantagem da AVL é a árvore mais baixa, e ela é usada
milhares de vezes por minuto. Portanto, **AVL**.

> Observação: na Q1 a AVL faz mais rotações do que a Rubro-Negra (11 contra 9) e mesmo assim
> vence. O que decide é a altura, porque a carga é de leitura.

## Como executar

```bash
python questao1.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | implementação da AVL e da Rubro-Negra, com contadores de rotações e recolorações |
| `questao1.py` | insere a sequência nas duas árvores e imprime o comparativo |
