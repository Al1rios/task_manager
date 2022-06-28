from fastapi.testclient import TestClient
from fastapi import status
from task_manager.manager import app


def test_list_tasks_return_code_200():
    client = TestClient(app)
    resp = client.get("/tasks")
    assert resp.status_code == status.HTTP_200_OK