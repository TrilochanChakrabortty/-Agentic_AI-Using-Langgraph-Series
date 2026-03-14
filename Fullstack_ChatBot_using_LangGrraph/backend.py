from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver

from langgraph.graph.message import add_messages
class ChatState(TypedDict):
    
    messages: Annotated[list[BaseMessage], add_messages]
    
import os
from langchain_groq import ChatGroq 

os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(model="llama-3.1-8b-instant")
def chat_node(state: ChatState) -> ChatState:
    
    #take user query from state
    messages = state['messages']
    
    #send to the llm
    response = llm.invoke(messages)
    
    #add the response to the state
    return {"messages": [response]}

checkponinter = MemorySaver()

graph = StateGraph(ChatState)

#add nodes to the llm
graph.add_node("chat_node", chat_node)

#add edges to the graph
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

workflow = graph.compile(checkpointer=checkponinter)



