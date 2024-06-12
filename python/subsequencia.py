# Ex Subsequência OBI 2023 Prog. Nível Sênior – Fase 1

a, b = [int(i) for i in input().split()]
sequenciaA = [int(x) for x in input().split()]
sequenciaB = [int(y) for y in input().split()]

i = 0
j = 0

while len(sequenciaA)-1 > i:
    if sequenciaB[j] == sequenciaA[i]:
        i += 1
        j += 1
    else:
        i += 1

if sequenciaB[j] == sequenciaA[i]:
    print("S")
else:
    print("N")