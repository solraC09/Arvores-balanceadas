# Questão 3 — Tabela de símbolos de um compilador

**Disciplina:** Estrutura de Dados Avançados — Engenharia de Software, Universidade de Vassouras
**Tema:** escolher entre AVL e Rubro-Negra a partir do perfil de carga e provar a escolha pela altura e pelas rotações.

## Resposta

**AVL.**

## O problema

A tabela de símbolos é construída uma vez na análise (os identificadores entram em ordem
imprevisível) e depois é consultada intensamente nas fases de verificação de tipos e geração
de código. Cada referência a uma variável é uma busca, e as buscas superam em muito as inserções.

Sequência inserida: `50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65` (12 chaves).

## Análise do perfil de carga

| Pista do enunciado | O que significa |
|---|---|
| "Consultada intensamente", "buscas muito mais frequentes que inserções" | carga de **busca** |
| "Construída uma vez" | inserção só na montagem |
| Chaves em ordem imprevisível | ordem aleatória, sem risco de degeneração |

Como a carga é de leitura, o que importa é a **altura** (custo de cada busca). O custo de
inserir é pago uma única vez.

## Resultados medidos

Sequência do enunciado:

|   Árvore    | Altura | Rotações | Recolorações | Verificações |
|-------------|--------|----------|--------------|--------------|
|     AVL     |    4   |     0    |      —       |      25      |
| Rubro-Negra |    4   |     0    |      3       |      3       |


Com essa sequência as duas árvores **empatam**: altura 4 e nenhuma rotação. Por isso o script
também sorteia ordens aleatórias de chaves (mesmo perfil do enunciado) e calcula as médias:

| Chaves | Árvore | Altura média | Altura máxima | Rotações/inserção | Verificações/inserção |
|---:|---|---:|---:|---:|---:|
| 100 | AVL | 7,98 | 8 | 0,656 | 5,38 |
| 100 | Rubro-Negra | 8,06 | 9 | 0,564 | 0,85 |
| 1.000 | AVL | 12,00 | 12 | 0,696 | 8,73 |
| 1.000 | Rubro-Negra | 12,10 | 13 | 0,580 | 0,89 |
| 10.000 | AVL | 16,00 | 16 | 0,694 | 12,11 |
| 10.000 | Rubro-Negra | 16,20 | 17 | 0,581 | 0,90 |

(50 sorteios para 100 e 1.000 chaves, 10 sorteios para 10.000; semente fixa 42.)

## Prova pela altura

- A AVL tem altura máxima ≈ 1,44 · log₂(n + 2); a Rubro-Negra, 2 · log₂(n + 1). O limite
  da AVL é menor.
- Com chaves aleatórias a diferença média é **pequena**: cerca de 0,1 a 0,2 nível. A AVL
  fica sempre um pouco mais baixa (e a altura máxima observada também: 12 contra 13 com
  1.000 chaves, 16 contra 17 com 10.000).

## Prova pelas rotações

A AVL gasta mais para montar: 0,69 rotações e 12 verificações por inserção (10.000 chaves),
contra 0,58 e 0,9 na Rubro-Negra. Mas isso acontece **uma só vez**, na análise do código.

## Conclusão

A vantagem da AVL aqui é pequena na média, mas é **gratuita**: a Rubro-Negra só compensaria
se inserir fosse frequente, e na tabela de símbolos a inserção ocorre só na montagem. Como
cada referência no código é uma busca, qualquer redução de altura se repete muitas vezes.
Sem nada a ganhar na escrita, não há motivo para abrir mão da árvore mais baixa. Portanto, **AVL**.

> Observação: a diferença de altura entre as duas é pequena para chaves aleatórias. A escolha
> da AVL se sustenta porque o custo extra de montagem não pesa nesta carga, não porque a
> Rubro-Negra seja ruim para busca.

## Como executar

```bash
python questao3.py
```

## Arquivos

| Arquivo | Função |
|---|---|
| `arvores.py` | AVL e Rubro-Negra com contadores |
| `experimentos.py` | tabelas e experimento com ordens aleatórias |
| `questao3.py` | roda a sequência do enunciado e os sorteios |
