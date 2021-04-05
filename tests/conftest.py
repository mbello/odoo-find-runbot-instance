import pytest
import httpx

pytest_plugins = ["odoo_find_runbot_instance.pytest_fixtures"]


@pytest.fixture(scope="session")
def http_client():
    return httpx
