import pytest
from infra.page_objects.login.login_page import LoginPage
from playwright.async_api import async_playwright, Page, Browser
import logging


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    root = logging.getLogger()
    root.setLevel(logging.INFO)


@pytest.mark.asyncio
async def test_login_valid():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        login_page = LoginPage(page)
        await login_page.goto()
        await login_page.verify_page_loaded()
