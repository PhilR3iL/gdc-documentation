# math_utils.py

def additionner(x, y):
    return x + y

def soustraire(a, b):
    return a - b

def factorielle(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def moyenne(nombres):
    return sum(nombres) / len(nombres)

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        raise ValueError("Impossible de diviser par zéro")
    return a / b

def puissance(base, exposant):
    return base ** exposant

def racine_carree(x):
    if x < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
    return x ** 0.5

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ppcm(a, b):
    return abs(a * b) // pgcd(a, b)

def fibonacci(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def moyenne_harmonique(nombres):
    if len(nombres) == 0:
        raise ValueError("Impossible de calculer la moyenne harmonique d'une liste vide")
    return len(nombres) / sum(1 / x for x in nombres)

def mode(nombres):
    from collections import Counter
    freq = Counter(nombres)
    max_count = max(freq.values())
    return [key for key, count in freq.items() if count == max_count]
