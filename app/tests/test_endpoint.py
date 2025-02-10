import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

@pytest.fixture
def sample_csv(tmp_path):
    csv_content = """HOTDOG,Germany,7.5
                    PIZZA,Italy,9.0
                    TACO,Mexico,8.5"""
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text(csv_content)
    return str(csv_path)