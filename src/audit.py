import pandas as pd

def audit_dataframe(df: pd.DataFrame) -> dict:
    """Retourne les contrôles descriptifs de base, sans altérer le DataFrame."""
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "target_distribution": (
            df["Machine failure"].value_counts(dropna=False).to_dict()
            if "Machine failure" in df.columns else None
        ),
    }
