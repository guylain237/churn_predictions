from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .base_model import BaseModel

class LogisticRegressionModel(BaseModel):
    """
    Modèle de régression logistique pour la prédiction du churn.
    """
    def __init__(self):
        super().__init__(name="Régression Logistique")
        self.model = LogisticRegression(
            random_state=42,
            max_iter=1000,
            class_weight='balanced',  # Pour gérer le déséquilibre des classes
            C=1.0  # Paramètre de régularisation
        )
        
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """
        Entraîne le modèle de régression logistique.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
        """
        self.model.fit(X_train, y_train)
        
    def get_feature_importance(self, feature_names: list) -> pd.DataFrame:
        """
        Retourne l'importance des features basée sur les coefficients.
        
        Args:
            feature_names: Liste des noms des features
            
        Returns:
            DataFrame avec les importances des features
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de calculer l'importance des features")
            
        # Calculer l'importance absolue des features
        importance = pd.DataFrame({
            'feature': feature_names,
            'importance': np.abs(self.model.coef_[0]),
            'coefficient': self.model.coef_[0]  # Coefficients réels (peuvent être négatifs)
        })
        
        # Trier par importance décroissante
        return importance.sort_values('importance', ascending=False)
    
    def plot_feature_importance(self, feature_names: list, top_n: int = 10) -> None:
        """
        Affiche un graphique des features les plus importantes.
        
        Args:
            feature_names: Liste des noms des features
            top_n: Nombre de features à afficher (par défaut: 10)
        """
        importance = self.get_feature_importance(feature_names)
        top_features = importance.head(top_n)
        
        plt.figure(figsize=(10, 6))
        colors = ['red' if x < 0 else 'blue' for x in top_features['coefficient']]
        plt.barh(range(len(top_features)), top_features['importance'], color=colors)
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importance absolue')
        plt.title(f'Top {top_n} features les plus importantes\n(Rouge = impact négatif, Bleu = impact positif)')
        plt.tight_layout()
        plt.show()