class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Ordenando as moedas em ordem crescente
        coins.sort()

        # Inicializando a quantidade de moedas selecionadas como 0
        quantMoedas = 0

        while(amount != 0):
            # Encontrar a maior moeda que seja menor ou igual ao valor total atual
            k = 0
            for moeda in coins:
                if moeda <= amount:
                    k = moeda
                else:
                    break
            if k == 0:
                return -1

            # Atualizando o valor atual amount subtraindo o valor da moeda selecionada k
            amount -= k

            # Incrementando a quantidade de moedas selecionadas
            quantMoedas += 1
        return quantMoedas