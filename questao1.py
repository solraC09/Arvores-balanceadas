from arvores import comparar

SEQUENCIA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


def main():
    linhas = comparar(SEQUENCIA)

    print(f"Chaves inseridas: {len(SEQUENCIA)} (ordem crescente)\n")
    print(f"{'Arvore':<14}{'Altura':>8}{'Rotacoes':>10}{'Recolor.':>10}")
    for nome, altura, rotacoes, recolor in linhas:
        print(f"{nome:<14}{altura:>8}{rotacoes:>10}{recolor:>10}")

    print("\nPior caso de uma busca (comparacoes ate a folha mais funda):")
    for nome, altura, _, _ in linhas:
        print(f"  {nome:<12}: {altura}")


if __name__ == "__main__":
    main()
