import os
import csv


""" archivo = './assets/mail_server.log'
if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8", newline='\n') as file:
        data = file.read()
        # print(data, type(data))
        lines = data.strip('\n')
        for line in lines:
            print(line, type(line))
else:
    print(f'el archivo {archivo} no se encuentra') 
"""

""" 
archivo = './assets/books.csv'
if os.path.exists(archivo):
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(type(reader))
        for row in reader:
            if row['price'] == '':
                print(row)
else: 
    print(f'el archivo {archivo} no se encuentra')

 """
import csv


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})