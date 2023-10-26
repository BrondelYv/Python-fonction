# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
# import random
""""
def somme(a):
    resultat = 0
    for x in a:
        resultat = resultat + x
    return resultat

def moyenne(b):
    test = 0
    for k in b:
        test += k
    return test

def moyenne(b):
    test = 0
    for k in b:
        test = k/len(b)
    return test


def moyenne(b):
    test1 = 0
    if len(b) > 0:
        test1 = somme(b)/len(b)
    return test1
"""
"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


""" IMPORTATION BIBLIOTHEQUES ET CHARGEMENT DES DONNEES """
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
# pd.set_option('display.max_row', 300)
# pd.set_option('display.max_column', 300)

# data = pd.read_excel(r'X:\Nouveau_dossier\2023-06-22_17-09-24_igriddisplay-xls-export.xls')

""" Affichage des 5 premières lignes de mes données """
# print(data.head(5))


"""  Analyse de la forme des données 
     Pour ne pas modifier mes données de base, il faut que je les copie dans ma dataframe : df 
     que j'utiliserai durant cette analyse des données 
     """

# df = data.copy()

""" Vérification des valeurs nulles dans ma dataframe et les sommées en les triant de façon asc """

# missing_rate = (df.isna().sum()/df.shape[0]).sort_values(ascending=True)

# print(missing_rate)

# print(df.shape)

# print(df.dtypes.value_counts().plot.pie())

# plt.figure(figsize=(5,5))
# sns.heatmap(df.isna(), cbar=False)
# plt.show()

# df.dtypes.values_counts().plot.pie()


"""  Analyse du fond  """

# 1. Visualisation initiale - Elimination des colonnes inutiles à notre étude

# df = df[df.columns[df.isna().sum()/df.shape[0] < 0.9]]

# colonnes_a_supp = ['selected','page','layer','Annot_ID','Annot_UID','Modification Date']

# df = df.drop('selected', axis=1)
# print(df)

""" Examen de la colonne game de prix  """
"""
print(df['gamme de prix'].value_counts())
sns.set_theme()
for col in df.select_dtypes('float'):
    plt.figure()
    sns.distplot(df[col])
    plt.show()
#print(col)
"""
# print(df.select_dtypes('float'))
# sns.distplot(df['priceOfKw'])
# plt.show()

# Variables Qualitatives

# for col in df.select_dtypes('object'):
# print(f'{col : <50} {df[col].unique()}')

# df.dtypes('gamme de prix')
# print(pd.crosstab(df['gamme de prix'], df['Layer']))

"""
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Chemin du fichier CSV en entrée
csv_file = Path('database_FAF1.csv')

# Utilise with_suffix pour obtenir les chemins des fichiers XML et JSON en sortie
xml_file = csv_file.with_suffix('.xml')
json_file = csv_file.with_suffix('.json')

# Ouvrir le fichier CSV en mode lecture
with csv_file.open(newline='') as csvfile:
    # Lire le contenu du CSV en tant que dictionnaire
    csvreader = csv.DictReader(csvfile)

    # Créer une liste pour stocker les données
    data = []

    # Lire chaque ligne du CSV et l'ajouter à la liste
    for row in csvreader:
        data.append(row)

# Convertir les données en format XML
root = ET.Element("Data")
for entry in data:
    item = ET.SubElement(root, "Entry")
    for key, value in entry.items():
        sub_element = ET.SubElement(item, key)
        sub_element.text = value

# Enregistrer le fichier XML en utilisant pathlib
ET.ElementTree(root).write(xml_file)

# Convertir les données en format JSON et les enregistrer en utilisant pathlib
with json_file.open('w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

"""

