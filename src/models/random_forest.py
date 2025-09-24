"""
Modèle Random Forest pour la prédiction du churn.
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .base_model import BaseModel

class RandomForestModel(BaseModel):
    """
    Modèle Random Forest pour la prédiction du churn.
    """
    def __init__(self, n_estimators=100, max_depth=10, min_samples_split=5, min_samples_leaf=2):
        super().__init__(name="Random Forest")
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,     # Nombre d'arbres dans la forêt
            max_depth=max_depth,           # Profondeur maximale des arbres
            min_samples_split=min_samples_split,  # Minimum d'échantillons pour diviser
            min_samples_leaf=min_samples_leaf,    # Minimum d'échantillons par feuille
            random_state=42,
            class_weight='balanced',       # Pour gérer le déséquilibre des classes
            n_jobs=-1                     # Utilise tous les processeurs
        )
        
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """
        Entraîne le modèle Random Forest.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
        """
        self.model.fit(X_train, y_train)
        
    def get_feature_importance(self, feature_names: list) -> pd.DataFrame:
        """
        Retourne l'importance des features basée sur Random Forest.
        
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
        plt.barh(range(len(top_features)), top_features['importance'], color='purple')
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importance')
        plt.title(f'Top {top_n} features les plus importantes - Random Forest')
        plt.tight_layout()
        plt.show()
    
    def optimize_hyperparameters(self, X_train: pd.DataFrame, y_train: pd.Series, cv=3) -> dict:
        """
        Optimise les hyperparamètres du Random Forest avec GridSearchCV.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
            cv: Nombre de folds pour la validation croisée
            
        Returns:
            Dictionnaire des meilleurs paramètres
        """
        # Grille de paramètres à tester
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [5, 10, 15, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        # Recherche par grille avec validation croisée
        grid_search = GridSearchCV(
            estimator=RandomForestClassifier(random_state=42, class_weight='balanced', n_jobs=-1),
            param_grid=param_grid,
            cv=cv,
            scoring='roc_auc',  # Optimiser pour l'AUC
            n_jobs=-1,
            verbose=1
        )
        
        print("Optimisation des hyperparamètres en cours...")
        grid_search.fit(X_train, y_train)
        
        # Mettre à jour le modèle avec les meilleurs paramètres
        self.model = grid_search.best_estimator_
        
        print(f"Meilleurs paramètres : {grid_search.best_params_}")
        print(f"Meilleur score AUC : {grid_search.best_score_:.3f}")
        
        return grid_search.best_params_
    
    def get_tree_diversity(self) -> dict:
        """
        Analyse la diversité des arbres dans la forêt.
        
        Returns:
            Dictionnaire avec des statistiques sur la diversité
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant d'analyser la diversité")
        
        # Statistiques sur les arbres
        tree_depths = [tree.tree_.max_depth for tree in self.model.estimators_]
        tree_nodes = [tree.tree_.node_count for tree in self.model.estimators_]
        
        diversity_stats = {
            'n_estimators': self.model.n_estimators,
            'avg_depth': np.mean(tree_depths),
            'std_depth': np.std(tree_depths),
            'avg_nodes': np.mean(tree_nodes),
            'std_nodes': np.std(tree_nodes),
            'oob_score': getattr(self.model, 'oob_score_', 'Non disponible')
        }
        
        return diversity_stats
    
    def plot_learning_curve(self, X_train: pd.DataFrame, y_train: pd.Series, 
                           train_sizes: list = None) -> None:
        """
        Affiche la courbe d'apprentissage du Random Forest.
        
        Args:
            X_train: Features d'entraînement
            y_train: Labels d'entraînement
            train_sizes: Tailles d'entraînement à tester
        """
        from sklearn.model_selection import learning_curve
        
        if train_sizes is None:
            train_sizes = np.linspace(0.1, 1.0, 10)
        
        train_sizes, train_scores, val_scores = learning_curve(
            self.model, X_train, y_train, 
            train_sizes=train_sizes, cv=3, scoring='roc_auc', n_jobs=-1
        )
        
        plt.figure(figsize=(10, 6))
        plt.plot(train_sizes, np.mean(train_scores, axis=1), 'o-', label='Score d\'entraînement')
        plt.plot(train_sizes, np.mean(val_scores, axis=1), 'o-', label='Score de validation')
        plt.fill_between(train_sizes, np.mean(train_scores, axis=1) - np.std(train_scores, axis=1),
                         np.mean(train_scores, axis=1) + np.std(train_scores, axis=1), alpha=0.1)
        plt.fill_between(train_sizes, np.mean(val_scores, axis=1) - np.std(val_scores, axis=1),
                         np.mean(val_scores, axis=1) + np.std(val_scores, axis=1), alpha=0.1)
        
        plt.xlabel('Taille de l\'ensemble d\'entraînement')
        plt.ylabel('Score AUC')
        plt.title('Courbe d\'apprentissage - Random Forest')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()