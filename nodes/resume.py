from typing import Dict, Any, List

from resume_graph.chains.summarize import summarize_chain
from resume_graph.state import GraphState, Paper


def resume(state: GraphState) -> Dict[str, Any]:
  """
  Summarizes the paper's abstract into a ~100 words resume.
  :param state: The current graph state
  :return:
  """
  print("---SUMMARIZING TOP 5 ABSTRACTS---")
  papers : List[Paper] = state["top_five"]

  for paper in papers:
    abstract_resume = summarize_chain.invoke(
        {
          "abstract": paper.summary
        }
    )
    print(f"---SUMMARIZED: {paper.title}---")
    paper.summary = abstract_resume.content
  return {
    "resumes": papers
  }
