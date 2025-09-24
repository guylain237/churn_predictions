"""
Classe de base pour tous les modèles de prédiction du churn.
Définit l'interface commune et les méthodes d'évaluation.
"""

from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

class BaseModel(ABC):
    """
    Classe de base pour tous les modèles de prédiction du churn.
    Définit l'interface commune et les méthodes d'évaluation.
    """
    def __init__(self, name: str):
        self.name = name
        self.model = None
        
    @abstractmethod
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """
        Entraîne le modèle sur les données fournies.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
        """
        pass
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Fait des prédictions sur de nouvelles données.
        
        Args:
            X: Features pour la prédiction
            
        Returns:
            Prédictions (0 ou 1)
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de faire des prédictions")
        return self.model.predict(X)
    
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Prédit les probabilités pour chaque classe.
        
        Args:
            X: Features pour la prédiction
            
        Returns:
            Probabilités pour chaque classe
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de faire des prédictions")
        return self.model.predict_proba(X)
    
    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> dict:
        """
        Évalue le modèle sur les données fournies.
        
        Args:
            X: Features pour l'évaluation
            y: Labels réels
            
        Returns:
            Dictionnaire contenant les métriques d'évaluation
        """
        y_pred = self.predict(X)
        y_proba = self.predict_proba(X)[:, 1]  # Probabilité de la classe positive
        
        return {
            'accuracy': accuracy_score(y, y_pred),
            'precision': precision_score(y, y_pred),
            'recall': recall_score(y, y_pred),
            'f1': f1_score(y, y_pred),
            'roc_auc': roc_auc_score(y, y_proba)
        }
    
    def plot_confusion_matrix(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Affiche la matrice de confusion du modèle.
        
        Args:
            X: Features pour l'évaluation
            y: Labels réels
        """
        y_pred = self.predict(X)
        cm = confusion_matrix(y, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Matrice de confusion - {self.name}')
        plt.ylabel('Vrai label')
        plt.xlabel('Prédiction')
        plt.show()
    
    def plot_roc_curve(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Affiche la courbe ROC du modèle.
        
        Args:
            X: Features pour l'évaluation
            y: Labels réels
        """
        y_proba = self.predict_proba(X)[:, 1]
        fpr, tpr, _ = roc_curve(y, y_proba)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc_score(y, y_proba):.2f})')
        plt.plot([0, 1], [0, 1], 'k--')  # Ligne de référence
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Taux de faux positifs')
        plt.ylabel('Taux de vrais positifs')
        plt.title(f'Courbe ROC - {self.name}')
        plt.legend(loc="lower right")
        plt.show()
    
    def save_model(self, filepath: str) -> None:
        """
        Sauvegarde le modèle sur le disque.
        
        Args:
            filepath: Chemin où sauvegarder le modèle
        """
        if self.model is None:
            raise ValueError("Pas de modèle à sauvegarder")
        joblib.dump(self.model, filepath)
    
    @classmethod
    def load_model(cls, filepath: str) -> 'BaseModel':
        """
        Charge un modèle sauvegardé.
        
        Args:
            filepath: Chemin vers le modèle sauvegardé
            
        Returns:
            Instance du modèle chargé
        """
        model = cls(name=filepath.split('/')[-1])
        model.model = joblib.load(filepath)
        return model