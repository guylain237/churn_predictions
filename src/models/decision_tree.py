"""
Modèle d'arbre de décision pour la prédiction du churn.
"""
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .base_model import BaseModel

class DecisionTreeModel(BaseModel):
    """
    Modèle d'arbre de décision pour la prédiction du churn.
    """
    def __init__(self):
        super().__init__(name="Arbre de Décision")
        self.model = DecisionTreeClassifier(
            max_depth=10,              # Limite la profondeur pour éviter l'overfitting
            min_samples_split=20,      # Minimum d'échantillons pour créer une division
            min_samples_leaf=10,       # Minimum d'échantillons dans chaque feuille
            random_state=42,
            class_weight='balanced'    # Pour gérer le déséquilibre des classes
        )
        
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """
        Entraîne l'arbre de décision.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
        """
        self.model.fit(X_train, y_train)
        
    def get_feature_importance(self, feature_names: list) -> pd.DataFrame:
        """
        Retourne l'importance des features basée sur l'arbre de décision.
        
        Args:
            feature_names: Liste des noms des features
            
        Returns:
            DataFrame avec les importances des features
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de calculer l'importance des features")
            
        importance = pd.DataFrame({
            'feature': feature_names,
            'importance': self.model.feature_importances_
        })
        
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
        plt.barh(range(len(top_features)), top_features['importance'], color='green')
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importance')
        plt.title(f'Top {top_n} features les plus importantes - Arbre de Décision')
        plt.tight_layout()
        plt.show()
    
    def plot_tree_structure(self, feature_names: list, max_depth: int = 3) -> None:
        """
        Visualise la structure de l'arbre de décision.
        
        Args:
            feature_names: Liste des noms des features
            max_depth: Profondeur maximale à afficher (par défaut: 3)
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de visualiser l'arbre")
        
        plt.figure(figsize=(20, 10))
        plot_tree(
            self.model,
            feature_names=feature_names,
            class_names=['No Churn', 'Churn'],
            filled=True,
            rounded=True,
            fontsize=10,
            max_depth=max_depth
        )
        plt.title(f'Structure de l\'Arbre de Décision (profondeur max: {max_depth})')
        plt.show()
    
    def get_tree_rules(self, feature_names: list, max_rules: int = 10) -> list:
        """
        Extrait les règles de décision principales de l'arbre.
        
        Args:
            feature_names: Liste des noms des features
            max_rules: Nombre maximum de règles à retourner
            
        Returns:
            Liste des règles de décision
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant d'extraire les règles")
        
        tree = self.model.tree_
        rules = []
        
        def extract_rules(node, path=""):
            if tree.children_left[node] == tree.children_right[node]:  # Feuille
                class_name = "Churn" if tree.value[node][0][1] > tree.value[node][0][0] else "No Churn"
                confidence = max(tree.value[node][0]) / sum(tree.value[node][0])
                rules.append(f"{path} => {class_name} (confiance: {confidence:.2f})")
            else:
                feature = feature_names[tree.feature[node]]
                threshold = tree.threshold[node]
                
                # Branche gauche (<=)
                extract_rules(tree.children_left[node], 
                            f"{path} {feature} <= {threshold:.2f} AND")
                
                # Branche droite (>)
                extract_rules(tree.children_right[node], 
                            f"{path} {feature} > {threshold:.2f} AND")
        
        extract_rules(0)
        return rules[:max_rules]