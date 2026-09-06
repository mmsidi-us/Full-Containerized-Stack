from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test that / returns 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_health_endpoint():
    """Test that /health returns 200 with expected fields"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "chromadb" in data
    assert "ollama" in data

def test_stats_endpoint():
    """Test that /stats returns 200 with a document_count field"""
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "document_count" in data