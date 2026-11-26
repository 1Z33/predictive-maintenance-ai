TARGET = "Machine failure"
IDENTIFIER_COLUMNS = ["UDI", "Product ID"]
FAILURE_MODE_COLUMNS = ["TWF", "HDF", "PWF", "OSF", "RNF"]

# Les prédicteurs seront confirmés après audit du fichier réel.
CANDIDATE_FEATURES = [
    "Type", "Air temperature [K]", "Process temperature [K]",
    "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"
]
