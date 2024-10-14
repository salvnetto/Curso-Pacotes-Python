from calculadora._utils import verificar_numero_valido 

import numpy as np


def soma(x: int, y: int) -> int:
    """
    Calcula a soma de dois números.

    Args:
        x (int): O primeiro número.
        y (int): O segundo número.

    Returns:
        int: A soma dos dois números.
    """
    verificar_numero_valido(x)
    verificar_numero_valido(y)

    return np.add(x, y)

print(soma(2, 2))