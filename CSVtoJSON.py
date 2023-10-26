import pandas as pd
import json
# import argparse


def CSVtoJSON(inputfile, outputfile):         # A 3rd parameter can be added to select the column names to be processed
    if not inputfile.lower().endswith('.csv'):
        print('Expected a CSV File')
        return 0
    if not outputfile.lower().endswith('.json'):
        print('Expected a JSON file')
        return 0

    try:
        df = pd.read_csv(inputfile, delimiter=';')  # Utiliser le point virgule comme délimiteur

    # En ajoutant "usecols=selected_columns" dans la lecture de df cela selectionne les colonnes que l'on veut en sortie
    # df = pd.read_csv(inputfile, delimiter=';', usecols=selected_columns)
    except FileNotFoundError:
        print('CSV file not found')
        return 0

    # Sélectionner uniquement les colonnes spécifiées
    # df = df[selectedColumns]

    # Convertir le DataFrame en une liste de dictionnaires
    json_data = df.to_dict(orient='records')

    # Écrire les données JSON dans le fichier de sortie
    with open(outputfile, 'w') as f:
        json.dump(json_data, f, indent=4)


# Exemple d'utilisation :
# if __name__ == "__main__":
# Spécifiez les colonnes que vous voulez extraire et traiter
# selected_columns = ['IdNum', 'selected', 'sessionId', 'assetLabel', 'socketType', 'startTime']

CSVtoJSON('database_FAF1.csv', 'incitius.json')  # Add 3rd parameter if necessary for selected column
