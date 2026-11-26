# Predictive Maintenance AI — AI4I 2020

Projet académique de BAC 3 GL & IA : conception et évaluation d'un modèle de Machine Learning pour prédire les défaillances d'équipements industriels.

> **Statut :** structure initiale. Les analyses et résultats seront ajoutés progressivement après inspection du CSV original.

## Dataset

- Source : [AI4I 2020 Predictive Maintenance Dataset — Kaggle](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020)
- Télécharger le CSV original et le placer dans `data/raw/`.
- Nom attendu par défaut : `ai4i2020.csv`.
- Ne pas publier le CSV sur GitHub sans vérifier sa licence et les conditions de redistribution. Le projet prévoit `.gitignore` pour les données locales.

## Environnement

Python 3.10 à 3.12 recommandé.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Dans VS Code, installer les extensions **Python** et **Jupyter**, puis sélectionner le kernel `.venv`.

## Démarrage

1. Placer le CSV dans `data/raw/ai4i2020.csv`.
2. Ouvrir `notebooks/01_audit_dataset.ipynb`.
3. Exécuter les cellules dans l'ordre.

## Arborescence

```text
data/raw/          données originales locales (ignorées par Git)
data/processed/    données préparées locales (ignorées par Git)
notebooks/         analyses reproductibles
src/               fonctions Python réutilisables
models/            modèles entraînés (ignorés par Git)
reports/figures/   graphiques exportés
app/               démonstrateur Streamlit (étape ultérieure)
tests/             tests de fonctions
```

## Méthodologie prévue

1. Cadrage scientifique et audit du dataset.
2. Analyse exploratoire.
3. Prétraitement et séparation train/test.
4. Modèles de référence puis modèles d'ensemble.
5. Évaluation adaptée au déséquilibre des classes (precision, recall, F1, PR-AUC, matrice de confusion).
6. Interprétation, limites et démonstrateur.

## Précautions méthodologiques

- Ne pas utiliser `UDI` comme variable prédictive.
- `Product ID` est un identifiant : ne pas l'utiliser comme variable prédictive sans justification.
- Les colonnes `TWF`, `HDF`, `PWF`, `OSF` et `RNF` décrivent les modes de panne. Elles risquent de révéler directement la cible `Machine failure` : elles seront exclues des prédicteurs du modèle principal.
- Le dataset est synthétique. Les résultats ne prouvent pas une performance équivalente sur des machines réelles d'une mine.
- La classe positive (défaillance) est rare : l'accuracy seule est insuffisante.
- Toute transformation, exclusion de variable et décision expérimentale devra être justifiée dans le rapport.

## Reproductibilité

Les versions installées seront figées dans `requirements-lock.txt` après validation de l'environnement. Les graines aléatoires seront fixées dans les expériences.

## Auteur

À compléter par l'étudiant.
