"""
Script de téléchargement des données
"""
import os
import sys
from pathlib import Path

# Ajouter le dossier racine au PYTHONPATH
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.data import Dataset

def main():
    
    dataset = Dataset()
    
    print("Téléchargement du dataset Telco Customer Churn")
    print("=" * 60)
    
    # Afficher les informations
    info = dataset.get_dataset_info()
    print(f"Dataset: {info['dataset_name']}")
    print(f"Chemin: {info['dataset_path']}")
    print(f"Fichier: {info['csv_filename']}")
    print(f"Téléchargé: {info['is_downloaded']}")
    
    # Télécharger si nécessaire
    dataset.data_downloads()
    
    # Charger et afficher un aperçu
    df = dataset.load_data()
    if df is not None:
        print(f"\nAperçu des données:")
        print(df.head())
        print(f"\nDistribution du churn:")
        print(df['Churn'].value_counts())

if __name__ == "__main__":
    main()
