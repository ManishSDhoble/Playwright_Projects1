from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.tranktechnologies.com/")
    # page.wait_for_timeout(2000)
    # country = page.locator('//select[@id="countrySelector"]').select_option("India")


#     # wait
    page.wait_for_load_state("load")
    
    verticals = page.locator('(//a[text()="Verticals"])[1]')
    
    Trading =  page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/trade-mob.png"]')

    trade1 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
    trade2 =page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
    trade3 = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
    trade4 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    trade5 = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
    trade6 = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
    trade7 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

    Retail_Ecommerce = page.locator('(//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/retailandecomm-mob.png"])')

    RE1 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
    RE2 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

    Healthcare = page.locator('//strong[text()="Healthcare"]')

    H1 = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    H2 = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

    Fintech = page.locator('(//strong[text()="Fintech"])')

    f1= page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    f2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')


    custom = page.locator('//strong[text()="Custom App"]')

    c1 = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    c2 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    c3 =page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    c4 = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
    c5 = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
    c6 = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
    c7 = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    c8 = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
    c9 = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')


    trading_list = [trade1,trade2,trade3,trade4,trade5,trade6,trade7]
    for i in trading_list:
        verticals.hover()
        Trading.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

    Retail_Ecommerce_list = [RE1,RE2]
    for i in Retail_Ecommerce_list:
        verticals.hover()
        Retail_Ecommerce.hover()
        i.click()
        print("url:",  page.url)
        page.wait_for_load_state("load")
        page.go_back()
        page.wait_for_load_state("load")

    Healthcare_list = [H1,H2]
    for i in Healthcare_list:
        verticals.hover()
        Healthcare.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")


    Fintech_list = [f1,f2]
    for i in Fintech_list:
        verticals.hover()
        Fintech.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

    custom_list = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
    for i in custom_list:
        verticals.hover()
        custom.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load") 
    


# Technologie
    Technologies = page.locator('(//a[text()="Technologies"])[1]')
    
    Ecom = page.locator('//strong[text()="eCommerce Development"]')

    ecom1 = page.locator('//a[text()="Magento Development"]')
    ecom2 = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
    ecom3 = page.locator('(//a[text()="Codeigniter Development"])[1]')
    ecom4 = page.locator('(//a[text()="WordPress Development"])[1]')
    ecom5 = page.locator('(//a[text()="Big Commerce"])[1]')
    ecom6 = page.locator('(//a[text()="Shopify Development"])[1]')
    ecom7 = page.locator('(//a[text()="CS-Cart Development"])[1]')
    ecom8 = page.locator('(//a[text()="Node JS Development"])[1]')
    ecom9 = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
    ecom10 = page.locator('(//a[text()="Woo Commerce"])[1]')
    ecom11= page.locator('(//a[text()="Laravel Development"])[1]')
    ecom12= page.locator('(//a[text()="Prestashop Development"])[1]')
    ecom13= page.locator('(//a[text()="Drupal Development"])[1]')
    ecom14= page.locator('(//a[text()="Wix Development"])[1]')
    ecom15= page.locator('(//a[text()="Joomla Development"])[1]')
    ecom16= page.locator('(//a[text()="React JS Development"])[1]')
    ecom17= page.locator('(//a[text()="Express JS Development"])[1]')


    mobileapp = page.locator('//strong[text()="Mobile App Development"]')

    m1 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    m1 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    m2 = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
    m3 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
    m4 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
    m5 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
    m6 = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
    m7 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
    m8 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    AI = page.locator('//strong[normalize-space()="Artificial Intelligence"]')

    Ecom_list = [ecom1,ecom2,ecom3,ecom4,ecom5,ecom6,ecom7,ecom8,ecom9,ecom10,ecom11,ecom12,ecom13,ecom14,ecom15,ecom16,ecom17]

    for i in Ecom_list:
        Technologies.hover()
        Ecom.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

    
    mobileapp_list = [m1,m2,m3,m4,m5,m6,m7,m8]

    for i in mobileapp_list:
        Technologies.hover()
        mobileapp.hover()
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

    page.wait_for_timeout(2000)

    Technologies.hover()
    AI.hover
    AI.click()
    print("url:",  page.url)
    page.go_back()



    # Blog page
    blog = page.locator('(//a[text()="Blog"])[1]')
    blog.click()
# # # Horizontal clicks
    HB1 = page.locator('(//a[text()="App Development"])[1]')
    HB2 = page.locator('(//a[text()="Web Development"])[1]')
    HB3 =  page.locator('(//a[text()="Software Development"])[1]')
    HB4 =  page.locator('(//a[text()="Digital Marketing"])[1]')
    HB5 = page.locator('(//a[text()="Email Marketing"])[1]')
    HB6 = page.locator('(//a[text()="Artificial Intelligence"])[2]')
    HB7 = page.locator('(//a[text()="UI UX Design"])[1]')

    horizontal_links = [HB1,HB2,HB3,HB4,HB5,HB6,HB7]

    blog.click()
    for i in horizontal_links:
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

