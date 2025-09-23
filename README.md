Churn_prediction/
├── data/
│   ├── raw/                    # Données brutes
│   ├── processed/              # Données nettoyées
│   └── external/               # Données externes (si nécessaire)
├── notebooks/
│   ├── 01_data_exploration.ipynb     # EDA et analyse qualité
│   ├── 02_data_preprocessing.ipynb   # Nettoyage et préparation
│   ├── 03_model_development.ipynb    # Développement modèles
│   ├── 04_model_evaluation.ipynb     # Évaluation et optimisation
│   └── 05_results_visualization.ipynb # Visualisations finales
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Chargement données
│   │   └── preprocessor.py     # Préprocessing
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py       # Classe de base
│   │   ├── logistic_regression.py
│   │   ├── decision_tree.py
│   │   └── random_forest.py
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── metrics.py          # Métriques d'évaluation
│   │   └── validation.py       # Validation croisée
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── eda_plots.py        # Graphiques EDA
│   │   └── model_plots.py      # Graphiques modèles
│   └── utils/
│       ├── __init__.py
│       ├── config.py           # Configuration
│       └── helpers.py          # Fonctions utilitaires
├── models/
│   ├── trained/                # Modèles entraînés
│   └── experiments/            # Expérimentations
├── reports/
│   ├── figures/                # Graphiques pour rapport
│   └── final_report.md         # Rapport final
├── dashboard/                  # Dashboard interactif (optionnel)
│   ├── app.py                  # Application Streamlit/Dash
│   └── components/             # Composants dashboard
├── tests/                      # Tests unitaires
├── requirements.txt            # Dépendances
├── setup.py                    # Installation package
├── .env                        # Variables d'environnement
├── .gitignore                  # Git ignore
└── README.md                   # Documentation projet