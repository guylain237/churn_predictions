# Rapport de Comparaison des Modèles de Prédiction du Churn

## 📋 Résumé Exécutif

Ce rapport présente l'analyse comparative de trois modèles de machine learning pour la prédiction du churn client : Régression Logistique, Arbre de Décision et Random Forest.

**Recommandation principale :** Le **Random Forest** est recommandé pour la mise en production grâce à son équilibre optimal entre performance et robustesse.

## 🎯 Objectif du Projet

Développer un système de prédiction du churn client permettant d'identifier proactivement les clients à risque de partir, afin de mettre en place des actions de rétention ciblées.

## 📊 Données Utilisées

- **Dataset :** Telco Customer Churn
- **Taille :** 7,043 clients
- **Features :** 19 variables (démographiques, services, facturation)
- **Target :** Churn (Oui/Non) → encodé en (1/0)
- **Répartition :** 
  - Entraînement : 70%
  - Validation : 15%
  - Test : 15%

## 🔧 Préprocessing Appliqué

1. **Nettoyage des données**
   - Gestion des valeurs manquantes
   - Conversion des types de données

2. **Encodage des variables catégorielles**
   - LabelEncoder pour toutes les variables catégorielles
   - Encodage de la variable cible (No=0, Yes=1)

3. **Standardisation**
   - StandardScaler pour les variables numériques
   - Normalisation des échelles pour la régression logistique

## 🤖 Modèles Développés

### 1. Régression Logistique

**Configuration :**
```python
LogisticRegression(
    random_state=42,
    max_iter=1000,
    class_weight='balanced',
    C=1.0
)
```

**Avantages :**
- Coefficients interprétables (impact positif/négatif)
- Probabilités calibrées
- Rapide à entraîner
- Baseline solide

**Inconvénients :**
- Assume une relation linéaire
- Sensible aux outliers

### 2. Arbre de Décision

**Configuration :**
```python
DecisionTreeClassifier(
    max_depth=10,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42,
    class_weight='balanced'
)
```

**Avantages :**
- Règles de décision explicites
- Pas besoin de standardisation
- Capture les interactions non-linéaires
- Visualisation intuitive

**Inconvénients :**
- Tendance au surapprentissage
- Instabilité (sensible aux petits changements)

### 3. Random Forest

**Configuration :**
```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)
```

**Avantages :**
- Robuste au surapprentissage
- Gère bien les données déséquilibrées
- Importance des features fiable
- Performance généralement supérieure

**Inconvénients :**
- Moins interprétable qu'un arbre unique
- Plus lourd computationnellement

## 📈 Résultats de Performance

### Métriques de Validation

| Métrique | Régression Logistique | Arbre de Décision | Random Forest | **Gagnant** |
|----------|----------------------|-------------------|---------------|-------------|
| **Accuracy** | 73.9% | 73.2% | **74.3%** | Random Forest |
| **Precision** | 50.9% | 50.1% | **51.5%** | Random Forest |
| **Recall** | **77.8%** | 73.6% | 77.8% | Régression Logistique |
| **F1-Score** | 61.6% | 59.6% | **62.0%** | Random Forest |
| **ROC-AUC** | **83.5%** | 79.4% | 83.2% | Régression Logistique |

### Analyse des Matrices de Confusion

**Régression Logistique :**
- Vrais Positifs : 295 | Faux Positifs : 284
- Vrais Négatifs : 746 | Faux Négatifs : 84
- **Force :** Détection maximale des churners
- **Faiblesse :** Beaucoup de faux positifs (coûts inutiles)

**Random Forest :**
- Performances similaires mais avec moins de faux positifs
- **Équilibre optimal** entre détection et précision

## 🔍 Analyse de l'Importance des Features

### Top 5 Features par Modèle

**Régression Logistique :**
1. tenure (ancienneté) - Impact négatif
2. PhoneService - Impact négatif  
3. Contract - Impact négatif
4. MonthlyCharges - Impact positif
5. TotalCharges - Impact positif

**Arbre de Décision :**
1. Contract (40% d'importance)
2. TotalCharges (12%)
3. tenure (11%)
4. MonthlyCharges (10%)
5. OnlineSecurity (7%)

**Random Forest :**
- Distribution plus équilibrée des importances
- Confirmation des variables clés identifiées par les autres modèles

### Insights Business

1. **Contract** : Variable la plus prédictive du churn
2. **tenure** : Les nouveaux clients sont plus volatiles
3. **Charges** : Relation complexe entre prix et fidélité
4. **Services additionnels** : Impact protecteur (OnlineSecurity, etc.)

## 🎯 Recommandations

### Stratégie Multi-Modèles

1. **Production (Prédictions quotidiennes) :** **Random Forest**
   - Meilleur équilibre performance/robustesse
   - Moins de faux positifs = économies sur les actions de rétention

2. **Analyse exploratoire :** **Régression Logistique**
   - Coefficients interprétables
   - Détection maximale des churners
   - Analyse des tendances

3. **Communication business :** **Arbre de Décision**
   - Règles simples et actionnables
   - Visualisation intuitive pour les équipes métier

### Actions Business Prioritaires

1. **Optimisation des contrats** (impact #1)
   - Inciter aux contrats long-terme
   - Réviser les conditions des contrats flexibles

2. **Programme de fidélisation nouveaux clients**
   - Suivi renforcé les 6 premiers mois
   - Offres d'engagement progressives

3. **Services additionnels**
   - Promouvoir OnlineSecurity et autres services protecteurs
   - Packages attractifs pour augmenter l'engagement

## 🔧 Optimisations Réalisées

### Hyperparamètres Random Forest
- **Méthode :** GridSearchCV avec validation croisée (3-fold)
- **Métrique d'optimisation :** ROC-AUC
- **Paramètres testés :** n_estimators, max_depth, min_samples_split, min_samples_leaf
- **Amélioration :** +1.2% en accuracy après optimisation

## 📋 Prochaines Étapes

1. **Validation sur données de test**
   - Évaluation finale sur l'ensemble de test non vu
   - Confirmation des performances

2. **Déploiement**
   - Mise en production du Random Forest
   - Monitoring des performances en temps réel

3. **Améliorations futures**
   - Feature engineering avancé
   - Modèles d'ensemble (stacking)
   - Optimisation des seuils de décision

4. **A/B Testing**
   - Test des actions de rétention basées sur les prédictions
   - Mesure du ROI des interventions

## 📊 Conclusion

Le projet a démontré la faisabilité de prédire le churn avec une précision de **74.3%** et une capacité de discrimination excellente (**83.2% ROC-AUC**). 

Le **Random Forest** s'impose comme le modèle optimal pour la production, offrant le meilleur compromis entre performance, robustesse et réduction des faux positifs.

L'analyse révèle que le **type de contrat** est le facteur le plus critique, suivi de l'ancienneté client et des montants facturés, fournissant des leviers d'action clairs pour les équipes business.


