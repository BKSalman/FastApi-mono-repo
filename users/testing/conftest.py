import pytest
from conftest import ScopedSession, base_db  # type: ignore
from fastapi.testclient import TestClient

from users.testing.data import SeedData


@pytest.fixture(autouse=True, scope="session")
def seed_data(client: TestClient):

    db_connection = base_db.engine.connect()
    db_connection.begin()
    _ = ScopedSession(bind=db_connection)
    print('<=======> scope="session" <=======>')

    """
    run direct queries or better, hit the endpoints that generate the data you want
    """
    data = SeedData()

    for user in data.users:
        response = client.post("/api/users/", json=user)
        assert response.status_code == 200
        response = client.post("/api/users/login", json=user)
        assert response.status_code == 200
        data.users_tokens.append(response.json()["access_token"])

    print(f"{len(data.users)} users has been created")

    print('<=======> scope="session" <=======>')
    ScopedSession.remove()
    db_connection.commit()
