"""
ESCREVE UM PROGRAMA EM PYTHON QUE LÊ UM ARQUIVO CSV CONTENDO INFORMAÇÕES 
SOBRE UMA LISTA DE PRODUTOS (NOME, PREÇO E QUANTIDADE EM STOCK), E ADICIONA UM 
NOVO PRODUTO À LISTA COM AS INFORMAÇÕES FORNECIDAS PELO UTILIZADOR.
"""

import csv

# Function to add a new product to the list
# The CSV was created manually by me, we only append data to it, the columns are already created.
def add_product(csv_file, new_product):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_product)

# CSV file name
csv_file = 'produtosv2.csv'

# Loops to handle user input and check if it is valid, if not user must insert a valid value
while True:
    new_name = input("Enter the name of the new product (or type 'exit' to stop): ")
    if new_name.lower() == 'exit':
        break

    while True:
        try:
            new_price = float(input("Enter the price of the new product: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")

    while True:
        try:
            new_quantity = int(input("Enter the stock quantity of the new product: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the quantity.")

    # Create a list with the information of the new product
    new_product = [new_name, new_price, new_quantity]

    # Add the new product to the CSV file
    add_product(csv_file, new_product)

print("Products added successfully.")
