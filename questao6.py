from arvores import comparar_detalhado
from experimentos import imprimir, imprimir_aleatorio

SEQUENCIA = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45]


def main():
    print(f"Sequencia do enunciado ({len(SEQUENCIA)} processos):\n")
    imprimir(comparar_detalhado(SEQUENCIA))
    imprimir_aleatorio(100, 50)
    imprimir_aleatorio(1000, 50)
    imprimir_aleatorio(10000, 10)


if __name__ == "__main__":
    main()
