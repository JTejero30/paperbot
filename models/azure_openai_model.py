from os import getenv
from langchain_openai import AzureChatOpenAI


class AzureOpenAiModel:
  def __init__(self):
    self.model = self._create_model()

  def _create_model(self) -> AzureChatOpenAI:
    """
    Crea e instancia el modelo AzureChatOpenAI con la configuración necesaria.
    :return: Instancia del modelo AzureChatOpenAI
    """
    return AzureChatOpenAI(
        deployment_name=getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
        openai_api_version=getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0.0,
        max_tokens=500,
        max_retries=3,
        verbose=True
    )

  def get_model(self) -> AzureChatOpenAI:
    """
    Devuelve la instancia del modelo.
    :return: Instancia del modelo AzureChatOpenAI
    """
    return self.model
