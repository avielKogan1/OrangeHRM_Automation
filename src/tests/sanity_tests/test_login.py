import pytest
import logging
from src.infra.page_objects.login.login_page import LoginPage
from src.infra.page_objects.platform.dashboard.dashboard_page import DashboardPage
from playwright.async_api import async_playwright


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    root = logging.getLogger()
    root.setLevel(logging.INFO)



@pytest.mark.asyncio
async def test_login_with_valid_credentials(datafile):
    async with async_playwright() as p:
        # Retrieving test data from external file fixture "datafile"
        jsondata = datafile

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Initializing Login page object
        login_page = LoginPage(page)
        # Initializing Dashboard page object
        dashboard_page = DashboardPage(page)

        # Go to login page
        await login_page.goto()

        # Verify Login Page loaded
        await login_page.verify_page_loaded()
        
        # Fill in user name
        await login_page.fill_username(jsondata["username"])

        # Fill in password
        await login_page.fill_password(jsondata["password"])

        # Click Login button
        await login_page.click_login_button()

        # Verify Dashboard page loaded
        await dashboard_page.verify_page_loaded()
        
            
@pytest.mark.asyncio
async def test_login_with_invalid_credentials(datafile):
    async with async_playwright() as p:
       # Retrieving test data from external file fixture "datafile"
        jsondata = datafile

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Initializing Login page object
        login_page = LoginPage(page)
        
        # Go to login page
        await login_page.goto()

        # Verify Login Page loaded
        await login_page.verify_page_loaded()
        

        # Fill in user name
        await login_page.fill_username(f"{jsondata['username']} invalid")

        # Fill in password
        await login_page.fill_password(f"{jsondata['password']} invalid")

        # Click Login button
        await login_page.click_login_button()

        # Verify error message appears
        await login_page.verify_error_message_visible()
        
              
        
            

    
            
