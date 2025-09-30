import pandas as pd
import os
import sys
from pathlib import Path

# Ajouter le dossier racine au PYTHONPATH
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.data.preprocessor import DataPreprocessor

def main():
    # Obtenir le chemin absolu du projet
    project_root = Path(__file__).parent.parent.parent
    data_file = os.path.join(project_root, 'data', 'raw', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
    # 1. Charger les données
    df = pd.read_csv(data_file)
    print(f"Données chargées avec succès. Shape: {df.shape}")
    
    # 2. Créer une instance du préprocesseur
    preprocessor = DataPreprocessor()
    
    # 3. Appliquer le preprocessing
    # Remplacez 'churn' par le nom de votre colonne cible
    X_train, X_val, X_test, y_train, y_val, y_test = preprocessor.preprocess_data(
        df=df,
        target_column='Churn'
    )
    
    # 4. Afficher les informations sur les données prétraitées
    print("\nInformations sur les données prétraitées :")
    print(f"Taille de l'ensemble d'entraînement : {X_train.shape}")
    print(f"Taille de l'ensemble de validation : {X_val.shape}")
    print(f"Taille de l'ensemble de test : {X_test.shape}")
    
    # 5. Sauvegarder les données prétraitées (optionnel)
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
