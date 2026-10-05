import {test, expect} from '@playwright/test'
import { asyncWrapProviders } from 'node:async_hooks';

test('Playwright special locators' , async({page})=>

    {

        await page.goto("https://rahulshettyacademy.com/angularpractice/");
        
        await page.getByLabel("Check me out if you Love IceCreams!").check();
        await page.getByLabel("Employed").check();
        await page.getByLabel("Gender").selectOption("Male")
        
          //npx playwright test --ui                   
        await page.getByPlaceholder("Password").fill("abc123")
        await page.getByRole("button",{name: 'Submit'}).click();
        // await page.pause();
        // 5 sec timeout for expect assertions
        await expect(page.getByText("Success! The Form has been submitted successfully!.")).toBeVisible({timeout:10000});
        await page.getByRole("link", {name :'Shop'}).click();
        await page.locator("app-card").filter({hasText:'Nokia Edge'}).getByRole("button").click();
    });

   test('Playwright special test level timeout' , async({page})=>

    {
        const slowexpect = expect.configure({timeout : 9000});
        await page.goto("https://rahulshettyacademy.com/angularpractice/");
        
        await page.getByLabel("Check me out if you Love IceCreams!").check();
        await page.getByLabel("Employed").check();
        await page.getByLabel("Gender").selectOption("Male")
        
          //npx playwright test --ui                   
        await page.getByPlaceholder("Password").fill("abc123")
        await page.getByRole("button",{name: 'Submit'}).click();
        // await page.pause();
        // 5 sec timeout for expect assertions
        await slowexpect(page.getByText("Success! The Form has been submitted successfully!.")).toBeVisible();
        await page.getByRole("link", {name :'Shop'}).click();
        await slowexpect(page.locator(".my-4").first()).toHaveText("Shop")
        await page.locator("app-card").filter({hasText:'Nokia Edge'}).getByRole("button").click();
    }); 



    test('Playwright special test timeout' , async({page})=>

    {
        const slowexpect = expect.configure({timeout : 9000});
        await page.goto("https://rahulshettyacademy.com/angularpractice/");
        
        await page.getByLabel("Check me out if you Love IceCreams!").check();
        await page.getByLabel("Employed").check();
        await page.getByLabel("Gender").selectOption("Male")
        
          //npx playwright test --ui                   
        await page.getByPlaceholder("Password").fill("abc123")
        await page.getByRole("button",{name: 'Submit'}).click();
        // await page.pause();
        // 5 sec timeout for expect assertions
        await slowexpect(page.getByText("Success! The Form has been submitted successfully!.")).toBeVisible();
        await page.getByRole("link", {name :'Shop'}).click();
        await slowexpect(page.locator(".my-4").first()).toHaveText("Shop")
        await page.locator("app-card").filter({hasText:'Nokia Edge'}).getByRole("button").click();
    }); 