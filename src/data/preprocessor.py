import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
        # Définir les colonnes à traiter
        self.numeric_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
        self.categorical_columns = [
            'gender', 'Partner', 'Dependents', 'PhoneService',
            'MultipleLines', 'InternetService', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract',
            'PaperlessBilling', 'PaymentMethod'
        ]
        self.columns_to_drop = ['customerID']
        
    def clean_data(self, df):
        """
        Nettoie les données en gérant les valeurs manquantes et les doublons
        
        Args:
            df (pd.DataFrame): DataFrame à nettoyer
            
        Returns:
            pd.DataFrame: DataFrame nettoyé
        """
        # Créer une copie pour éviter de modifier les données originales
        df_clean = df.copy()
        
        # Supprimer les colonnes non nécessaires
        df_clean = df_clean.drop(columns=self.columns_to_drop, errors='ignore')
        
        # Convertir TotalCharges en numérique (car c'est une string dans le dataset)
        df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
        
        # Gérer les valeurs manquantes numériques
        for col in self.numeric_columns:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        
        # Gérer les valeurs manquantes catégorielles
        for col in self.categorical_columns:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
        
        return df_clean

    def encode_categorical(self, df):
        """
        Encode les variables catégorielles en utilisant LabelEncoder
        
        Args:
            df (pd.DataFrame): DataFrame avec variables catégorielles
            
        Returns:
            pd.DataFrame: DataFrame avec variables catégorielles encodées
        """
        # Créer une copie pour éviter de modifier les données originales
        df_encoded = df.copy()
        
        # Encoder uniquement les colonnes catégorielles spécifiées
        for col in self.categorical_columns:
            if col in df_encoded.columns:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                df_encoded[col] = self.label_encoders[col].fit_transform(df_encoded[col])
        
        return df_encoded

    def scale_numerical(self, df):
        """
        Standardise les variables numériques
        
        Args:
            df (pd.DataFrame): DataFrame avec variables numériques
            
        Returns:
            pd.DataFrame: DataFrame avec variables numériques standardisées
        """
        # Créer une copie pour éviter de modifier les données originales
        df_scaled = df.copy()
        
        # Standardiser uniquement les colonnes numériques spécifiées
        columns_to_scale = [col for col in self.numeric_columns if col in df_scaled.columns]
        if len(columns_to_scale) > 0:
            df_scaled[columns_to_scale] = self.scaler.fit_transform(df_scaled[columns_to_scale])
        
        return df_scaled

    def split_data(self, X, y, test_size=0.2, val_size=0.25):
        """
        Divise les données en ensembles train, validation et test
        
        Args:
            X (pd.DataFrame): Features
            y (pd.Series): Variable cible
            test_size (float): Proportion de données pour le test (par défaut 0.2 soit 20%)
            val_size (float): Proportion des données d'entraînement pour la validation (par défaut 0.25 soit 25%)
            
        Returns:
            tuple: (X_train, X_val, X_test, y_train, y_val, y_test)
        """
        # Première division : séparer les données de test
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Deuxième division : séparer les données de validation
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size, random_state=42
        )
        
        return X_train, X_val, X_test, y_train, y_val, y_test

    def preprocess_data(self, df, target_column):
        """
        Applique tout le pipeline de preprocessing sur les données
        
        Args:
            df (pd.DataFrame): DataFrame brut
            target_column (str): Nom de la colonne cible
            
        Returns:
            tuple: (X_train, X_val, X_test, y_train, y_val, y_test)
        """
        # Séparer features et target
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Nettoyer les données
        X = self.clean_data(X)
        
        # Encoder les variables catégorielles
        X = self.encode_categorical(X)
        
        # Encoder la variable cible
        if target_column not in self.label_encoders:
            self.label_encoders[target_column] = LabelEncoder()
        y = pd.Series(self.label_encoders[target_column].fit_transform(y), index=y.index)
        
        # Standardiser les variables numériques
        X = self.scale_numerical(X)
        
        # Diviser les données
        return self.split_data(X, y)