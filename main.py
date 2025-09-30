"""
Point d'entrée principal du projet de prédiction du churn client
"""
import os
import sys
import pandas as pd
from pathlib import Path

# Ajouter le dossier racine au PYTHONPATH
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Importer le script de téléchargement et le logger
from scripts.data.dowload_setup import main as setup_data
from src.utils.logger import logger
# Créer et entraîner les modèles
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from src.evaluation.model_evaluator import ModelEvaluator

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
        
        # Étape 2 : Préparation des données
        logger.info("Étape 2 : Préparation des données")
        from src.data.process_data import main as process_data
        process_data()
        logger.info("Étape 2 terminée avec succès")
        
        # Étape 3 : Entraînement et évaluation des modèles
        logger.info("Étape 3 : Entraînement et évaluation des modèles")
        
        # Charger les données préparées
        X_train = pd.read_csv('data/processed/X_train.csv')
        X_test = pd.read_csv('data/processed/X_test.csv')
        y_train = pd.read_csv('data/processed/y_train.csv')['0']
        y_test = pd.read_csv('data/processed/y_test.csv')['0']
        
       
        
        # Random Forest
        rf_model = RandomForestClassifier(
            n_estimators=100, max_depth=10, min_samples_split=5,
            min_samples_leaf=2, random_state=42, class_weight='balanced', n_jobs=-1
        )
        
        # Régression Logistique
        lr_model = LogisticRegression(
            random_state=42, max_iter=1000, class_weight='balanced', C=1.0
        )
        
        # Arbre de Décision
        dt_model = DecisionTreeClassifier(
            max_depth=10, min_samples_split=20, min_samples_leaf=10,
            random_state=42, class_weight='balanced'
        )
        
        # Entraîner les modèles
        logger.info("Entraînement des modèles...")
        rf_model.fit(X_train, y_train)
        lr_model.fit(X_train, y_train)
        dt_model.fit(X_train, y_train)
        
        # Évaluer les modèles
        logger.info("Évaluation des modèles...")
        evaluator = ModelEvaluator()
        
        rf_metrics = evaluator.evaluate_model(rf_model, "Random Forest", X_test, y_test)
        lr_metrics = evaluator.evaluate_model(lr_model, "Régression Logistique", X_test, y_test)
        dt_metrics = evaluator.evaluate_model(dt_model, "Arbre de Décision", X_test, y_test)
        
        # Afficher les résultats
        evaluator.print_results()
        logger.info("Étape 3 terminée avec succès")
        
        # Étape 4 : Lancement du dashboard
        logger.info("Étape 4 : Lancement du dashboard Streamlit")
        import subprocess
        
        try:
            dashboard_path = os.path.join(project_root, 'src', 'visualisation', 'dashboard.py')
            logger.info(f"Démarrage du dashboard : {dashboard_path}")
            
            # Lancer Streamlit dans un processus séparé
            process = subprocess.Popen(
                [sys.executable, '-m', 'streamlit', 'run', dashboard_path],
                cwd=project_root
            )
            
            logger.info(" Dashboard lancé avec succès !")
            logger.info(" Accédez au dashboard sur : http://localhost:8501")
            logger.info(" Appuyez sur Ctrl+C pour arrêter le serveur")
            
            # Attendre que l'utilisateur arrête le processus
            process.wait()
            
        except KeyboardInterrupt:
            logger.info("\n  Dashboard arrêté par l'utilisateur")
        except Exception as e:
            logger.error(f"Erreur lors du lancement du dashboard : {str(e)}")
        
    except Exception as e:
        logger.error(f"Une erreur est survenue : {str(e)}", exc_info=True)
        sys.exit(1)
        
    logger.info("Exécution terminée avec succès")

if __name__ == "__main__":
    main()
