from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo= 500)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator('//input[@name="username"]').fill("Admin")
    page.locator('//input[@type="password"]').fill("admin123")
    page.locator('//button[@type="submit"]').click()
    page.wait_for_timeout(5000)