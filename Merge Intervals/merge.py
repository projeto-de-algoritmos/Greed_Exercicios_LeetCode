from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Ordena os intervalos em ordem crescente com base no início
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]  # Lista para armazenar os intervalos mesclados

        for interval in intervals[1:]:
            # Verifica se há sobreposição com o último intervalo mesclado
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])  # Mescla os intervalos
            else:
                merged.append(interval)  # Adiciona o intervalo à lista mesclada

        return merged
