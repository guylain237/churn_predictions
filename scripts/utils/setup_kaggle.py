
"""Script pour configurer Kaggle"""

import shutil
import json
from pathlib import Path

def main():
    # Chemins
    source = Path(__file__).parent.parent / "kaggle.json"
    dest_dir = Path.home() / ".kaggle"
    dest = dest_dir / "kaggle.json"
    
    if not source.exists():
        print("❌ kaggle.json non trouvé")
        return
    
    # Créer répertoire et copier
    dest_dir.mkdir(exist_ok=True)
    shutil.copy2(source, dest)
    
    # Tester
    try:
        import kaggle
        kaggle.api.authenticate()
        print("✅ Kaggle configuré avec succès!")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()
