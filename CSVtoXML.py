# import csv
import pandas as pd   # Importation de la bibliothèque Pandas pour la manipulation de données tabulaires

"""

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""

"""
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'; {row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
"""

"""
def convert_row(row):
    xml_row = "<Facture>\n"
    for cell in row:

        xml_row += f"    <field>{cell}</field>\n"
        xml_row += "</Facture>\n"
        return xml_row

    with open('database_FAF1.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Ignorer la première ligne si elle contient les en-têtes
        xml_data = []
        for row in csv_reader:
            if row:  # Vérifiez si la ligne n'est pas vide
                xml_data.append(convert_row(row))

    # Écrire toutes les données XML dans un fichier de sortie
    with open('output2.xml', 'w') as xmlfile:
        xmlfile.write('<Facture>\n')  # Début de la balise racine
        xmlfile.write('\n'.join(xml_data))  # Écrire toutes les lignes converties en XML
        xmlfile.write('\n</Facture>')  # Fin de la balise racine
"""


def CSVtoXML(inputfile, outputfile):  # A 3rd parameter can be added to select the column names to be processed

    # Vérifions si nos deux fichiers d'entrés se terminent par des extensions .csv et .xml
    if not inputfile.lower().endswith('.csv'):
        print('Expected a CSV File')
        return 0
    if not outputfile.lower().endswith('.xml'):
        print('Expected an XML file')
        return 0

    # Essayons de lire le fichier .csv avec Pandas en le stockant dans un Dataframe
    try:
        df = pd.read_csv(inputfile, delimiter=';')  # Utiliser les points virgule comme délimiteur

    # En ajoutant "usecols=selected_columns" dans la lecture de df cela selectionne les colonnes que l'on veut en sortie
    # df = pd.read_csv(inputfile, delimiter=';', usecols=selected_columns)
    except FileNotFoundError:
        print('CSV file not found')
        return 0

    # Spécifiez les colonnes que vous voulez extraire et traiter
    # selected_columns = ['id', 'select', 'sessionId', 'assetlabel', 'sockettype', 'startime']
    # Sélectionner uniquement les colonnes spécifiées
    # df = df[selected_columns]

    # Ouverture de mon fichier de sortie en mode écriture : 'w' avec l'ajout d'une extension en haut du fichier
    with open(outputfile, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<root>\n')

    # On fait une itération à travers chaque ligne de notre Dataframe
        for _, row in df.iterrows():
            f.write('    <non_fichier>\n')   # On ouvre une balise <non_fichier> pour chaque ligne

    # Une boucle itère à travers chaque colonne (champ) et sa valeur dans la ligne actuelle
    # Pour chaque colonne, une balise correspondante est ouverte, avec le nom de la colonne en tant que balise

            for col, value in row.items():
                f.write(f'        <{col}>{value}</{col}>\n')
            f.write('    </non_fichier>\n')

        f.write('</root>')  # Une fois que toutes les lignes ont été traitées, on ferme la balise racine du fichier XML.


# Spécifiez les colonnes que vous voulez extraire et traiter
# selected_columns = ['IdNum', 'selected', 'sessionId', 'assetLabel', 'socketType', 'startTime']

CSVtoXML('database_FAF1.csv', 'facture001.xml')    # Add 3rd parameter if necessary for selected column