"""
def CSVtoXML(inputfile, outputfile):
    if not inputfile.lower().endswith('.csv'):
        print('Expected A CSV File')
        return 0
    if not outputfile.lower().endswith('.xml'):
        print('Expected a XML file')
        return 0

    try:
        df = pd.read_csv(inputfile)
    except FileNotFoundError:
        print('CSV file not found')
        return 0
    entireop = '<collection="data0">\n'
    att = df.columns
    rowop = ''
    for j in range(len(df)):
        for i in range(len(att)):

            if i == 0:
                rowop = rowop + f'<{att[i]} title="{df[att[i]][j]}">\n'
            elif i == len(att) - 1:
                rowop = rowop + f'<{att[i]}>{df[att[i]][j]}</{att[i]}>\n</{att[0]}>\n'
            else:
                rowop = rowop + f'<{att[i]}>{df[att[i]][j]}</{att[i]}>\n'
    entireop = entireop + rowop + '</collection>'
    with open(outputfile, 'w') as f:
        f.write(entireop)


CSVtoXML('data0.csv', 'example.xml')
"""

"""
t = "employee_birthday.txt"
k = "i.xml"

print(CSVtoXML(t, k))"""

"""
import csv
f = open('data0.csv')
csv_f = csv.reader(f)
data = []

for column in csv_f:
   data.append(column)
f.close()
"""
#print(data[1:])

"""
import csv

def convert_csv_to_xml(input_csv_file, output_xml_file):
    def convert_row(row):
        xml_row = "<Employee>\n"
        for cell in row:
            xml_row += f"    <field>{cell}</field>\n"
        xml_row += "</Employee>\n"
        return xml_row

    with open(input_csv_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Ignorer la première ligne si elle contient les en-têtes

        xml_data = []

        for row in csv_reader:
            if row:  # Vérifiez si la ligne n'est pas vide
                xml_data.append(convert_row(row))

    # Écrire toutes les données XML dans le fichier de sortie
    with open(output_xml_file, 'w') as xmlfile:
        xmlfile.write('<Employees>\n')  # Début de la balise racine
        xmlfile.write('\n'.join(xml_data))  # Écrire toutes les lignes converties en XML
        xmlfile.write('\n</Employees>')  # Fin de la balise racine


# Exemple d'utilisation :
if __name__ == "__main__":
    convert_csv_to_xml('database_FAF1.csv', 'test.xml')
"""

"""import csv

def convert_csv_to_xml(input_csv_file, output_xml_file):
    with open(input_csv_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')  # Utiliser la tabulation comme délimiteur
        next(csv_reader)  # Ignorer la première ligne si elle contient les en-têtes

        xml_data = []

        for row in csv_reader:
            if row:  # Vérifier si la ligne n'est pas vide
                xml_row = "<Employee>\n"
                for cell in row:
                    xml_row += f"    <field>{cell}</field>\n"
                xml_row += "</Employee>\n"
                xml_data.append(xml_row)

    # Écrire toutes les données XML dans le fichier de sortie
    with open(output_xml_file, 'w') as xmlfile:
        xmlfile.write('<Employees>\n')  # Début de la balise racine
        xmlfile.write('\n'.join(xml_data))  # Écrire toutes les lignes converties en XML
        xmlfile.write('\n</Employees>')  # Fin de la balise racine

# Exemple d'utilisation :
if __name__ == "__main__":
    convert_csv_to_xml('database_FAF1.csv', 'test00.xml')
"""
"""
import csv


def convert_csv_to_xml(input_csv_file, output_xml_file):
    with open(input_csv_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')  # Utiliser la tabulation comme délimiteur
        keys = next(csv_reader)  # Récupérer la première ligne des clés
        data = next(csv_reader)  # Récupérer la deuxième ligne des données

        xml_data = []

        # Ouvrir une balise <non_fichier>
        xml_data.append("<non_fichier>")

        for key, value in zip(keys, data):
            xml_data.append(f"    <{key}>{value}</{key}>")

        # Fermer la balise </non_fichier>
        xml_data.append("</non_fichier>")

    # Écrire les données XML dans le fichier de sortie
    with open(output_xml_file, 'w') as xmlfile:
        xmlfile.write('\n'.join(xml_data))


# Exemple d'utilisation :
if __name__ == "__main__":
    convert_csv_to_xml('database_FAF1.csv', 'yvell.xml')
"""


