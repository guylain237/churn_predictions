# 🎯 Projet Prédiction Churn — Présentation Complète

## Étape 1: Analyse Exploratoire (EDA)

* Dataset: Telco Customer Churn (7 043 clients, 19 variables, churn 26.5%)
* Constats: Contrat `Month-to-month` (+risque), ancienneté < 12 mois (volatil), absence `OnlineSecurity`
* Split: 70% train / 15% validation / 15% test

## Étape 2: Préprocessing

* Nettoyage: Conversion `TotalCharges`, harmonisation labels
* Encodage: One-hot catégorielles, standardisation numériques
* Exports: `data/processed/` → `dashboard.py`

## Étape 3: Modélisation & Comparaison

| Modèle | Accuracy | Precision | Recall | F1 | ROC-AUC |
|--------|----------|-----------|--------|-----|---------|
| **Random Forest** | **74.3%** | **51.5%** | **77.8%** | **62.0%** | **83.2%** |
| Régression Logistique | 73.9% | 50.9% | 77.8% | 61.6% | 83.5% |
| Arbre de Décision | 73.2% | 50.1% | 73.6% | 59.6% | 79.4% |

**Stratégie**: RF (production), LR (analyse), DT (communication)

## Étape 4: Validation & Robustesse

* Cross-validation: 5-fold, ±3.6%
* Tests: 53 tests → 100% OK (`docs/test_robustesse.md`)
* Performance finale: 76.4% accuracy ✅ PRODUCTION READY

## Étape 5: Dashboard (`src/visualisation/dashboard.py`)

* **Vue d'ensemble**: KPIs et comparaison
* **Prédiction**: Simulateur temps réel
* **Analyse**: Importance features
* **Insights**: Facteurs clés et actions

## Étape 6: Interprétation Business

### Top Facteurs Churn
1. **Contrat Month-to-month** (40%) → Migration long-terme
2. **Ancienneté < 12 mois** (11%) → Fidélisation
3. **Charges élevées** (10%) → Révision pricing
4. **Pas OnlineSecurity** (7%) → Cross-sell gratuit
5. **Pas téléphone** (5%) → Bundles

### Actions Prioritaires
- Incitations contrats 12-24 mois (-20%)
- Suivi nouveaux clients 6 mois
- OnlineSecurity gratuit 3 mois

## Étape 7: Améliorations

* Techniques: Calibration, SHAP, monitoring dérive
* Produit: Export PDF, historique, API CRM

## Étape 8: Impact Financier

* Gains: 525K€/an (actions ciblées, +15% rétention)
* Coûts: 22K€/an (infra, maintenance, formation)
* ROI: 2,386%


