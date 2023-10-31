import csv

def clear_csv(csv_file):
  with open(csv_file, 'r', newline='') as readfile:
        reader = csv.reader(readfile)
        rows = list(reader)  # Read the CSV into a list of rows
        header = rows[0]  # Save the header row
  with open(csv_file, 'w', newline='') as writefile:
        writer = csv.writer(writefile)
        writer.writerows([header])  # Write back the header row

# Call the function and clean the .csv
clear_csv('names.csv') 

def insert_data(csv_file, data):
    with open(csv_file, 'a', newline='') as file:  # Use 'a' to append to the file
        writer = csv.writer(file)
        writer.writerow(data.values())  # Write the values of the dictionary as a new row

# Define data as a list of dictionaries
data = [
    {"Name": "Hugo", "Age": 32, "Gender": "M"},
    {"Name": "Pedro", "Age": 30, "Gender": "M"},
    {"Name": "Tânia", "Age": 32, "Gender": "F"},
    {"Name": "Rebelo", "Age": 32, "Gender": "M"},
    {"Name": "André", "Age": 30, "Gender": "M"},
]

# Insert data into 'names.csv'
for record in data:
    insert_data('names.csv', record)

def read_data(csv_file):
    total_age = 0
    people_count = 0
    with open(csv_file, 'r', newline='') as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            age = int(row['Age'])
            total_age += age
            people_count += 1

    if people_count > 0:
        average_age = total_age / people_count
        print(f"The average age is: {average_age:.2f}")
    else:
        print("No people data found in the file.")

read_data('names.csv')

