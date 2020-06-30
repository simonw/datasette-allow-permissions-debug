from datasette.app import Datasette
import pytest
import httpx


@pytest.mark.asyncio
async def test_plugin_is_installed():
    app = Datasette([], memory=True).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/-/plugins.json")
        assert 200 == response.status_code
        installed_plugins = {p["name"] for p in response.json()}
        assert "datasette-allow-permissions-debug" in installed_plugins


@pytest.mark.asyncio
async def test_allows_access():
    app = Datasette([], memory=True).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/-/permissions")
        assert 200 == response.status_code
