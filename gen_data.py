import numpy as np
import os
import random

articles = {
    # format: 'Article Name': [Price, threshold, price after threshold]
    'Pluma Negra': [3, 10, 2.5],
    'Pluma Azul': [2, 20, 1.5],
    'Pluma Roja': [5, 15, 4.0],
    'Cuaderno Rayas Grande': [20, 15, 18],
    'Cuaderno Rayas Chico': [10, 30, 8],
    'Cuaderno Cuadros Grande': [25, 10, 22],
    'Cuaderno Cuadros Chico': [12, 25, 10],
    'Mochila Escolar': [50, 5, 45],
    'Mochila Deportiva': [70, 3, 65],
    'Lápiz HB': [1, 50, 0.8],
    'Copias Carta': [0.50, 100, 0.30],
    'Copias Oficio': [0.75, 80, 0.50],
    'Borrador Grande': [8, 40, 6],
    'Borrador Chico': [4, 60, 3],
    'Cartulina Blanca': [15, 20, 12],
    'Cartulina de Color Pastel': [18, 15, 15],
    'Cartulina de Color Neón': [20, 10, 17],
    'Marcatextos Fluorescentes': [6, 30, 5],
    'Resistol Barra Grande': [10, 25, 8],
    'Resistol Barra Chico': [5, 50, 4],
    'Tijeras Escolar': [12, 15, 10],
    'Cutter Profesional': [15, 10, 12],
    'Libros para Colorear': [8, 20, 6],
    'Colores de Madera (10pzs)': [25, 15, 20],
    'Colores de Madera (24pzs)': [40, 10, 35],
    'Pegamento Líquido Chico': [7, 30, 5],
    'Pegamento Líquido Grande': [12, 20, 10],
    'Impresión a Color': [3, 50, 2],
    'Impresión Blanco y Negro': [2, 60, 1.5],
    'Folder Carta': [3, 100, 2.5], 
    'Folder Oficio': [4, 80, 3.5]
}

data = []

for article, details in articles.items():
    price = details[0]
    threshold = details[1]
    price_after_thresshold = details[2]
    data.append(f'{article}: precio por unidad: {price} pesos')
    data.append(f'{article} al mayoreo: {price_after_thresshold} pesos superior a {threshold} piezas')

random.shuffle(data)

with open('data/articles_data.txt', 'w') as file:
    for line in data:
        file.write(line + '\n')

questions = []

for article, details in articles.items():
    price = details[0]
    threshold = details[1]
    price_after_thresshold = details[2]
    questions.append(f'¿Cuánto cuesta {article}?')
    questions.append(f'¿Cuánto cuesta {article} al mayoreo?')

random.shuffle(questions)

with open('data/questions_data.txt', 'w') as file:
    for line in questions:
        file.write(line + '\n')

    file.write('¿Cuánto cuestan los autos de carreras?\n')
    file.write('¿Cuál es el precio de los juguetes?\n')
    file.write('¿Cuánto cuesta una computadora portátil?\n')
    file.write('¿Cuál es el precio de un teléfono móvil?\n')
    file.write('¿Cuánto cuesta una bicicleta?')