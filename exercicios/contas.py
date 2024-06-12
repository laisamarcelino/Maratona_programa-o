# Ex Contas a Pagar OBI 2023 Prog. Nível Sênior – Fase 1

v = int(input()) #valor disponivel
a = int(input()) # devendo açougue
f = int(input()) #devendo farmacia
p = int(input()) # devendo padaria

cont = 0

if a+f+p <= v:
    print(3)
elif a+f <= v or a+p <= v or f+p <= v:
    print(2)
elif a <= v or f <= v or p <= v:
    print(1)
else:
    print(0)
