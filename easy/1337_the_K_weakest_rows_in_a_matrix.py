
from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

print(kWeakestRows(mat, 3))