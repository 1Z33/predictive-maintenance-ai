from src.schema import TARGET, IDENTIFIER_COLUMNS, FAILURE_MODE_COLUMNS

def test_target_name():
    assert TARGET == "Machine failure"

def test_identifier_and_failure_columns_are_separated():
    assert "UDI" in IDENTIFIER_COLUMNS
    assert "TWF" in FAILURE_MODE_COLUMNS
