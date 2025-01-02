from dotenv import load_dotenv
load_dotenv()

from graph import graph

if __name__ == "__main__":
  graph.invoke(input={
    "user_interest": "Artificial Intelligence",
    "user_subinterest": ["AI", "AI Agents", "RAG"]
  })
