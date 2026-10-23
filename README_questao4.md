# Questão 4 — Índice de sessões ativas

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**Rubro-Negra.**

## O problema

Um servidor web mantém em memória o índice das sessões ativas, indexado pelo ID de sessão.
Como usuários entram e saem o tempo todo, o índice sofre inserções e remoções constantes
(o enunciado pede para considerar só as inserções). As buscas existem, mas são raras perto
do volume de alterações.

Sequência inserida: `42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70` (12 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Entram e saem o tempo todo" | carga de **escrita** |
| "Buscas raras perto do volume de alterações" | leitura secundária |
| IDs em ordem aleatória | sem risco de degeneração; inserção espalhada |

Com a escrita dominando, o que importa é o **custo de cada inserção**, não a altura.

## Resultados medidos

Sequência do enunciado:

|   Árvore    | Altura | Rotações | Recolorações | Verificações |
|-------------|--------|----------|--------------|--------------|
|     AVL     |    4   |     0    |      —       |      25      |
| Rubro-Negra |    4   |     0    |      3       |      3       |


Com essa sequência as duas **empatam** em altura e rotações; a diferença já aparece nas
verificações (25 contra 3). Como o servidor insere o tempo todo, o script também sorteia ordens
aleatórias de IDs e calcula as médias:

| Chaves | Árvore | Altura média | Rotações/inserção | Verificações/inserção |
|---:|---|---:|---:|---:|
| 100 | AVL | 7,98 | 0,656 | 5,38 |
| 100 | Rubro-Negra | 8,06 | 0,564 | 0,85 |
| 1.000 | AVL | 12,00 | 0,696 | 8,73 |
| 1.000 | Rubro-Negra | 12,10 | 0,580 | 0,89 |
| 10.000 | AVL | 16,00 | 0,694 | 12,11 |
| 10.000 | Rubro-Negra | 16,20 | 0,581 | 0,90 |

(50 sorteios para 100 e 1.000 chaves, 10 sorteios para 10.000; semente fixa 42.)

**Verificações** = na AVL, ancestrais cujo fator foi conferido; na Rubro-Negra, passos do laço
de correção.

## Prova pelas rotações

Mesmo com IDs aleatórios, a AVL rotaciona cerca de **16% mais** que a Rubro-Negra por inserção
(0,69 contra 0,58 com 10.000 chaves). Cada rotação mexe em ponteiros; já o Caso 1 da
Rubro-Negra é só recoloração.

## Prova pelo custo de reequilíbrio

A AVL confere, em toda inserção, o caminho até a raiz: 12 ancestrais em média com 10.000
chaves, número que cresce com log n. A Rubro-Negra para cedo e fica perto de 1 verificação por
inserção. Com inserções constantes, essa diferença se acumula o tempo todo.

## Prova pela altura (o que a Rubro-Negra perde)

Quase nada: com IDs aleatórios a AVL é só 0,1 a 0,2 nível mais baixa. E, como a busca é rara,
mesmo essa diferença pequena quase não é usada.

## Conclusão

A escrita domina, a Rubro-Negra rotaciona menos e verifica muito menos por inserção, e a
vantagem de altura da AVL é mínima e atende uma leitura rara. Portanto, **Rubro-Negra**.

> Observação: o enunciado manda considerar só inserções. Se as remoções entrassem na conta,
> a vantagem da Rubro-Negra seria ainda maior, já que o rebalanceamento dela após remoção
> é limitado a poucas rotações.

## Como executar

```bash
python questao4.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | AVL e Rubro-Negra com contadores |
| `experimentos.py` | tabelas e experimento com ordens aleatórias |
| `questao4.py` | roda a sequência do enunciado e os sorteios |
