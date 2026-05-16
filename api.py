#instalar bibliotecas
#pip install requests

#segundo passo: adicionar/importar ao código
import requests

nome = input("digite seu nome: ")
email = input("digite seu e-mail: ")
telefone = input("digite o seu telefone: ")
#recebe cep: digitado pelo usuário
cep = input("qual seu cep? ")

#cria um variável e atribui o resultado do link
#utilizamos o f string, para conseguir inserir uma variável
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()

print(f"Bem vindo ao Mercado Livre {nome}. O seu e-mail é {email}. O seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, na cidade {dados['localidade']}, no estado {dados['estado']}.")



#atribuindo variáveis para cada um dos resultados 
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']

