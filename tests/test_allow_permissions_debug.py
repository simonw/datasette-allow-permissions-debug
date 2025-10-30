from datasette.app import Datasette
import pytest
import httpx


@pytest.mark.asyncio
async def test_plugin_is_installed():
    ds = Datasette([], memory=True)
    response = await ds.client.get("/-/plugins.json")
    assert 200 == response.status_code
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-allow-permissions-debug" in installed_plugins


@pytest.mark.asyncio
async def test_allows_access():
    ds = Datasette([], memory=True)
    response = await ds.client.get("/-/permissions")
    assert 200 == response.status_code
