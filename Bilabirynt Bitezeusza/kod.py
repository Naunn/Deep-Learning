import pandas as pd
import numpy as np
from typing import List
import sys


inFile = sys.argv[1]
outFile = sys.argv[2]


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


with open(inFile, "r") as i:
    lines = i.readlines()
input = [int(lines[0]), [int(x) for x in lines[1].split(" ")]]

result = BB(input[0], input[1])

with open(outFile, "w") as o:
    o.write(str(result))
