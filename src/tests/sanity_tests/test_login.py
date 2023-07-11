import pytest
from pytest_steps import test_steps, optional_step
import logging
from src.infra.page_objects.login.login_page import LoginPage
from src.infra.page_objects.platform.dashboard.dashboard_page import DashboardPage
from src.tests.test_data.test_data import User
from playwright.async_api import async_playwright, Page, Browser, BrowserContext


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    root = logging.getLogger()
    root.setLevel(logging.INFO)


@pytest.mark.asyncio
async def test_login_with_valid_credentials():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        user = User()
        logging.info(f"user created : {user.username}")
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        # Go to login page
        await login_page.goto()

        # Verify Login Page loaded
        await login_page.verify_page_loaded()
        

        # Fill in user name
        await login_page.fill_username(user.username)

        # Fill in password
        await login_page.fill_password(user.password)

        # Click Login button
        await login_page.click_login_button()

        # Verify Dashboard page loaded
        await dashboard_page.verify_page_loaded()
        
            
@pytest.mark.asyncio
async def test_login_with_invalid_credentials():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        user = User()
        logging.info(f"user created : {user.username}")
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        # Go to login page
        await login_page.goto()

        # Verify Login Page loaded
        await login_page.verify_page_loaded()
        

        # Fill in user name
        await login_page.fill_username("invalid")

        # Fill in password
        await login_page.fill_password("invalid")

        # Click Login button
        await login_page.click_login_button()

        # Verify error message appears
        await login_page.verify_error_message_visible()
        
              
        
            

    
            
