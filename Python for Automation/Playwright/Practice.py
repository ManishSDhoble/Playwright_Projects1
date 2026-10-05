# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False,slow_mo= 500)
#     page = browser.new_page()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.locator('//input[@name="username"]').fill("Admin")
#     page.locator('//input[@type="password"]').fill("admin123")
#     page.locator('//button[@type="submit"]').click()
#     page.wait_for_timeout(5000)

# from playwright.sync_api import sync_playwright 
# with sync_playwright()  as P:
#     browser = P.chromium.launch(headless=False)
#     page = browser.new_page()
#     # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     # page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.goto("https://demo.automationtesting.in/Register.html")
#     page.wait_for_load_state("load")
#     # page.wait_for_timeout(5000)
# # fill , type ,click
#     page.locator('//input[@placeholder="Last Name"]').fill("manish")
#     page.locator('//input[@placeholder="First Name"]').fill("Dhoble")
#     page.locator('//textarea[@ng-model="Adress"]').type("nagpur, Maharashtra, India")
#     page.locator('//input[@type="email"]').type("manish123@google.com")
#     page.locator('//input[@type="tel"]').fill("9876898767")
#     page.locator('//input[@value="Male"]').click()
#     page.locator('//input[@id="checkbox1"]').click()
#     page.locator('//input[@id="checkbox2"]').click()
#     page.locator('//input[@id="checkbox3"]').click()

# #DROPDOWN with select tagname
#     page.locator('//select[@id="Skills"]').select_option("Adobe Photoshop")
#     page.locator('//select[@id="yearbox"]').select_option("1995")
#     page.locator('//select[@placeholder="Month"]').select_option("April")
#     page.locator('//select[@id="daybox"]').select_option("13")

# # set Passowrd
#     page.locator('//input[@id="firstpassword"]').type('Manish@123')
#     page.locator('//input[@id="secondpassword"]').type('Manish@123')

#         # //select[@id="countries"]

# # Dropdown with search bar - customise 
#     page.locator('//span[@role="combobox"]').click()
#     page.locator('//input[@role="textbox"]').type("ind")
#     page.locator('//input[@role="textbox"]').press("Enter")

# # dropdown with multiple option
#     page.locator('//div[@id="msdd"]').click()
#     lang1 = page.locator('//a[text()="Arabic"]')
#     lang2 = page.locator('//a[text()="Bulgarian"]')
#     lang3 = page.locator('//a[text()="Catalan"]')
#     lang4 = page.locator('//a[text()="Croatian"]')

#     Languages = [lang1,lang2,lang3,lang4]
#     for i in Languages:
#         i.click()
#     # click outside to close the dropdown  
#     page.locator('//label[text()="Languages"]').click()

#     page.locator('//button[@id="submitbtn"]').click()

# # Waits
#     # page.pause()
#     page.wait_for_timeout(5000)
#     page.wait_for_load_state("load")


# mouse hover dropdown

