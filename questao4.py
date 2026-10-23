from arvores import comparar_detalhado
from experimentos import imprimir, imprimir_aleatorio

SEQUENCIA = [42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70]


def main():
    print(f"Sequencia do enunciado ({len(SEQUENCIA)} IDs de sessao):\n")
    imprimir(comparar_detalhado(SEQUENCIA))
    imprimir_aleatorio(100, 50)
    imprimir_aleatorio(1000, 50)
    imprimir_aleatorio(10000, 10)


if __name__ == "__main__":
    main()
