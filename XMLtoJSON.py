import xml.etree.ElementTree as ET   # Utilise cette bibliothèque  pour analyser le fichier XML et extraire ses données.
import json


def XMLtoJSON(inputfile, outputfile):
    # Vérifiez que le fichier d'entrée est au format XML
    if not inputfile.lower().endswith('.xml'):
        print('Expected an XML File')
        return

    try:
        # Analyser le fichier XML
        tree = ET.parse(inputfile)
        root = tree.getroot()

        # Extraire les données XML dans une liste de dictionnaires
        data = []
        for item in root:
            row = {}
            for element in item:
                row[element.tag] = element.text
            data.append(row)

        # Écrire les données JSON dans un fichier JSON
        with open(outputfile, 'w') as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        print('XML file not found')


# Exemple d'utilisation :
# if __name__ == "__main__":

XMLtoJSON('facture00.xml', 'output00.json')
