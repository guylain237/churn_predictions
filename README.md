# 🎯 Projet de Prédiction du Churn Client

## 📋 Description

Ce projet développe un système de machine learning pour prédire le churn (désabonnement) des clients d'une entreprise de télécommunications. L'objectif est d'identifier proactivement les clients à risque de partir afin de mettre en place des stratégies de rétention ciblées.

## 🏆 Résultats Principaux

- **Meilleur modèle :** Random Forest (74.3% accuracy, 83.2% ROC-AUC)
- **Facteur #1 de churn :** Type de contrat (40% d'importance)
- **ROI estimé :** Réduction de 51.5% des actions de rétention inutiles

## 📊 Comparaison des Modèles

### Résultats Détaillés
```
=== COMPARAISON COMPLÈTE DES MODÈLES ===
           Régression Logistique  Arbre de Décision  Random Forest
accuracy                   0.739              0.732          0.743
precision                  0.509              0.501          0.515
recall                     0.778              0.736          0.778
f1                         0.616              0.596          0.620
roc_auc                    0.835              0.794          0.832

=== MEILLEUR MODÈLE PAR MÉTRIQUE ===
accuracy: Random Forest (0.743)
precision: Random Forest (0.515)
recall: Régression Logistique (0.778)
f1: Random Forest (0.620)
roc_auc: Régression Logistique (0.835)
```

### Usage Recommandé par Modèle
| Modèle | Usage Recommandé | Raison |
|--------|------------------|--------|
| **Random Forest** | **Production** | Meilleur équilibre général |
| **Régression Logistique** | **Analyse** | Meilleur recall et ROC-AUC |
| **Arbre de Décision** | **Communication** | Plus interprétable |

## 🏗️ Structure du Projet

```
churn_prediction/
├── data/
│   ├── raw/                    # Données brutes (Telco Customer Churn)
│   └── processed/              # Données prétraitées et divisées
├── notebooks/
│   ├── 01_data_exploration.ipynb     # Analyse exploratoire
│   ├── 02_data_preprocessing.ipynb   # Prétraitement des données
│   └── 03_model_development.ipynb    # Développement et comparaison des modèles
├── src/
│   ├── data/
│   │   ├── dataset.py          # Gestion des données
│   │   ├── preprocessor.py     # Pipeline de préprocessing
│   │   └── process_data.py     # Script de traitement des données
│   └── models/
│       ├── base_model.py       # Classe abstraite commune
│       ├── logistic_regression.py  # Modèle de régression logistique
│       ├── decision_tree.py    # Modèle d'arbre de décision
│       └── random_forest.py    # Modèle Random Forest (avec optimisation)
├── scripts/
│   └── data/
│       └── download_setup.py   # Téléchargement et setup automatique
├── docs/
│   └── model_comparison_report.md  # Rapport détaillé des résultats
├── models/                     # Modèles entraînés sauvegardés
├── requirements.txt
└── README.md
```

## 🚀 Installation et Utilisation

### 1. Setup Initial
```bash
git clone <repository-url>
cd churn_prediction
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Téléchargement Automatique des Données
```bash
python scripts/data/download_setup.py
```
*Télécharge automatiquement le dataset Kaggle et applique le préprocessing*

### 3. Exploration et Développement
```bash
# Lancer Jupyter
jupyter notebook

# Exécuter dans l'ordre :
# 1. notebooks/01_data_exploration.ipynb
# 2. notebooks/02_data_preprocessing.ipynb  
# 3. notebooks/03_model_development.ipynb
```

### 4. Utilisation Rapide des Modèles
```python
# Import des modèles
from src.models.random_forest import RandomForestModel
from src.models.logistic_regression import LogisticRegressionModel

# Chargement des données
import pandas as pd
X_train = pd.read_csv('data/processed/X_train.csv')
y_train = pd.read_csv('data/processed/y_train.csv')['0']

# Entraînement Random Forest
rf_model = RandomForestModel()
rf_model.train(X_train, y_train)

# Prédictions
predictions = rf_model.predict(X_test)
probabilities = rf_model.predict_proba(X_test)
```

## 🎯 Fonctionnalités Clés

### Modèles Implémentés
- ✅ **Régression Logistique** avec analyse des coefficients
- ✅ **Arbre de Décision** avec visualisation des règles
- ✅ **Random Forest** avec optimisation automatique des hyperparamètres

### Analyses Avancées
- 📊 **Matrices de confusion** interactives
- 📈 **Courbes ROC** comparatives  
- 🎯 **Importance des features** par modèle
- 🌳 **Visualisation de l'arbre de décision**
- ⚙️ **Optimisation automatique** des hyperparamètres

### Pipeline Complet
- 🔄 **Préprocessing automatisé** (nettoyage, encodage, standardisation)
- 📊 **Évaluation multi-métriques** (accuracy, precision, recall, F1, ROC-AUC)
- 💾 **Sauvegarde des modèles** entraînés
- 📋 **Rapports automatiques** de performance

## 📈 Insights Business

### Facteurs Clés de Churn
1. **Type de contrat** (40% d'importance) - Contrats flexibles = risque élevé
2. **Ancienneté client** (11%) - Nouveaux clients plus volatiles  
3. **Montants facturés** (10%) - Relation complexe prix/fidélité
4. **Services additionnels** - Impact protecteur (OnlineSecurity, etc.)

### Recommandations Stratégiques
- 🎯 **Priorité #1** : Optimiser les types de contrats (inciter long-terme)
- 👥 **Nouveaux clients** : Suivi renforcé les 6 premiers mois
- 📦 **Services additionnels** : Promouvoir les packages protecteurs
- 💰 **Pricing** : Réviser la stratégie tarifaire selon l'ancienneté

## 📊 Métriques et Performance

### Métriques d'Évaluation
- **Accuracy** : Performance globale du modèle
- **Precision** : Réduction des faux positifs (actions inutiles)
- **Recall** : Détection des vrais churners (ne pas les manquer)
- **F1-Score** : Équilibre precision/recall
- **ROC-AUC** : Capacité de discrimination

### Validation Robuste
- ✅ Division train/validation/test (70%/15%/15%)
- ✅ Validation croisée pour l'optimisation
- ✅ Métriques sur données non vues
- ✅ Analyse des matrices de confusion

## 🔧 Configuration Technique

### Dépendances Principales
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
kaggle>=1.5.0
```

### Optimisations Implémentées
- 🚀 **Parallélisation** (n_jobs=-1) pour Random Forest
- ⚖️ **Gestion du déséquilibre** (class_weight='balanced')
- 🎛️ **GridSearchCV** pour l'optimisation automatique
- 💾 **Sauvegarde/chargement** des modèles avec joblib

## 📚 Documentation

- 📋 **Rapport complet** : `docs/model_comparison_report.md`
- 📓 **Notebooks détaillés** avec analyses pas-à-pas
- 💡 **Code commenté** et docstrings complètes
- 🎯 **Exemples d'utilisation** dans chaque module

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/NouvelleFonctionnalite`)
3. Commit les changements (`git commit -m 'Ajout NouvelleFonctionnalite'`)
4. Push vers la branche (`git push origin feature/NouvelleFonctionnalite`)
5. Ouvrir une Pull Request


*🎯 Projet développé pour la prédiction proactive du churn client*  
*📊 Résultats : 74.3% accuracy avec Random Forest optimisé*