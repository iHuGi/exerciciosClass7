"""
RECEBEU UM FICHEIRO CSV DENOMINADO "NOTAS.CSV", QUE COTNEM INFORMAÇÕES SOBRE AS NOTAS DE ESTUDANTES.

O ficheiro tem a seguinte estrutura:

Nome,Nota 

AlicE,85 

Bob,92

Charlie,78

David,88

Eve,95

Crie um programa em Python que leia o ficheiro "notas.csv" e calcule a média das notas dos estudantes.
Em seguida, o programa deve imprimir a média das notas com duas casas decimais.
"""

import csv

# CSV file name, this file was create manually.
csv_file = 'notas.csv'

# Initialize variables to hold values that we will use to calculate the AVG.
total_grade = 0
student_count = 0

# Read the CSV file and calculate the total grade and count of students
with open(csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grade = float(row['Nota'])
        total_grade += grade
        student_count += 1

# Calculate the average grade and display it with two decimal places
if student_count > 0:
    average_grade = total_grade / student_count
    print(f"The average grade is: {average_grade:.2f}")
else:
    print("No student data found in the file.")

