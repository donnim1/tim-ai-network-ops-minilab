from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
import requests
import os

# put your API key in environment variable OPENAI_API_KEY

@tool
def get_anomalies():
    """Get current anomalies from network API"""
    r = requests.get("http://127.0.0.1:8000/anomalies")
    return r.text

@tool
def router_impact(router_name: str):
    """Get affected towers if a router fails"""
    r = requests.get(f"http://127.0.0.1:8000/impact/{router_name}")
    return r.text

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tools = [get_anomalies, router_impact]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

while True:
    q = input("Ask: ")
    if q == "exit":
        break
    print(agent.run(q))