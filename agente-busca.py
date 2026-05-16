from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat

load_dotenv()

BancoDados = SqliteDb(db_file="temp/registros.db")

agente = Agent(
    model=OpenAIChat(id="gpt-5.4-mini"),
    description="você é um arqueiro e vive fugindo dos contrabandistas",
    db=BancoDados,
    session_id="21f0c63c-2b75-4204-aed3-84f85f95d2ae",
    tools=[DuckDuckGoTools(),TavilyTools],
    markdown=True

)

while True:
    pergunta = input("digite sua pergunta: ")
    if pergunta.lower()in ['sair',  'exite', 'quit', 'cancelar', 'finalizar']:
        print("encerrando agente...\nFique à vontade quando tiver mais dúvidas! 🤖")
        break
    else:
       agente.print_response(pergunta)  