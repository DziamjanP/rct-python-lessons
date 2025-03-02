from fastapi.testclient import TestClient
from task import TaskModel
from reponses import TaskActionResponse
from main import app

client = TestClient(app)

task_id = 0

def test_task_add():
    r = client.post("/tasks", json={'title':'Test task', 'description':'test'})
    assert r.status_code == 200
    assert r.json()["code"] == 0
    global task_id
    task_id = int(r.json()["msg"])

    r = client.get(f"/tasks?id={task_id}")
    assert r.status_code == 200
    assert r.json()["tasks"][0] == TaskModel(id=task_id, title="Test task", description="test").model_dump()

def test_task_get_error():
    r = client.get(f"/tasks?id={task_id}&completed=True&limit=1")
    assert r.status_code == 404
    
def test_task_get_success():
    r = client.get(f"/tasks?id={task_id}")
    assert r.status_code == 200
    assert r.json()["tasks"][0] == TaskModel(id=task_id, title="Test task", description="test").model_dump()
    
def test_task_update():
    r = client.put(f"/tasks/{task_id}", json={"completed":True, "description":"new description"})
    assert r.status_code == 200
    assert r.json() == TaskActionResponse.make_success().model_dump()

    r = client.get(f"/tasks?id={task_id}")
    assert r.status_code == 200
    assert r.json()["tasks"][0] == TaskModel(id=task_id, title="Test task", description="new description", completed=True).model_dump()

def test_task_delete():
    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json() == TaskActionResponse.make_success().model_dump()

    r = client.get(f"/tasks?id={task_id}")
    assert r.status_code == 404