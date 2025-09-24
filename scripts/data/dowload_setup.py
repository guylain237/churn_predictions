"""
Script de téléchargement des données
"""
import os
import sys
from pathlib import Path
import pandas as pd

# Ajouter le dossier racine au PYTHONPATH
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.data import Dataset, DataPreprocessor

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

        print("\nPrétraitement des données...")
        # Créer une instance du préprocesseur
        preprocessor = DataPreprocessor()
    
        # Appliquer le preprocessing
        X_train, X_val, X_test, y_train, y_val, y_test = preprocessor.preprocess_data(
            df=df,
            target_column='Churn'
        )
        
        # Afficher les informations sur les données prétraitées
        print("\nInformations sur les données prétraitées :")
        print(f"Taille de l'ensemble d'entraînement : {X_train.shape}")
        print(f"Taille de l'ensemble de validation : {X_val.shape}")
        print(f"Taille de l'ensemble de test : {X_test.shape}")
        
        # Créer le dossier processed s'il n'existe pas
        processed_dir = os.path.join(project_root, 'data', 'processed')
        os.makedirs(processed_dir, exist_ok=True)
        
        # Sauvegarder les fichiers
        X_train.to_csv(os.path.join(processed_dir, 'X_train.csv'), index=False)
        X_val.to_csv(os.path.join(processed_dir, 'X_val.csv'), index=False)
        X_test.to_csv(os.path.join(processed_dir, 'X_test.csv'), index=False)
        y_train.to_csv(os.path.join(processed_dir, 'y_train.csv'), index=False)
        y_val.to_csv(os.path.join(processed_dir, 'y_val.csv'), index=False)
        y_test.to_csv(os.path.join(processed_dir, 'y_test.csv'), index=False)
        
        print("\nLes données prétraitées ont été sauvegardées dans le dossier 'data/processed/'")


if __name__ == "__main__":
    main()
