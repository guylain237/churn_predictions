# 📖 Guide d'Utilisation - Dashboard Prédiction Churn

## 🚀 Comment Lancer le Dashboard

### Prérequis
- Python 3.8+ installé
- Dépendances installées : `pip install streamlit plotly pandas scikit-learn`
- Données préprocessées dans `data/processed/`

### Lancement
1. **Ouvrir un terminal** dans le dossier du projet
2. **Exécuter la commande :**
   ```bash
   streamlit run src/visualisation/dashboard.py
   ```
3. **Le dashboard s'ouvre automatiquement** dans votre navigateur à l'adresse `http://localhost:8501`

---

## 🎛️ Guide d'Utilisation par Page

### 📊 Page 1 : Vue d'Ensemble

**Objectif :** Aperçu général des performances du projet

**Contenu :**
- **Métriques clés** : Meilleur modèle, accuracy, ROC-AUC, nombre de clients analysés
- **Graphique comparatif** : Performance des 3 modèles sur toutes les métriques
- **Tableau récapitulatif** : Détail des scores par modèle

**Utilisation :**
- Consultez cette page pour avoir une vue d'ensemble rapide
- Utilisez le graphique pour comparer visuellement les modèles
- Le tableau donne les valeurs exactes pour vos rapports

---

### 🔮 Page 2 : Prédiction

**Objectif :** Simuler une prédiction de churn pour un nouveau client

**Formulaire de saisie :**

#### 📊 Informations Générales
- **Ancienneté** : Nombre de mois depuis l'inscription (0-72)
- **Charges mensuelles** : Montant facturé chaque mois (18-118$)
- **Charges totales** : Montant total depuis l'inscription

#### 🛠️ Services
- **Type de contrat** : Month-to-month / One year / Two year
- **Service Internet** : DSL / Fiber optic / No
- **Sécurité en ligne** : Yes / No / No internet service

**Interprétation des résultats :**

#### ✅ Client Fidèle (Probabilité < 50%)
- **Couleur verte** : Risque faible
- **Actions** : Maintenir la qualité de service
- **Suivi** : Standard

#### ⚠️ Risque de Churn (Probabilité > 50%)
- **Couleur rouge** : Risque élevé
- **Actions recommandées** automatiques selon le profil
- **Suivi** : Prioritaire

**Facteurs de risque affichés :**
- Contrat flexible (+40%)
- Client récent (+30%)
- Pas de sécurité (+20%)
- Charges élevées (+10%)

---

### 📈 Page 3 : Analyse des Modèles

**Objectif :** Analyser en détail chaque modèle ML

**Sélecteur de modèle :**
- Random Forest (recommandé production)
- Régression Logistique (meilleure discrimination)
- Arbre de Décision (plus interprétable)

**Graphique d'importance :**
- **Axe Y** : Noms des features
- **Axe X** : Score d'importance (0-1)
- **Couleur** : Spécifique à chaque modèle

**Métriques de performance :**
- **Accuracy** : Performance globale
- **Precision** : Réduction des faux positifs
- **Recall** : Détection des vrais churners
- **F1-Score** : Équilibre precision/recall
- **ROC-AUC** : Capacité de discrimination

---

### 💼 Page 4 : Insights Business

**Objectif :** Recommandations stratégiques pour l'entreprise

#### 🎯 Facteurs Clés de Churn
**Tableau interactif** avec :
- **Facteur** : Variable identifiée
- **Impact** : Pourcentage d'importance
- **Description** : Explication business

#### 🚀 Recommandations Stratégiques

**Actions Prioritaires :**
1. **Optimiser les contrats** (impact immédiat)
2. **Programme nouveaux clients** (prévention)
3. **Services additionnels** (fidélisation)

**KPIs de Suivi :**
- Taux de conversion contrats long-terme
- Taux de rétention nouveaux clients
- Adoption services additionnels
- Score de satisfaction par segment

#### 💰 Impact Financier
- **Réduction coûts** : 51.5% (moins de faux positifs)
- **Amélioration rétention** : +15% (actions ciblées)
- **ROI estimé** : 300% sur 12 mois

---

## 🎯 Conseils d'Utilisation

### Pour les Analystes
1. **Commencez par la Vue d'ensemble** pour le contexte
2. **Utilisez l'Analyse des Modèles** pour comprendre les prédictions
3. **Testez différents profils** dans la Prédiction

### Pour les Managers
1. **Consultez directement les Insights Business**
2. **Utilisez la Prédiction** pour des cas concrets
3. **Présentez la Vue d'ensemble** aux équipes

### Pour les Dirigeants
1. **Focalisez sur l'Impact Financier** (page 4)
2. **Validez avec des exemples** (page 2)
3. **Utilisez les KPIs** pour le suivi

---

## 🔧 Dépannage

### Erreur de chargement des données
- Vérifiez que les fichiers sont dans `data/processed/`
- Relancez le preprocessing si nécessaire

### Dashboard lent
- Fermez les autres applications
- Réduisez le nombre de features analysées

### Graphiques ne s'affichent pas
- Vérifiez la connexion internet (Plotly)
- Actualisez la page (F5)

---

## 📞 Support

Pour toute question ou problème :
1. Consultez ce guide
2. Vérifiez les logs dans le terminal
3. Contactez l'équipe Data Science

---

*Guide créé pour le Dashboard Prédiction Churn v1.0*
