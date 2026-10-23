# Questão 6 — Fila de processos do escalonador

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**Rubro-Negra.**

## O problema

O escalonador de um sistema operacional didático mantém os processos prontos numa árvore
ordenada pela prioridade/tempo virtual. A cada troca de contexto, dezenas de milhares de vezes
por segundo, um processo é inserido reposicionado. É caminho crítico: cada microssegundo
reorganizando a estrutura é tempo roubado da CPU. Buscar um elemento específico quase nunca acontece.

Sequência inserida: `40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45` (12 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Dezenas de milhares de vezes por segundo" | **escrita** extrema |
| "Caminho crítico", "busca quase nunca" | leitura irrelevante |
| Dica: estrutura que o kernel Linux usa no escalonador | Rubro-Negra |

Aqui o que decide é o **custo por inserção**: cada operação desperdiçada tira tempo da CPU.

## Resultados medidos

Sequência do enunciado:

|   Árvore    | Altura | Rotações | Recolorações | Verificações |
|-------------|--------|----------|--------------|--------------|
|     AVL     |    4   |     0    |      —       |      25      |
| Rubro-Negra |    4   |     0    |      3       |      3      |


Com essa sequência não há rotação em nenhuma das duas, e a diferença já aparece nas
verificações (25 contra 3). Como o escalonador insere sem parar, o script também sorteia
ordens aleatórias e calcula as médias:

| Chaves | Árvore | Altura média | Rotações/inserção | Verificações/inserção |
|---:|---|---:|---:|---:|
| 100 | AVL | 7,98 | 0,656 | 5,38 |
| 100 | Rubro-Negra | 8,06 | 0,564 | 0,85 |
| 1.000 | AVL | 12,00 | 0,696 | 8,73 |
| 1.000 | Rubro-Negra | 12,10 | 0,580 | 0,89 |
| 10.000 | AVL | 16,00 | 0,694 | 12,11 |
| 10.000 | Rubro-Negra | 16,20 | 0,581 | 0,90 |

(50 sorteios para 100 e 1.000 chaves, 10 sorteios para 10.000; semente fixa 42. É o mesmo
experimento das questões 3 e 4, porque o perfil de chaves, aleatórias, é o mesmo; o que muda
é a carga.)

**Verificações** = na AVL, ancestrais cujo fator foi conferido; na Rubro-Negra, passos do laço
de correção.

## Prova pelas rotações

A AVL rotaciona cerca de **16% mais** por inserção (0,69 contra 0,58 com 10.000 processos).
A Rubro-Negra garante no máximo 2 rotações por inserção, e o Caso 1 só recolore, sem mover nós.

## Prova pelo custo de reequilíbrio

A cada inserção a AVL recalcula e confere o caminho até a raiz, 12 ancestrais em média com
10.000 processos. A Rubro-Negra fica perto de 1 verificação por inserção. Multiplicado por
dezenas de milhares de trocas de contexto por segundo, é muito tempo de CPU.

## Prova pela altura (o que a Rubro-Negra perde)

Quase nada: 0,1 a 0,2 nível a mais na média. E a busca por elemento específico quase nunca
acontece, então a árvore mais baixa da AVL não é aproveitada.

## Conclusão

Em escrita extrema e caminho crítico, a Rubro-Negra rotaciona menos, verifica muito menos por
inserção e perde apenas em altura, que aqui ninguém usa. É também a estrutura usada pelo
escalonador do kernel Linux, como o enunciado sugere. Portanto, **Rubro-Negra**.

## Como executar

```bash
python questao6.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | AVL e Rubro-Negra com contadores |
| `experimentos.py` | tabelas e experimento com ordens aleatórias |
| `questao6.py` | roda a sequência do enunciado e os sorteios |
