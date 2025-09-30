"""
Package src du projet Churn Prediction
"""
from pathlib import Path
import sys

# Ajout du répertoire racine au PYTHONPATH
ROOT_DIR = Path(__file__).parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
