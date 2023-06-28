import pytest
from ....src.infra.page_objects.login_page import LoginPage
from playwright.sync_api import sync_playwright


# def browser():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch()
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()

async def test_perform_login():
    page = await browser.new_page()
    login_page = LoginPage(page)
    await login_page.verify_page_loaded()


