from arvores import comparar_detalhado
from experimentos import imprimir, imprimir_aleatorio

SEQUENCIA = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65]


def main():
    print(f"Sequencia do enunciado ({len(SEQUENCIA)} identificadores):\n")
    imprimir(comparar_detalhado(SEQUENCIA))
    imprimir_aleatorio(100, 50)
    imprimir_aleatorio(1000, 50)
    imprimir_aleatorio(10000, 10)


if __name__ == "__main__":
    main()
