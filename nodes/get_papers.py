from typing import Any, Dict, List

from ingestion import search_papers, download_papers, pdf_text_converter
from resume_graph.state import GraphState, Paper


def get_papers(state: GraphState)-> Dict[str, Any]:

  papers = search_papers(state["user_interest"])
  download_papers(papers)
  pdf_text_converter()

  return {
    "papers": papers
  }