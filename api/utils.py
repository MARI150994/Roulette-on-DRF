import enum
import random
from typing import List


# give used cells and return random choice from available cells
def select_cell(used_cells: List) -> int:
    all_cells = list(range(1, 11))
    available_cells = set(all_cells) - set(used_cells)
    return random.choice(list(available_cells))

