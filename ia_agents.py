from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain.agents import Tool
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()

search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="google_search_tool",
        func=search.run,
        description="Ferramenta para fazer análises de bases de dados e auxiliar na tomada de descisão"
    )
]


def agente(prompt):
    model = ChatOpenAI(model="gpt-4.1-mini")

    agent = create_react_agent(
        model=model,
        tools=tools,

    )

    resp = agent.invoke({"messages": prompt})

    return resp['messages'][-1].content
