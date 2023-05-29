class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = []

        # Construir os intervalos de tempo para cada viagem
        for numPassengers, fromi, toi in trips:
            intervals.append((fromi, numPassengers))
            intervals.append((toi, -numPassengers))

        # Ordenar os intervalos com base na localização "from"
        intervals.sort()

        current_capacity = 0

        # Percorrer os intervalos e verificar a capacidade do carro
        for _, passengers in intervals:
            current_capacity += passengers

            # Verificar se a capacidade atual excede a capacidade do carro
            if current_capacity > capacity:
                return False

        return True
