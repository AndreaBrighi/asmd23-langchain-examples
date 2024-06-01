import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

prompt = hub.pull("hwchase17/react")
llm = Ollama(model="mistral")
tools = load_tools(["llm-math"], llm=llm)
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
#agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent_executor.invoke({"input":"My age is 28, what is my age raised at the power of 2.4"})