'''
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://uncodemy.com/")

    Categories = page.locator('//span[@id="categoriesBtn"]')

    FSD = page.locator('//a[text()="Full-Stack-Development"]')
    DS = page.locator('//a[text()="Data Science"]')
    ST = page.locator('(//a[text()="Software Testing"])[1]')
    CT = page.locator('//a[text()="Cloud Tools"]')
    DM = page.locator('(//a[text()="Digital Marketing"])[1]')
    JT = page.locator('//a[text()="Java Technology+"]')
    NS = page.locator('//a[text()="Network & Security"]')
    PL = page.locator('//a[text()="Programming Language"]')
    CT = page.locator('//a[text()="CAD Training"]')
    GD = page.locator('(//a[text()="Graphic Designing"])[1]')

    # Full-Stack-Development

    FSD1 = page.locator('(//a[@href="/course/full-stack-with-nodejs-training-course-in-noida"])[1]')
    FSD2 = page.locator('(//a[@href="/course/python-full-stack-training-course-in-noida"])[1]')
    FSD3 = page.locator('(//a[@href="/course/java-full-stack-using-react-training-course-in-noida"])[1]')
    FSD4 = page.locator('(//a[@href="/course/web-designing-training-course-in-noida"])[1]')
    FSD5 = page.locator('(//a[@href="/course/web-development-training-course-in-noida"])[1]')
    FSD6 = page.locator('(//a[@href="/course/frontend-development-training-course-in-noida"])[1]')
    FSD7 = page.locator('(//a[@href="/course/angular-training-course-in-noida"])[1]')
    FSD8 = page.locator('(//a[@href="/course/react-js-training-course-in-noida"])[1]')
    FSD9 = page.locator('(//a[@href="/course/data-structure-and-algorithm-training-course-in-noida"])[1]')
    FSD10 = page.locator('(//a[@href="/course/mean-stack-development-training-course-in-noida"])[1]')
    FSD11 =page.locator('(//a[@href="/course/mern-stack-development-training-course-in-noida"])[1]')
   
    # Data Science
    
    DS1 = page.locator('(//a[@href="/course/python-training-course-in-noida"])[1]')
    DS2 = page.locator('(//a[@href="/course/data-analytics-using-python-training-course-in-noida"])[1]')
    DS3 = page.locator('(//a[@href="/course/data-science-machine-learning-using-python-training-course-in-noida"])[1]')
    DS4 = page.locator('(//a[@href="/course/machine-learning-using-python-training-course-in-noida"])[1]')
    DS5 = page.locator('(//a[@href="/course/ai-using-python-training-course-in-noida"])[1]')

    # Software Testing 
    ST1 = page.locator('(//a[@href="/course/software-testing-training-course-in-noida"])[1]')
    ST2 = page.locator('(//a[@href="/course/automation-testing-course-in-noida"])[1]')
    ST3 = page.locator('(//a[@href="/course/playwright-training-course-in-noida"])[1]')
    ST4 = page.locator('(//a[@href="/course/manual-testing-course-in-noida"])[1]')
    ST5 = page.locator('(//a[@href="/course/istqb-training-course-in-noida"])[1]')
    ST6 = page.locator('//a[text()="Manual + Selenium"]')

    # Cloud Tools
    CT1 = page.locator('(//a[@href="/course/microsoft-azure-training-course-in-noida"])[1]')
    CT2 = page.locator('(//a[@href="/course/devops-training-course-in-noida"])[1]')
    CT3 = page.locator('(//a[@href="/course/aws-training-course-in-noida"])[1]')
    CT4 = page.locator('(//a[@href="/course/cloud-computing-training-course-in-noida"])[1]')
    CT5 = page.locator('(//a[@href="/course/salesforce-training-course-in-noida"])[1]')

    # Digital Marketting
    DM1 = page.locator('(//a[@href="/course/digital-marketing-training-course-in-noida"])[1]')
    DM2 = page.locator('(//a[@href="/course/advance-digital-marketing-training-course-in-noida"])[1]')
    DM3 = page.locator('(//a[@href="/course/seo-training-course-in-noida"])[1]')

    # Java Training
    JT1 = page.locator('(//a[@href="/course/java-training-course-in-noida"])[1]')
    JT2 = page.locator('(//a[@href="/course/java-for-beginners-training-course-in-noida"])[1]')
    JT3 = page.locator('(//a[@href="/course/java-expert-training-course-in-noida"])[1]')
    JT4 = page.locator('(//a[@href="/course/spring-boot-microservices-security-with-hibernate-training-course-in-noida"])[1]')

    # Network and Security
    NS1 = page.locator('(//a[@href="/course/ethical-hacking-course-in-noida"])[1]')
    NS2 = page.locator('(//a[@href="/course/cyber-security-training-course-in-noida"])[1]')
    NS3 = page.locator('(//a[@href="/course/ccnp-training-course-in-noida"])[1]')
    NS4 = page.locator('(//a[@href="/course/mcsa-training-course-in-noida"])[1]')
    NS5 = page.locator('(//a[@href="/course/vmware-training-course-in-noida"])[1]')

    #Programming Languages
    PL1 = page.locator('(//a[@href="/course/c-with-data-structure-and-algorithm-training-course-in-noida"])[1]')
    PL2 = page.locator('(//a[@href="/course/cpptraining-training-course-in-noida"])[1]')
    PL3 = page.locator('(//a[@href="/course/net-4-months-training-course-in-noida"])[1]')
    PL4 = page.locator('(//a[@href="/course/dotnet-full-stack-training-course-in-noida"])[1]')
    PL5 = page.locator('(//a[@href="/course/r-programming-training-course-in-noida"])[1]')

    #CAD Training
    CT1 = page.locator('(//a[@href="/course/autocad-training-course-in-noida"])[1]')
    CT2= page.locator('(//a[@href="/course/cnc-programming-training-course-in-noida"])[1]')

    # Graphics Design
    GD1 = page.locator('(//a[@href="/course/graphic-designing-training-course-in-noida"])[1]')
    GD2 = page.locator('(//a[@href="/course/uiux-training-course-in-noida"])[1]')

    # page.locator('')
    # page.locator('')
    # page.locator('')


    FSD_LIST = [FSD1,FSD2,FSD3,FSD4,FSD5,FSD6,FSD7,FSD8,FSD9,FSD10,FSD11]
    DS_LIST = [DS1,DS2,DS3,DS4,DS5]
    ST_LIST = [ST1,ST2,ST3,ST4,ST5,ST6]
    CT_LIST = [CT1,CT2,CT3,CT4,CT5]
    DM_LIST = [DM1,DM2,DM3]
    JT_LIST = [JT1,JT2,JT3,JT4]
    NS_LIST = [NS1,NS2,NS3,NS4,NS5]
    PL_LIST = [PL1,PL2,PL3,PL4,PL5]
    CT_LIST = [CT1,CT2]
    GD_LIST = [GD1,GD2]



    for i in FSD_LIST:
            Categories.hover()
            FSD.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in DS_LIST:
            Categories.hover()
            DS.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in ST_LIST:
            Categories.hover()
            ST.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in CT_LIST:
            Categories.hover()
            CT.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in DM_LIST:
            Categories.hover()
            DM.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in JT_LIST:
            Categories.hover()
            JT.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in NS_LIST:
            Categories.hover()
            NS.hover()
            i.click()
            print("url:",  page.url)
            # page.wait_for_timeout(1000)
            page.go_back()

    for i in PL_LIST:
            Categories.hover()
            PL.hover()
            i.click()
            print("url:",  page.url)
                    # page.wait_for_timeout(1000)
            page.go_back()
    
    for i in CT_LIST:
        Categories.hover()
        CT.hover()
        i.click()
        print("url:",  page.url)
            # page.wait_for_timeout(1000)
        page.go_back()  

    for i in GD_LIST:
        Categories.hover()
        GD.hover()
        i.click()
        print("url:",  page.url)
                     # page.wait_for_timeout(1000)
        page.go_back()  
    
    page.wait_for_timeout(5000)

'''


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://uncodemy.com/")
    page.wait_for_load_state("load")
    page.wait_for_timeout(1000)


