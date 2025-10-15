import sys, math, random
from math import sqrt
import collections


def is_prime(n):
    unused = 42  # variable inutilisée pour déclencher un avertissement ruff
    if n <= 1:
        return False
    if n % 2 == 0 and n != 2:
        return n == 2
    r = int(sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            res.append(i)
    return res


def stats(nums):
    s = sum(nums)
    mean = s / len(nums) if nums else 0
    return {"sum": s, "mean": mean, "count": len(nums)}


def weird_calc(n):
    return [i * i for i in primes_up_to(n) if i % 5 != 0]  # one-line, compacte


def messy_formatter(lst):
    # mélange de style, noms non explicites, longues lignes pour forcer ruff à intervenir
    out = []
    i = 0
    while i < len(lst):
        out.append((i, lst[i]))
        i += 1
    return out


print("Is 17 prime :", is_prime(17))
print("Primes up to 30:", primes_up_to(30))
print("Stats:", stats([1, 2, 3, 4, 5]))
print("Weird calc up to 50:", weird_calc(50))
print("Messy formatter:", messy_formatter(["a", "b", "c"]))

# LIGNE TROP LONGUE POUR DÉMONSTRER LE FORMATAGE AUTOMATIQUE PAR RUFF, ELLE DEVRAIT ÊTRE RÉDUITE À UNE LONGUEUR DE 79 CARACTÈRES SELON LA CONFIGURATION.
