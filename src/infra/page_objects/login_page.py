from playwright.async_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        self.header = page.locator(".orangehrm-login-branding")
        self.header_logo = page.get_by_role("img", name="company-branding")
        self.login_title = page.get_by_role("heading", name="Login")
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.username_text = page.get_by_text("Username", exact=True)
        self.password_text = page.get_by_text("Password", exact=True)
        self.login_button = page.get_by_role("button", name="Login")
        self.forgot_password_link = page.get_by_text("Forgot your password?")
        self.footer = page.get_by_text("© 2005 - 2023 OrangeHRM, Inc. All rights reserved.")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.header).to_be_visible()
        await expect(self.login_title).to_be_visible()

    async def login(self, username: str, password: str) :
        await self.fill_username(username)
        await self.fill_password(password)
        await self.click_login_button()

    async def fill_username(self, username:str) :
        await self.username_field.fill(username)
    
    async def fill_password(self, password: str) :
        await self.password_field.fill(password)

    async def click_login_button(self) :
        await self.login_button.click()
    
    async def click_forgot_password(self) :
        await self.forgot_password_link.click()
    
    

