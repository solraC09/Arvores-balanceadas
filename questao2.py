from arvores import comparar_detalhado

SEQUENCIA = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def imprimir(linhas):
    print(f"{'Arvore':<14}{'Altura':>8}{'Rotacoes':>10}{'Recolor.':>10}{'Verific.':>10}")
    for nome, altura, rotacoes, recolor, verif in linhas:
        print(f"{nome:<14}{altura:>8}{rotacoes:>10}{recolor:>10}{verif:>10}")


def main():
    print(f"== Sequencia do enunciado ({len(SEQUENCIA)} timestamps crescentes) ==\n")
    imprimir(comparar_detalhado(SEQUENCIA))

    print("\n== Escalando: o log cresce o dia todo ==")
    for n in (100, 1000, 10000):
        print(f"\n{n} eventos:")
        imprimir(comparar_detalhado(range(n)))

    print("\nVerific. = ancestrais conferidos na AVL / passos do while na Rubro-Negra.")


if __name__ == "__main__":
    main()
