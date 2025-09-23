"""
Point d'entrée principal du projet de prédiction du churn client
"""
import os
import sys
from pathlib import Path

# Ajouter le dossier racine au PYTHONPATH
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Importer le script de téléchargement et le logger
from scripts.data.dowload_setup import main as setup_data
from src.utils.logger import logger

def main():
    """
    Fonction principale qui exécute toutes les étapes du projet dans l'ordre
    1. Téléchargement et configuration des données
    2. Préparation et analyse des données
    3. Entraînement des modèles
    4. Évaluation des performances
    5. Visualisation des résultats
    """
    logger.info("Démarrage du projet de prédiction du churn client")
    
    try:
        # Étape 1 : Téléchargement et configuration des données
        logger.info("Étape 1 : Téléchargement et configuration des données")
        setup_data()
        logger.info("Étape 1 terminée avec succès")
        
        # Les futures étapes seront ajoutées ici
        # TODO: Ajouter les autres étapes du projet
        
    except Exception as e:
        logger.error(f"Une erreur est survenue : {str(e)}", exc_info=True)
        sys.exit(1)
        
    logger.info("Exécution terminée avec succès")

if __name__ == "__main__":
    main()
