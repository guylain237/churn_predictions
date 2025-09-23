"""
Configuration du système de logging pour le projet
"""
import logging
import sys
from pathlib import Path
from datetime import datetime

def setup_logger(name: str = __name__) -> logging.Logger:
    """
    Configure et retourne un logger avec handlers pour console et fichier
    
    Args:
        name: Nom du logger (par défaut le nom du module)
        
    Returns:
        logging.Logger: Logger configuré
    """
    # Créer le dossier logs s'il n'existe pas
    log_dir = Path(__file__).parent.parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Nom du fichier de log avec timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{timestamp}.log"
    
    # Créer le logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Formatter pour les logs
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Handler pour la console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Handler pour le fichier
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Ajouter les handlers au logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Logger par défaut pour le projet
logger = setup_logger('churn_prediction')
