import os
import re
from typing import Any, Dict

from resume_graph.consts import DOCS_PATH
from resume_graph.state import GraphState


def get_abstracts(state: GraphState)-> Dict[str, Any]:

  print("---EXTRACTING ABSTRACTS FROM DOCUMENTS---")
  abstracts_dict = {}

  for filename in os.listdir(DOCS_PATH):
    filepath = os.path.join(DOCS_PATH, filename)
    with open(filepath, "r") as file:
      content = file.read()

      abstract_match = re.search(r'\babstract\b', content, re.IGNORECASE)
      introduction_match = re.search(r'\bintroduction\b', content, re.IGNORECASE)

      if abstract_match and introduction_match:
        abstract_start = abstract_match.end()
        introduction_start = introduction_match.start()

        abstract_text = content[abstract_start:introduction_start].strip()

        title = os.path.splitext(filename)[0]
        abstracts_dict[title] = abstract_text

  return {
    "originals": abstracts_dict
  }