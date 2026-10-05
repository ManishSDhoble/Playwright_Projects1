class registers:
    def __init__(self, page):
        self.page = page

        self.login_button = page.locator("(//span[text()='Log in'])[2]")
        self.register_link = page.locator("(//a[@href='/registratie'])[2]")

        self.first_name_input = page.locator("//input[@name='first_name']")
        self.surname = page.locator("//input[@name='surname']")
        self.email =  page.locator("//input[@type='email']")
        self.password = page.locator("(//input[@type='password'])[1]")
        self.confirm_password = page.locator("(//input[@type='password'])[2]")

        self.checkbox1 = page.locator("(//input[@type='checkbox'])[1]")
        self.checkbox2 = page.locator("(//input[@type='checkbox'])[2]")
        self.register_button = page.locator("//input[@id='register']")

        self.log = page.locator("(//a[@href='/login'])[2]")
        self.login_email_input = page.locator("//input[@type='email']")
        self.login_password_input = page.locator("//input[@type='password']")
        self.checkbox3 = page.locator("(//input[@type='checkbox'])[1]")
        self.logged_in_button = page.locator("//input[@id='btn_login']")


    def register(self):
        self.login_button.hover()
        self.register_link.click()
        self.first_name_input.fill("Manish")
        self.surname.fill("Dhobale")    
        self.email.fill("manishsdhobale2@gmail.com")
        self.password.fill("Manish@123")
        self.confirm_password.fill("Manish@123")
        self.checkbox1.click()
        self.checkbox2.click()
        self.register_button.click()

    def login(self):
        self.login_button.hover()
        self.log.click()
        self.login_email_input.fill("manishsdhobale2@gmail.com")
        self.login_password_input.fill("Manish@123")
        self.checkbox3.click()
        self.logged_in_button.click()
     