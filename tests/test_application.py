from fastapi import FastAPI


def test_application_created(application):
    assert isinstance(application, FastAPI)


async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
