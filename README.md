# Agente de IA para Búsqueda y Resumen de Papers Científicos

Este proyecto utiliza el framework **LangGraph** para crear un agente de inteligencia artificial que ayuda a los usuarios a mantenerse al día con la investigación científica.

## Descripción

Este agente de IA busca semanalmente los papers científicos más relevantes basados en los intereses del usuario. El agente:

- Realiza búsquedas según los temas e intereses proporcionados.
- Selecciona los papers más relevantes, categorizados según subintereses.
- Envía notificaciones por WhatsApp con resúmenes de los papers seleccionados y enlaces directos a los artículos.

El objetivo es simplificar el acceso a artículos científicos, proporcionando solo la información más relevante de manera rápida y accesible.

## Requisitos

- Python 3.x
- Framework LangGraph
- API de WhatsApp (como Twilio o similar)
- Acceso a bases de datos de papers científicos (por ejemplo, arXiv, PubMed, etc.)
