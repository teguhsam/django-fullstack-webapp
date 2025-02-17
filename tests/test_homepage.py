from playwright.sync_api import Page


def test_can_load_homepage(test_server: Page):
    test_server.goto("/")
    assert "Write and collaborate" in test_server.content()
