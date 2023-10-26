import xml.etree.ElementTree as ET
import pandas as pd


def XMLtoCSV(inputfile, outputfile):
    # Vérifiez que le fichier d'entrée est au format XML
    if not inputfile.lower().endswith('.xml'):
        print('Expected an XML File')
        return 0

    try:
        # Analyser le fichier XML
        tree = ET.parse(inputfile)
        root = tree.getroot()

        # Extraire les données XML dans un dictionnaire
        data = []
        for item in root:
            row = {}
            for element in item:
                row[element.tag] = element.text
            data.append(row)

        # Créer un DataFrame Pandas
        df = pd.DataFrame(data)

        # Écrire le DataFrame dans un fichier CSV
        df.to_csv(outputfile, index=False)

    except FileNotFoundError:
        print('XML file not found')


# Exemple d'utilisation :
# if __name__ == "__main__":

XMLtoCSV('facture00.xml', 'output00.csv')
