from typing import Dict, Any, List

from langchain_core import documents

from resume_graph.chains.filter import filter_chain
from resume_graph.state import GraphState, Paper


def select_top_5(state: GraphState)-> Dict[str, Any]:
  """
  Filter all papers from the past week to identify and return those that are truly relevant to the user.
  :param state: current grapph state
  :return: the relevant documents to the user
  """
  print("---SELECTING TOP 5 FOR THE USER---")
  user_interest = state["user_interest"]
  user_subinterest = state["user_subinterest"]

  titles = []

  papers = state["papers"]
  for paper in papers:
    titles.append(paper.title)

  documents_list_string = "\n".join([f"{i + 1}.{title}" for i, title in enumerate(titles)])

  filtered_documents= filter_chain.invoke(
      {
        "user_interest": user_interest,
        "user_subinterest": user_subinterest,
        "documents": documents_list_string
      }
  )
  filtered_documents = eval(filtered_documents.content)

  top_five = []

  for document_title in filtered_documents:
    for paper in papers:
      if paper.title == document_title:
        top_five.append(paper)

  return {
    "top_five": top_five
  }