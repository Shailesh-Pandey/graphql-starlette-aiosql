import pytest
from starlette.testclient import TestClient
from api import app  # Replace with the actual module where your Starlette app is defined


import sys, asyncio
if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.fixture
def client():
    return TestClient(app)

def test_graphql_hello(client):
    # Define your GraphQL query
    query = """
    {
      hello
    }
    """

    # Make a POST request to the GraphQL API
    response = client.post("/graphql", json={"query": query})

    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"data": {"hello": "Hello world!"}}

def test_graphql_get_user_by_name(client):
    # Define your GraphQL query
    query = """
    {
      get_user_by_name(name: "example"){id,name,email}
    }
    """

    # Make a POST request to the GraphQL API
    response = client.post("/graphql", json={"query": query})

    print(response.json())
    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"data": { "get_user_by_name": {
      "id": "3",
      "name": "example",
      "email": "example@example.com"
    }
    }
    }

def test_graphql_experiment(client):
    # Define your GraphQL query
    query = """
    {
      experiment(num: 3)
    }
    """

    # Make a POST request to the GraphQL API
    response = client.post("/graphql", json={"query": query})

    print(response.json())
    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"data": { "experiment": "hello hello hello "
    }	}
