
listaNotas = []

print("-" * 40)
print("bem vindo a I.A que calcula a média final 🤖")
print("-" * 40)

while True:
    notas = input("digite a nota que deseja inserir (digite sair para parar): ")
    if notas.lower () == "sair": #comando lower briga a entrada a ser toda minuscula
        break
    else:
        listaNotas.append(float(notas))#insere dados em uma lista
    
media = sum(listaNotas) / len(listaNotas)

print(f" A media final do aluno é {media:.2f}")

if media >= 6:
    print("parabéns! você está aprovado!")
else:
    print("você está reprovado! estude mais ano que vem")