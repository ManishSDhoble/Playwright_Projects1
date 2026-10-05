from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoblaze.com/")
    
    # signup
    # page.locator('//a[@id="signin2"]').click()
    # page.locator('//input[@id="recipient-email"]').fill("Manishsd")
    # page.locator('//input[@id="sign-password"]').type("Manish@123")
    # page.locator('//button[text()="Sign up"]').click()
    # page.wait_for_timeout(5000)
    
    # login
    page.locator('//a[@id="login2"]').click()
    page.locator('//input[@id="loginusername"]').fill("Manishsd")
    page.locator('//input[@id="loginpassword"]').fill("Manish@123")
    page.locator('//button[text()="Log in"]').click()

    # Add to cart
    page.locator('//a[text()="Samsung galaxy s6"]').click()
    # page.wait_for_timeout(1000)
    page.once("Dialog" ,lambda Dialog:Dialog.accept())
    # page.wait_for_timeout(1000)

    page.locator('//a[@onclick="addToCart(1)"]').click()
    page.once("Dialog" ,lambda Dialog:Dialog.accept())
    page.wait_for_timeout(1000)
    page.locator('//a[@href="cart.html"]').click()
    page.wait_for_timeout(1000)
    page.locator('//button[@data-target="#orderModal"]').click()
    page.wait_for_timeout(1000)
    page.locator('//input[@id="name"]').fill("Manish S D")
    page.locator('//input[@id="country"]').fill("India")
    page.locator('//input[@id="city"]').fill("NGP")
    page.locator('//input[@id="card"]').fill("pay")
    page.locator('//input[@id="month"]').fill("Jan")
    page.locator('//input[@id="year"]').fill("2002")
    page.locator('//button[@onclick="purchaseOrder()"]').click()

    page.wait_for_timeout(2000)

    




