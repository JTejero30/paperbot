from os import getenv
from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import ChatOllama

class OllamaModel:
  
  def __init__(self):
    self.model = self._create_model()

  def _create_model(self) -> ChatOllama:
    """
    Crea e instancia el modelo Ollama con la configuración necesaria.
    :return: Instancia del modelo Ollama
    """
    modelo= getenv("OLLAMA_MODEL")
    print(modelo)
    return ChatOllama(
        model=getenv("OLLAMA_MODEL"),
        temperature=0.0,
        num_predict=500,
        verbose=True
    )

  def get_model(self) -> ChatOllama:
    """
    Devuelve la instancia del modelo.
    :return: Instancia del modelo Ollama
    """
    return self.model
