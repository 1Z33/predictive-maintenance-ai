from pathlib import Path
import pandas as pd

DEFAULT_DATA_PATH = Path("data/raw/ai4i2020.csv")

def load_dataset(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Charge le CSV AI4I 2020 sans modifier les données originales."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {path}. Téléchargez le CSV Kaggle et placez-le à cet emplacement."
        )
    return pd.read_csv(path)
