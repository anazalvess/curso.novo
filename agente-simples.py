from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#todos os agentes necessitam da chave de API, e a função LOAD_DOTENV faz a leitura do arquivo no .env.
load_dotenv()

perguntaUsuario = input("digite a sua pergunta: ")

agente = Agent(
    #essa linha, define o modelo do meu agente.
    model= OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

agente.print_response(perguntaUsuario)
