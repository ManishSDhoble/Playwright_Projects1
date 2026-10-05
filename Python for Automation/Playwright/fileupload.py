from playwright.sync_api import sync_playwright 
with sync_playwright()  as P:
    browser = P.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.goto("https://demo.automationtesting.in/Register.html")
    page.wait_for_load_state("load")
    # page.wait_for_timeout(5000)
# fill , type ,click
    page.locator('//input[@placeholder="Last Name"]').fill("manish")
    page.locator('//input[@placeholder="First Name"]').fill("Dhoble")
    page.locator('//textarea[@ng-model="Adress"]').type("nagpur, Maharashtra, India")
    page.locator('//input[@type="email"]').type("manish123@google.com")
    page.locator('//input[@type="tel"]').fill("9876898767")
    page.locator('//input[@value="Male"]').click()
    page.locator('//input[@id="checkbox1"]').click()
    page.locator('//input[@id="checkbox2"]').click()
    page.locator('//input[@id="checkbox3"]').click()

#DROPDOWN with select tagname
    page.locator('//select[@id="Skills"]').select_option("Adobe Photoshop")
    page.locator('//select[@id="yearbox"]').select_option("1995")
    page.locator('//select[@placeholder="Month"]').select_option("April")
    page.locator('//select[@id="daybox"]').select_option("13")

# set Passowrd
    page.locator('//input[@id="firstpassword"]').type('Manish@123')
    page.locator('//input[@id="secondpassword"]').type('Manish@123')

        # //select[@id="countries"]

# Dropdown with search bar - customise 
    page.locator('//span[@role="combobox"]').click()
    page.locator('//input[@role="textbox"]').type("ind")
    page.locator('//input[@role="textbox"]').press("Enter")

# dropdown with multiple option
    page.locator('//div[@id="msdd"]').click()
    lang1 = page.locator('//a[text()="Arabic"]')
    lang2 = page.locator('//a[text()="Bulgarian"]')
    lang3 = page.locator('//a[text()="Catalan"]')
    lang4 = page.locator('//a[text()="Croatian"]')

    Languages = [lang1,lang2,lang3,lang4]
    for i in Languages:
        i.click()
    # click outside to close the dropdown  
    page.locator('//label[text()="Languages"]').click()

    page.locator('//button[@id="submitbtn"]').click()

# file upload 
    page.set_input_files('//input[@id="imagesrc"]',"C://Users//Manish Shriram//Pictures//Screenshots//file.txt.png")
# Waits
    # page.pause()
    page.wait_for_timeout(5000)
    page.wait_for_load_state("load")
