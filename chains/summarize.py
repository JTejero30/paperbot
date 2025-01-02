from typing import Dict

from langchain_core.prompts import ChatPromptTemplate

from resume_graph.models.ollama_model import OllamaModel

llm = OllamaModel().get_model()
"""
NO VALID WITH LLAMA->
class Abstract(BaseModel):
  title: str = Field(description= "Title of the paper")
  resume: str = Field(description=" 100~ resume of the paper abstract")

structured_llm_summarize = llm.with_structured_output(Abstract)
"""

system = """"You are an expert in summarizing texts in a precise and concise manner.
 Your task is to take the text I will provide below and generate a clear and relevant summary with ~100 words. 
 Make sure to capture the main idea and eliminate unnecessary details.
 You MUST RESPONSE directly with the resume. Do NOT add any introduction. 
"""

resume_prompt = ChatPromptTemplate.from_messages(
    [
      ("system", system),
      ("human", "Text to summarize: {abstract}")
    ]
)

summarize_chain = resume_prompt | llm