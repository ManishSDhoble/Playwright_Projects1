from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator('//input[@name="username"]').fill("Admin")
    page.locator('//input[@type="password"]').fill("admin123")
    page.screenshot(path='screen.png')  
    '''will save on project level'''
    page.screenshot(path='D://Python for Automation//Playwright//screen.png')
    page.locator('//button[@type="submit"]').click()
    page.wait_for_timeout(5000)
    page.go_back()
    page.wait_for_timeout(5000)
    page.go_forward()
    page.wait_for_timeout(5000)
    page.reload()
    page.wait_for_load_state("load")

