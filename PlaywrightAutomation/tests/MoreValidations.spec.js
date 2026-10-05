const {test, expect} = require("@playwright/test")


test("popup validations" , async({page})=>

{

    await page.goto("https://rahulshettyacademy.com/AutomationPractice/");
        // await page.goto("https://www.google.com/");

        // page.goBack();
        // page.goForward();
    await expect(page.locator("#displayed-text")).toBeVisible();
    await page.locator("#hide-textbox").click();
    await expect(page.locator("#displayed-text")).toBeHidden();
    
    // await page.pause();

    page.on('dialog', dialog => dialog.accept());
    await page.locator("#confirmbtn").click();


    await page.locator("#mousehover").hover();


    const framespage = page.frameLocator("#courses-iframe");
    // const framespage = await expect(page.frameLocator("#courses-iframe")).toBeVisible();
    await framespage.locator("li a[href*='lifetime-access']:visible").click();
    const textcheck  = await framespage.locator(".text h2").textContent();
    console.log(textcheck.split(" ")[1]);







});