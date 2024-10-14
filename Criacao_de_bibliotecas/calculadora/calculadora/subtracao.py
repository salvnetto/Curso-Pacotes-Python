from calculadora._utils import verificar_numero_valido 

def subtracao(x: int, y: int) -> int:
    """
    Calcula a diferença de dois números.

    Args:
        x (int): O primeiro número.
        y (int): O segundo número.

    Returns:
        int: A diferença entre o primeiro e o segundo número.
    """
    verificar_numero_valido(x)
    verificar_numero_valido(y)

    return x - y