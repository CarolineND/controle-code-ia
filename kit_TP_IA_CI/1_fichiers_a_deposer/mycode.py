# mycode.py — version corrigée


def division(a, b):
    """Divise a par b et retourne le résultat."""
    if b == 0:
        raise ValueError("division par zéro")
    return a / b


def factorielle(n):
    """Calcule la factorielle de n (récursif)."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("n doit être un entier positif")
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    if n == 0:
        return 1
    return n * factorielle(n - 1)
