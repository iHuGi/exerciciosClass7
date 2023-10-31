"""
ESCREVE UM PROGRAMA EM PYTHON QUE LÊ UM ARQUIVO CSV CONTENDO INFORMAÇÕES 
SOBRE UMA LISTA DE PRODUTOS (NOME, PREÇO E QUANTIDADE EM STOCK), E IMPRIME A 
LISTA DESSES PRODUTOS.

Passo 1: Importar o módulo CSV
Passo 2: Definir a função para ler o arquivo CSV e calcular a média de preço
Passo 3: Imprimir
"""
import csv

# Function to handle AVG price
def calculate_average_price(csv_file):
    total_price = 0
    product_count = 0

# Use of Try to check for possible errors and handle the situation.
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                price = float(row['Price'])
                total_price += price
                product_count += 1

        if product_count > 0:
            average_price = total_price / product_count
            return average_price
        else:
            return None

    except FileNotFoundError:
        print(f"The file '{csv_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# CSV file name
csv_file = 'produtos.csv'

average_price = calculate_average_price(csv_file)

# If products are found we print the AVG price.
if average_price is not None:
    print(f"Average Price of Products: ${average_price:.2f}")
else:
    print("No products found in the file.")

