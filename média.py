print("bem vindo ao portal educacional da Ana")

notaUm = float(input("digite a primeira nota do aluno: "))
notaDois = float(input("digite a segunda nota do aluno: "))
notaTrês = float(input("digite a treceita nota do aluno: "))
notaQuatro = float(input("digite a quarta nota do aluno: "))

media = (notaUm + notaDois + notaTrês + notaQuatro) / 4

print(f"A média é {media}")

# o if e else são condicionais, e você pode tomar decisões
if media >= 6:
    print("parabéns! você está aprovado!")
else:
    print("você está reprovado! estude mais ano que vem")