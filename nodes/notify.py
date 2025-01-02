from typing import Dict, Any
import pywhatkit

from resume_graph.chains.notifications import whatsapp_chain
from resume_graph.chains.translation import translate_prompt, translate_chain
from resume_graph.state import GraphState

"""
from resume_graph.chains.notifications import whatsapp_chain
from resume_graph.state import GraphState


def notify_user(state: GraphState)-> Dict[str, Any]:

  print("---SENDING INFORMATION TO THE USER---")
  resumes = state["resumes"]
  resumes_string = "\n".join([f"{i + 1}. TITLE: {paper.title} \n RESUME: {paper.summary} \n URL: {paper.url}" for i, paper in enumerate(resumes)])
  whatsapp_msg =  whatsapp_chain.invoke(
      {
        "news": resumes_string
      }
  )
  print(whatsapp_msg)
  pass
"""
def send_whatsapp(state: GraphState):
  print("---SENDING INFORMATION TO THE USER---")
  resumes = state["resumes"]
  resumes_string = "\n".join([f"{i + 1}. TITLE: {paper.title} \n RESUME: {paper.summary} \n URL: {paper.url}" for i, paper in enumerate(resumes)])
  res =  whatsapp_chain.invoke(
      {
        "news": resumes_string
      }
  )
  print("---TRANSLATING MESSAGE---")
  whatsapp_msg = translate_chain.invoke(
      {
        "news": res.content
      }
  )
  pywhatkit.sendwhatmsg_instantly("+34635770927", whatsapp_msg.content)
  print("---USER HAS BEEN NOTIFICATED---")
