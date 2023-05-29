class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Verificando se a lista de intervalos está vazia
        if len(intervals) == 0: return 0

        # Ordenando os intervalos pelo final em ordem crescente
        intervals.sort(key=lambda x: x[1])

        quantParaRemover = 0
        finalIntervalo = intervals[0][1]
        quantTotal = len(intervals)

        # Percorrendo a lista de intervalos
        for i in range(1, quantTotal):
            # Verificando se há sobreposição entre o intervalo atual e o último selecionado
            if intervals[i][0] >= finalIntervalo:
                # Atualizando a variável finalIntervalo para a posição atual, pois não há sobreposição
                finalIntervalo = intervals[i][1]
            else:
                # Incrementando o contador quando há sobreposição
                quantParaRemover += 1

        # Retornando o número mínimo de intervalos que precisam ser removidos
        return quantParaRemover