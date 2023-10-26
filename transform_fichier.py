import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Chemin du fichier CSV en entrée
csv_file = Path('data.csv')

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
