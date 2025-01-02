from typing import TypedDict, Dict, List

class Paper:
  title: str
  url: str
  summary: str

  def __init__(self, title: str, summary: str, url: str):
    self.title = title
    self.summary = summary
    self.url = url

class GraphState(TypedDict):

  user_interest: str
  user_subinterest: List[str]
  papers: List[Paper]
  top_five: List[Paper]
  resumes: Dict[str, str]
  whatsapp_msg: str

