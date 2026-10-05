

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    page.wait_for_timeout(2000)

    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//button[@onclick="alertbox()"]').click()
    page.wait_for_timeout(2000)
    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(2000)
    page.locator('//a[@href="#Textbox"]').click()
    page.once("dialog", lambda dialog: dialog.accept("automation"))
    page.locator('//button[@onclick="promptbox()"]').click()
    page.wait_for_timeout(2000)