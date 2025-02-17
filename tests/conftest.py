import os
import pytest
from playwright.sync_api import sync_playwright
from pytest_django.live_server_helper import LiveServer

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture
def test_server(live_server: LiveServer):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        browser_context = browser.new_context(base_url=live_server.url)
        page = browser_context.new_page()
        yield page
        browser_context.close()
        browser.close()
