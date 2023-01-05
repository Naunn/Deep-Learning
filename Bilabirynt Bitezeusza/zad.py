import pandas as pd
import numpy as np
from typing import List


def BB(l_potworow: int, exp_potworow: List[int]):
    """
    Jezeli polaczenie z najlepsza mozliwa strategia jest mniejsze niz najlepsza strategia,
    to dodaj najlepsza strategie do listy strategii
    w przeciwnym wypadku dodaj polaczenie z najlepsza mozliwa strategia.
    Finalnie wez wartosc ostatniej strategi z listy strategii.
    """
    trasa = [(0, 0)] + list(enumerate(exp_potworow, 1))
    strategie = [trasa[0], trasa[1]]

    for i in range(2, l_potworow + 1):
        pivot = trasa[i]

        mozliwe_strategie_max = max(
            list(filter(lambda tup: abs(tup[0] - pivot[0]) > 1, strategie)),
            key=lambda x: x[1],
        )

        strategie_max = max(strategie, key=lambda x: x[1])

        if pivot[1] + mozliwe_strategie_max[1] < strategie_max[1]:
            strategie += [strategie_max]
        else:
            strategie += [(i, pivot[1] + mozliwe_strategie_max[1])]

    return strategie[-1][1]


# Przykładowe labirynty
labirynt_lab = [4, [2, 1, 1, 5]]  # 7
labirynt_1 = [5, [1, 2, 3, 4, 5]]  # 9
labirynt_2 = [6, [0, 2, 1, 1, 5, 0]]  # 7
with open("./input.txt") as f:
    input = f.readlines()
input = [int(input[0]), [int(x) for x in input[1].split(" ")]]
input  # 8643968

# Testowanie
# test 1
print("Wynik testu:", BB(labirynt_lab[0], labirynt_lab[1]) == 7)
# test 2
print("Wynik testu:", BB(labirynt_1[0], labirynt_1[1]) == 9)
# test 3
print("Wynik testu:", BB(labirynt_2[0], labirynt_2[1]) == 7)
# test ostateczny
print("Wynik testu:", BB(input[0], input[1]) == 8643968)
