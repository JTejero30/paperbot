from langgraph.graph import END, StateGraph

from consts import ABSTRACTS, RESUME, FILTER, NOTIFY, PAPERS
from nodes.get_papers import get_papers
from nodes.abstracts import get_abstracts
from nodes.notify import send_whatsapp
from nodes.resume import resume
from nodes.user_filter import select_top_5
from state import GraphState

builder = StateGraph(GraphState)

builder.add_node(PAPERS, get_papers)
builder.add_node(ABSTRACTS, get_abstracts)
builder.add_node(FILTER, select_top_5)
builder.add_node(RESUME, resume)
builder.add_node(NOTIFY, send_whatsapp)

builder.set_entry_point(PAPERS)

builder.add_edge(PAPERS, ABSTRACTS)
builder.add_edge(ABSTRACTS, FILTER)
builder.add_edge(FILTER, RESUME)
builder.add_edge(RESUME, NOTIFY)
builder.add_edge(NOTIFY, END)

graph =  builder.compile()

graph.get_graph().draw_mermaid_png(output_file_path="resume_graph.png")
