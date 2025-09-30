# Projet de Prédiction du Churn Client

## Description

Ce projet développe un système de machine learning pour prédire le churn (désabonnement) des clients d'une entreprise de télécommunications. L'objectif est d'identifier proactivement les clients à risque de partir afin de mettre en place des stratégies de rétention ciblées.

## Résultats Principaux

- **Meilleur modèle :** Random Forest (74.3% accuracy, 83.2% ROC-AUC)
- **Facteur #1 de churn :** Type de contrat (40% d'importance)
- **ROI estimé :** Réduction de 51.5% des actions de rétention inutiles

## Comparaison des Modèles

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

## Structure du Projet

```
churn_prediction/
├── data/
│   ├── raw/                    # Données brutes (Telco Customer Churn)
│   └── processed/              # Données prétraitées et divisées
├── notebooks/
│   ├── 01_data_exploration.ipynb     # EDA et visualisations
│   ├── 02_data_preprocessing.ipynb   # Nettoyage et préparation
│   └── 03_model_development.ipynb    # Tests des modèles
├── src/
│   ├── data/
│   │   ├── dataset.py          # Gestion des données
│   │   ├── preprocessor.py     # Pipeline de preprocessing
│   │   └── process_data.py     # Traitement des données
│   ├── models/
│   │   ├── base_model.py       # Classe de base
│   │   ├── logistic_regression.py
│   │   ├── decision_tree.py
│   │   └── random_forest.py
│   ├── evaluation/
│   │   └── model_evaluator.py  # Évaluation des modèles
│   └── visualisation/
│       └── dashboard.py        # Dashboard Streamlit
├── scripts/
│   └── data/
│       └── download_setup.py   # Setup des données
├── docs/
│   ├── model_comparison_report.md
│   └── user_guide.md
├── results/                    # Résultats et visualisations
├── requirements.txt
├── main.py                     # Orchestration du pipeline
└── README.md
## Installation et Exécution

### 1. Configuration de l'Environnement
```bash
# Cloner le projet
git clone https://github.com/guylain237/churn_predictions.git
cd churn_prediction

# Créer et activer l'environnement virtuel
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Pipeline Complet (Automatique)
```bash
# Exécuter le pipeline complet
python main.py
```
Cette commande exécute automatiquement :
1. Téléchargement des données
2. Préparation et analyse
3. Entraînement et évaluation des modèles
4. Lancement du dashboard

### 3. Exécution Étape par Étape

#### 3.1 Téléchargement des Données et  Préparation des Données
```bash
python scripts/data/download_setup.py
```


#### 3.3 Analyse Exploratoire (Notebooks)(installation de anaconda nécessaire)
```bash
jupyter notebook notebooks/
```
Notebooks disponibles :
- `01_data_exploration.ipynb` : Analyse et visualisations
- `02_data_preprocessing.ipynb` : Détails du preprocessing
- `03_model_development.ipynb` : Développement des modèles
- `04_results_visualization.ipynb` : Visualisation des résultats

#### 3.4 Dashboard Interactif
```bash
streamlit run src/visualisation/dashboard.py
```


### Dashboard de Visualisation

#### Vue d'Ensemble
- **Métriques Principales**
  - Accuracy globale : 74.3%
  - ROC-AUC : 83.2%
  - Nombre de clients analysés : 7,043

#### Analyses Interactives

1. **Comparaison des Modèles**
   - Graphiques comparatifs des performances
   - Métriques détaillées (Accuracy, Precision, Recall, F1)
   - Matrices de confusion interactives
   - Courbes ROC

2. **Prédiction en Temps Réel**
   - Interface de saisie des données client
   - Prédiction instantanée du risque de churn
   - Probabilités détaillées
   - Recommandations personnalisées

3. **Analyse des Features**
   - Importance des variables par modèle
   - Visualisations des relations
   - Impact des features sur les prédictions

4. **Insights Business**
   - Facteurs clés de churn
   - Recommandations stratégiques
   - Analyse des segments clients
   - ROI estimé des actions

#### Fonctionnalités Techniques
- Mise à jour en temps réel
- Filtres interactifs
- Export des résultats
- Visualisations personnalisables

## Fonctionnalités Clés

### Modèles Implémentés
- **Régression Logistique** avec analyse des coefficients
- **Arbre de Décision** avec visualisation des règles
- **Random Forest** avec optimisation automatique des hyperparamètres

### Analyses Avancées
- **Matrices de confusion** interactives
- **Courbes ROC** comparatives  
- **Importance des features** par modèle
- **Visualisation de l'arbre de décision**
- **Optimisation automatique** des hyperparamètres

### Pipeline Complet
- **Préprocessing automatisé** (nettoyage, encodage, standardisation)
- **Évaluation multi-métriques** (accuracy, precision, recall, F1, ROC-AUC)
- **Sauvegarde des modèles** entraînés
- **Rapports automatiques** de performance

## Insights Business

### Facteurs Clés de Churn
1. **Type de contrat** (40% d'importance) - Contrats flexibles = risque élevé
2. **Ancienneté client** (11%) - Nouveaux clients plus volatiles  
3. **Montants facturés** (10%) - Relation complexe prix/fidélité
4. **Services additionnels** - Impact protecteur (OnlineSecurity, etc.)

### Recommandations Stratégiques
- **Priorité #1** : Optimiser les types de contrats (inciter long-terme)
- **Nouveaux clients** : Suivi renforcé les 6 premiers mois
- **Services additionnels** : Promouvoir les packages protecteurs
- **Pricing** : Réviser la stratégie tarifaire selon l'ancienneté

## Métriques et Performance

### Métriques d'Évaluation
- **Accuracy** : Performance globale du modèle
- **Precision** : Réduction des faux positifs (actions inutiles)
- **Recall** : Détection des vrais churners (ne pas les manquer)
- **F1-Score** : Équilibre precision/recall
- **ROC-AUC** : Capacité de discrimination

### Validation Robuste
- Division train/validation/test (70%/15%/15%)
- Validation croisée pour l'optimisation
- Métriques sur données non vues
- Analyse des matrices de confusion

## Configuration Technique



### Optimisations Implémentées
- **Parallélisation** (n_jobs=-1) pour Random Forest
- **Gestion du déséquilibre** (class_weight='balanced')
- **GridSearchCV** pour l'optimisation automatique
- **Sauvegarde/chargement** des modèles avec joblib

## Documentation

- **Rapport complet** : `docs/model_comparison_report.md`
- **Notebooks détaillés** avec analyses pas-à-pas
- **Code commenté** et docstrings complètes
- **Exemples d'utilisation** dans chaque module



*Projet développé pour la prédiction proactive du churn client*  
*Résultats : 74.3% accuracy avec Random Forest optimisé*