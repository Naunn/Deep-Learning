import pandas as pd
import numpy as np
from typing import List


def BB(
    l_potworow: int, exp_potworow: List[int], i: int = 0, exp: int = 0, krok: int = 3
):

    if i > l_potworow:
        return exp

    print(i)
    # niech sprawdza najlepsza pare rozwiazan o 3 kroki wprzód
    tab = exp_potworow[i : i + krok]

    print(tab)

    para = tab[0] + tab[2]
    print(tab[0], tab[2])

    singiel = tab[1]
    print(tab[1])

    if para > singiel:
        print("para")

        exp += para
        i += i + 3
        print("i", i)
        BB(l_potworow=l_potworow, exp_potworow=exp_potworow, i=i, exp=exp)
    else:
        print("singiel")

        exp += singiel
        i += i + 1
        print("i", i)
        BB(l_potworow=l_potworow, exp_potworow=exp_potworow, i=i, exp=exp)


labirynt_1 = [5, [1, 2, 3, 4, 5]]

BB(labirynt_1[0], labirynt_1[1])

# 4
# 2,1,1,5

# i = 0 (2)
# mamy 0 expa
# do wyboru jest 0 lub 2 expa
# zapisujemy scenariusze
# [0,2]

# i = 1 (1)
# mamy [0,2] expa
# do wyboru jest 0 + 1 lub 2 + 0
# zapisujemy lepszy wybór
# [0,2,2]

# i = 2 (1)
# mamy [0,2,2] expa
# do wyboru mamy 2 + 1 lub 0 + 1
# zapisujemy lepszy wybór
# [0,2,2,3]

# i = 3 (5)
# mamy [0,2,2,3] expa
# do wyboru jest

# 0,2,2,3,7
