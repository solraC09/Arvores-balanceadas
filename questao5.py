from arvores import comparar_detalhado
from experimentos import imprimir

SEQUENCIA = [1, 2, 3, 4, 5, 6, 7]


def main():
    print(f"Sequencia do enunciado ({len(SEQUENCIA)} inscricoes, ja ordenadas):\n")
    imprimir(comparar_detalhado(SEQUENCIA))
    for n in (100, 1000, 10000, 100000):
        print(f"\nImportacao de {n} inscricoes ordenadas:")
        imprimir(comparar_detalhado(range(1, n + 1)))


if __name__ == "__main__":
    main()
