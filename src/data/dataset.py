import pandas as pd
import subprocess
import zipfile
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Dataset:
    def __init__(self, dataset_name=None, dataset_path=None):
        """
        Initialise la classe Dataset avec les paramètres de téléchargement et de chemin.
        """
        # Configuration pour le projet churn prediction
        self.dataset_name = dataset_name or os.getenv('DATASET_NAME', 'blastchar/telco-customer-churn')
        self.dataset_path = dataset_path or os.getenv('DATASET_PATH', 'data/raw')
        
        # Normaliser le chemin
        self.dataset_path = os.path.normpath(self.dataset_path)
        
        # Fichier CSV attendu pour le churn prediction
        self.csv_filename = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
        
        # Créer le dossier s'il n'existe pas
        os.makedirs(self.dataset_path, exist_ok=True)

    def data_already_downloaded(self):
        """
        Vérifie si le fichier du dataset churn est déjà présent.
        """
        csv_path = os.path.join(self.dataset_path, self.csv_filename)
        return os.path.exists(csv_path)

    def data_downloads(self):
        """
        Télécharge et extrait le dataset Telco Customer Churn si ce n'est pas déjà fait.
        """
        if self.data_already_downloaded():
            print(" Le dataset Telco Customer Churn existe déjà, téléchargement ignoré.")
            csv_path = os.path.join(self.dataset_path, self.csv_filename)
            df = pd.read_csv(csv_path)
            print(f" Dimensions: {df.shape[0]} lignes, {df.shape[1]} colonnes")
            return

        # Vérifier d'abord s'il y a déjà un fichier ZIP à extraire
        if self._extract_existing_zip():
            return

        # Sinon, essayer de télécharger
        try:
            print(f" Téléchargement du dataset: {self.dataset_name}")
            
            # Télécharger le dataset Kaggle
            result = subprocess.run([
                "kaggle", "datasets", "download", 
                "-d", self.dataset_name, 
                "-p", self.dataset_path
            ], check=True, capture_output=True, text=True)

            print(" Téléchargement terminé")

            # Extraire le fichier ZIP téléchargé
            self._extract_existing_zip()

        except subprocess.CalledProcessError as e:
            print(f" Erreur lors du téléchargement Kaggle: {e}")
            print("Vérifiez votre configuration Kaggle:")
            print("   1. Assurez-vous que kaggle est installé: pip install kaggle")
            print("   2. Configurez vos credentials Kaggle (kaggle.json)")
            print("   3. Vérifiez que le fichier kaggle.json est dans le bon répertoire:")
            print("      Windows: C:\\Users\\{username}\\.kaggle\\kaggle.json")
            print("      Linux/Mac: ~/.kaggle/kaggle.json")
            print("   4. Ou téléchargez manuellement depuis:")
            print("      https://www.kaggle.com/datasets/blastchar/telco-customer-churn")
            print("   5. Placez le fichier archive.zip téléchargé dans data/raw/")
            
        except Exception as e:
            print(f"Erreur inattendue: {e}")

    def _extract_existing_zip(self):
        """
        Cherche et extrait un fichier ZIP existant dans le répertoire
        """
        # Noms possibles pour le fichier ZIP
        possible_zip_names = [
            "archive.zip",  # Téléchargement manuel depuis Kaggle
            "telco-customer-churn.zip",  # Téléchargement automatique
            "blastchar-telco-customer-churn.zip"  # Autre variante possible
        ]
        
        # Chercher tous les fichiers ZIP
        zip_files = [f for f in os.listdir(self.dataset_path) if f.endswith('.zip')]
        
        if not zip_files:
            return False
        
        # Prioriser les noms connus, sinon prendre le premier trouvé
        zip_to_extract = None
        for preferred_name in possible_zip_names:
            if preferred_name in zip_files:
                zip_to_extract = preferred_name
                break
        
        if not zip_to_extract:
            zip_to_extract = zip_files[0]
        
        zip_path = os.path.join(self.dataset_path, zip_to_extract)
        
        try:
            print(f" Extraction du fichier ZIP: {zip_to_extract}")
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(self.dataset_path)

            # Supprimer le fichier ZIP après extraction
            os.remove(zip_path)
            print("Extraction terminée, fichier ZIP supprimé")

            # Vérifier que le fichier CSV est présent
            csv_path = os.path.join(self.dataset_path, self.csv_filename)
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                print(f"Dataset extrait avec succès!")
                print(f" Fichier: {self.csv_filename}")
                print(f" Dimensions: {df.shape[0]} lignes, {df.shape[1]} colonnes")
                return True
            else:
                print("Le fichier CSV attendu n'a pas été trouvé après extraction")
                self._list_downloaded_files()
                return False
                
        except zipfile.BadZipFile:
            print(f" Le fichier {zip_to_extract} n'est pas un fichier ZIP valide")
            return False
        except Exception as e:
            print(f" Erreur lors de l'extraction: {e}")
            return False

    def _list_downloaded_files(self):
        """
        Liste les fichiers téléchargés pour debug
        """
        print(" Fichiers présents dans le répertoire:")
        for file in os.listdir(self.dataset_path):
            file_path = os.path.join(self.dataset_path, file)
            if os.path.isfile(file_path):
                print(f"   - {file}")

    def load_data(self):
        """
        Charge le fichier CSV du dataset churn.
        """
        try:
            csv_path = os.path.join(self.dataset_path, self.csv_filename)
            
            if not os.path.exists(csv_path):
                print(f" Fichier non trouvé: {csv_path}")
                print("Exécutez d'abord data_downloads() pour télécharger le dataset")
                print("Ou téléchargez manuellement et placez archive.zip dans data/raw/")
                return None
                
            df = pd.read_csv(csv_path)
            print(f" Dataset chargé: {df.shape[0]} lignes, {df.shape[1]} colonnes")
            return df
            
        except FileNotFoundError as e:
            print(f" Fichier non trouvé: {e}")
            return None
        except pd.errors.EmptyDataError as e:
            print(f"Fichier vide: {e}")
            return None
        except Exception as e:
            print(f" Erreur inattendue lors du chargement: {e}")
            return None

    def get_dataset_info(self):
        """
        Retourne les informations sur le dataset
        """
        return {
            "dataset_name": self.dataset_name,
            "dataset_path": self.dataset_path,
            "csv_filename": self.csv_filename,
            "is_downloaded": self.data_already_downloaded()
        }
