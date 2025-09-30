#!/usr/bin/env python3
"""
Script pour vérifier la configuration Kaggle
"""

import os
import json
from pathlib import Path

def check_kaggle_installation():
    """Vérifie si kaggle est installé"""
    try:
        import kaggle
        print("✅ Package kaggle installé")
        return True
    except ImportError:
        print("❌ Package kaggle non installé")
        print("   Installez avec: pip install kaggle")
        return False

def check_kaggle_credentials():
    """Vérifie si les credentials Kaggle sont configurés"""
    # Chemins possibles pour kaggle.json
    home_dir = Path.home()
    kaggle_dir = home_dir / ".kaggle"
    kaggle_json = kaggle_dir / "kaggle.json"
    
    # Vérifier aussi dans le répertoire courant
    current_kaggle_json = Path("kaggle.json")
    
    print(f"🔍 Recherche de kaggle.json dans:")
    print(f"   - {kaggle_json}")
    print(f"   - {current_kaggle_json}")
    
    if kaggle_json.exists():
        print(f"✅ Fichier kaggle.json trouvé: {kaggle_json}")
        return check_kaggle_json_content(kaggle_json)
    elif current_kaggle_json.exists():
        print(f"✅ Fichier kaggle.json trouvé: {current_kaggle_json}")
        print("⚠️ Déplacez le fichier vers ~/.kaggle/ pour plus de sécurité")
        return check_kaggle_json_content(current_kaggle_json)
    else:
        print("❌ Fichier kaggle.json non trouvé")
        print("📝 Pour créer kaggle.json:")
        print("   1. Allez sur https://www.kaggle.com/")
        print("   2. Connectez-vous à votre compte")
        print("   3. Allez dans Account > API")
        print("   4. Cliquez sur 'Create New API Token'")
        print("   5. Placez le fichier téléchargé dans ~/.kaggle/")
        return False

def check_kaggle_json_content(kaggle_json_path):
    """Vérifie le contenu du fichier kaggle.json"""
    try:
        with open(kaggle_json_path, 'r') as f:
            config = json.load(f)
        
        required_keys = ['username', 'key']
        missing_keys = [key for key in required_keys if key not in config]
        
        if missing_keys:
            print(f"❌ Clés manquantes dans kaggle.json: {missing_keys}")
            return False
        
        print("✅ Fichier kaggle.json valide")
        print(f"   Username: {config['username']}")
        print(f"   Key: {'*' * len(config['key'])}")
        
        # Vérifier les permissions (Unix/Linux/Mac)
        if os.name != 'nt':  # Pas Windows
            stat = kaggle_json_path.stat()
            permissions = oct(stat.st_mode)[-3:]
            if permissions != '600':
                print(f"⚠️ Permissions incorrectes: {permissions}")
                print("   Exécutez: chmod 600 ~/.kaggle/kaggle.json")
            else:
                print("✅ Permissions correctes (600)")
        
        return True
        
    except json.JSONDecodeError:
        print("❌ Fichier kaggle.json invalide (format JSON incorrect)")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de la lecture de kaggle.json: {e}")
        return False

def test_kaggle_api():
    """Teste l'API Kaggle"""
    try:
        import kaggle
        print("🧪 Test de l'API Kaggle...")
        
        # Tester une commande simple
        kaggle.api.authenticate()
        print("✅ Authentification Kaggle réussie")
        
        # Tester la recherche du dataset
        datasets = kaggle.api.dataset_list(search='telco customer churn', user='blastchar')
        if datasets:
            print("✅ Dataset 'blastchar/telco-customer-churn' trouvé")
            dataset = datasets[0]
            print(f"   Titre: {dataset.title}")
            print(f"   Taille: {dataset.size}")
            print(f"   Dernière mise à jour: {dataset.lastUpdated}")
        else:
            print("⚠️ Dataset non trouvé dans la recherche")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test de l'API: {e}")
        return False

def main():
    """Fonction principale"""
    print("🔧 Vérification de la configuration Kaggle")
    print("=" * 50)
    
    success_count = 0
    total_checks = 3
    
    # 1. Vérifier l'installation
    if check_kaggle_installation():
        success_count += 1
    
    print()
    
    # 2. Vérifier les credentials
    if check_kaggle_credentials():
        success_count += 1
    
    print()
    
    # 3. Tester l'API
    if success_count == 2:  # Seulement si les 2 premiers checks sont OK
        if test_kaggle_api():
            success_count += 1
    else:
        print("⏭️ Test de l'API ignoré (prérequis non satisfaits)")
    
    print()
    print("=" * 50)
    print(f"📊 Résultat: {success_count}/{total_checks} vérifications réussies")
    
    if success_count == total_checks:
        print("🎉 Configuration Kaggle complète et fonctionnelle!")
        print("Vous pouvez maintenant télécharger le dataset avec:")
        print("   python src/data/dataset.py")
    else:
        print("⚠️ Configuration incomplète. Suivez les instructions ci-dessus.")

if __name__ == "__main__":
    main()
