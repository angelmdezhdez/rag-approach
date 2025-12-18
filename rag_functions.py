from google import genai
from config.settings import API_KEY
import os

client = genai.Client(api_key=API_KEY)

def get_data(data_dir: str) -> str:
    data = []
    with open(data_dir, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def get_context(data: list, question: str) -> str:
    context = ''
    for datum in data:
        if any(word in datum.lower() for word in question.lower().split()):
            context += datum + '\n'
    return context

def get_answer(question:str, data_dir: str) -> str:
    data = get_data(data_dir)
    context = get_context(data, question)
    prompt = f'Usa el siguiente contexto para responder la pregunta de la mejor manera posible. Quiero que la respuesta sea corta y si en el contexto no hay información del producto, indícalo.\n\nContexto:\n{context}\n\nPregunta: {question}\n\nRespuesta:'
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
)
    return str(response.text)
    