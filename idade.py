print("-" * 50)
print(" bem vindo ao coletor de dados do Chat GPT 🤖")
print("-" * 50)

# DECLARAÇÕES DE VARIÁVEIS
nome = input("digite seu nome: ") #input recebe dados do teclado do usuário
email = input("digite seu email: ") #criei uma variável email que irá armazenar o email do usuário 
cidade = input("em qual cidade você mora?: ")
estado = input("em qual estado?: ")
país = input("este estado fica em qual pais?: ")
qualSeuAno = int(input("digite seu ano "))
idadeAtual = 2026 - qualSeuAno


print(f"Olá {nome} vamos confirmar seus dados, o seu e-mail é {email}, você mora na cidade de {cidade}, que fica no estado de {estado}, seu país é o(a) {país}, a sua idade atual é {idadeAtual} ") #o f minúsculo antes das aspas, permite que eu trabalhe com variáveis na frase. As cchaves {} servem paraeu chamar uma variável dentro da frase
