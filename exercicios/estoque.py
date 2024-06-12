# Ex estoque OBI 2023 Prog. Nível Sênior – Fase 1
# TERMINAR DEPOIS

#tipo = m linha
#tamanho = n coluna

# i = tipo de um pedido
# j = tamanho da peça pedida

m, n = [int(i) for i in input().split()]
matriz = []

for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input())
        print(matriz[i][j])

p = int(input()) #pedidos recebidos

