"""
Module d'évaluation des modèles de prédiction du churn
"""
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    roc_auc_score, confusion_matrix, classification_report
)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    def __init__(self):
        self.results = {}
        self.models = {}
    
    def evaluate_model(self, model, model_name: str, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
        """Évalue un modèle et retourne ses métriques"""
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred),
            'roc_auc': roc_auc_score(y_test, y_pred_proba),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
        self.results[model_name] = metrics
        self.models[model_name] = model
        
        return metrics
    
    def print_results(self):
        """Affiche les résultats de l'évaluation"""
        print("\n=== RÉSULTATS DE L'ÉVALUATION ===")
        for model_name, metrics in self.results.items():
            print(f"\n{model_name}:")
            print(f"Accuracy:  {metrics['accuracy']:.3f}")
            print(f"Precision: {metrics['precision']:.3f}")
            print(f"Recall:    {metrics['recall']:.3f}")
            print(f"F1-Score:  {metrics['f1_score']:.3f}")
            print(f"ROC-AUC:   {metrics['roc_auc']:.3f}")
            print("\nMatrice de confusion:")
            print(metrics['confusion_matrix'])
