from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/demo-site/draganddrop/#google_vignette")
    page.wait_for_timeout(2000)

    # Drag and drop 
    fm = page.frame_locator('(//iframe[@class="demo-frame"])[1]')
    img1 = fm.locator('//img[@src="images/high_tatras_min.jpg"]')
    img2 = fm.locator('//img[@src="images/high_tatras3_min.jpg"]')
    img3 = fm.locator('//img[@src="images/high_tatras4_min.jpg"]')
    img4 = fm.locator('//img[@src="images/high_tatras2_min.jpg"]')
    trash  = fm.locator('//div[@id="trash"]')

    images = [img1,img2,img3,img4]
    for i in images:
        i.drag_to(trash)
        page.wait_for_timeout(1000)