# Categories
    Categ1 = page.locator('(//a[text()="App Development"])[3]')
    Categ2 = page.locator('(//a[text()="Artificial Intelligence"])[3]')
    Categ3 = page.locator('(//a[text()="Content Marketing"])')
    Categ4 = page.locator('(//a[text()="CRM Development"])[3]')
    Categ5 = page.locator('(//a[text()="Digital Marketing"])[2]')
    Categ6 = page.locator('(//a[text()="ECommerce Development"])[5]')
    Categ7 = page.locator('(//a[text()="Email Marketing"])[2]')
    Categ8 = page.locator('(//a[text()="Graphic Design"])[3]')
    Categ9 = page.locator('(//a[text()="Software & IT Company"])')
    Categ10 = page.locator('(//a[text()="Software Development"])[2]')
    Categ11 = page.locator('(//a[text()="UI UX Design"])[6]')
    Categ12 = page.locator('(//a[text()="Web Development"])[6]')

    categories_list = [Categ1,Categ2,Categ3,Categ4,Categ5,Categ6,Categ7,Categ8,Categ9,Categ10,Categ11,Categ12]
    blog.click()
    for i in categories_list:
        i.click()
        page.go_back()
        print("url:",  page.url)  
        page.wait_for_load_state("load")


    # LINKS

    webdev = page.locator('(//a[text()="Web Development"])[7]')
    webdev1 = page.locator('(//a[@href="/cms-website-development-company-in-india"])')
    webdev2 = page.locator('//a[@href="/ecommerce-web-development-company-in-india"]')
    t1 = page.locator('(//span[@class="toggle-btn"])[1]')
    webdev21 = page.locator('//a[@href="/website-development-company-in-delhi-ncr"]')
    t2= page.locator('(//span[@class="toggle-btn"])[2]')
    webdev3 = page.locator('//a[@href="/custom-web-portal-development-company-in-india"]')

    appdev = page.locator('(//a[text()="App Development"])[4]')
    appdev1= page.locator('//a[@href="/ios-mobile-app-development-company-in-india"]')
    appdev2 = page.locator('//a[@href="/android-mobile-app-development-company-in-india"]')

    appdev21 = page.locator('//a[@href="/android-app-development-company-in-delhi-ncr"]')
    appdev22 = page.locator('//a[@href="/app-development-company-in-delhi-ncr"]')


    appdev3 = page.locator('//a[@href="/hybrid-mobile-app-development-company-in-india"]')
    appdev4 = page.locator('//a[@href="/cross-platform-mobile-app-development-company-in-india"]')
    appdev5 = page.locator('//a[@href="/progressive-web-app-development-company-in-india"]')


    graphicsdev = page.locator('//a[@href="/graphic-design-company-in-india"]')
    graphicsdev1  = page.locator('//a[@href="/logo-design-company-in-india"]')
    graphicsdev2 = page.locator('//a[@href="/banner-design-company-in-india"]')
    graphicsdev3 = page.locator('//a[@href="/packaging-design-company-in-india"]')
    graphicsdev4 = page.locator('//a[@href="/business-cards-design-company-in-india"]')

    UIUXDEV = page.locator('//a[@href="/ui-ux-design-company-in-india"]')
    UIUXDEV1 = page.locator('//a[@href="/mobile-app-design-company-in-india"]')
    UIUXDEV2 = page.locator('//a[@href="/responsive-web-design-company-in-india"]')
    UIUXDEV3 = page.locator('//a[@href="/brand-identity-design-services-company-in-india"]')


    porfolio = page.locator('(//a[@href="#"])[10]')
    porfolio1 = page.locator('//a[@href="/assets/trank-profile.pdf"]')

    links = [webdev,webdev1,webdev2,webdev3,appdev,appdev1,appdev2,appdev3,appdev4,appdev5,graphicsdev,graphicsdev1,graphicsdev2,graphicsdev3,graphicsdev4,UIUXDEV,UIUXDEV1,UIUXDEV2,UIUXDEV3]

    blog.click()

    for i in links:
        i.click()
        print("url:",  page.url)
        page.go_back()
        page.wait_for_load_state("load")

    # Contact Us
    ContactUs= page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
    page.wait_for_timeout(2000)

    # form
    name = page.locator('(//input[@placeholder="Your Name"])[2]').fill("Manish S D")
    email = page.locator('(//input[@placeholder="Your Mail"])[2]').fill("manishsdhoble@gmail.com")
    page.once("dialog", lambda dialog : dialog.accept())
    page.screenshot(path="ss2.png")
    sendOTP = page.locator('(//button[text()="Send OTP"])[2]').click()
    page.screenshot(path="ss.png")
    enterOTP= page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("12345")
    company = page.locator('(//input[@placeholder="Your Company"])[2]').fill("ABC")

    service = page.locator('(//select[@name="service"])[2]').select_option("App Development")
    # selectoption = "App Development"
    phone =page.locator('(//input[@placeholder="Your Phone"])[2]').type("9876543210")
    message = page.locator('(//textarea[@placeholder="Message"])[2]').type("TRY TO AUTOMATE CAPTCHA FIRST THEN SUBMIT")
    page.screenshot(path="screenshot0.png")
    # captcha = page.locator('(//div[@role="presentation"])[2]').click()
    # page.screenshot(path="screenshot1.png")
    page.wait_for_timeout(1000)
    # page.screenshot(path="screenshot2.png")
    submit = page.locator('(//input[@value="Submit"])[2]').click()
    page.screenshot(path="screenshot3.png")
    page.wait_for_timeout(5000)

    # trading
    # stock trading
    # Request a Quote

    # page.locator('(//input[@placeholder="Your Name"])[2]')

    # page.locator('(//input[@placeholder="Your Mail"])[2]')
    # page.locator('(//input[@placeholder="Your Company"])[2]')
    # page.locator('(//select[@name="service"])[2]')
    # page.locator('(//input[@placeholder="Your Phone"])[2]')
    # page.locator('(//textarea[@placeholder="Message"])[2]')
    # page.locator('')

    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')
    # page.locator('')

    # page.locator('')
    # page.locator('')

    # page.locator('')
    # page.locator('')

    # page.locator('')
    # page.locator('')


    
