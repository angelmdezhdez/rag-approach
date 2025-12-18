import time
from rag_functions import *

QUESTIONS_FILE = 'data/questions_data.txt'
ASKED_FILE = 'data/questions_asked.txt'
ANSWERS_FILE = 'data/answers_data.txt'


def load_questions(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def save_questions(path, questions):
    with open(path, 'w', encoding='utf-8') as f:
        for q in questions:
            f.write(q + '\n')


questions = load_questions(QUESTIONS_FILE)

total = len(questions)

for i in range(total):
    if not questions:
        break

    question = questions.pop(0)

    answer = get_answer(question, 'data/articles_data.txt')

    print(f'Pregunta {i + 1} de {total}')

    with open(ANSWERS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'Pregunta: {question}\n')
        f.write(f'Respuesta: {answer}\n\n')

    with open(ASKED_FILE, 'a', encoding='utf-8') as f:
        f.write(question + '\n')

    save_questions(QUESTIONS_FILE, questions)

    time.sleep(20)
