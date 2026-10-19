import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "restaurant_health_analysis.ipynb"


def test_notebook_json_and_cells_are_valid() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["cells"]
    assert any(cell["cell_type"] == "code" for cell in notebook["cells"])


def test_notebook_has_no_saved_outputs_or_execution_counts() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            assert cell.get("outputs", []) == []
            assert cell.get("execution_count") is None


def test_dataset_path_is_explicit_and_typo_is_removed() -> None:
    source = NOTEBOOK.read_text(encoding="utf-8")
    assert "data/restaurants.csv" in source
    assert "resturent.csv" not in source
