// import { text } from 'node:stream/consumers';

const {test, expect}  = require('@playwright/test');
// const { title } = require('node:process');

test('Browser context Playwright test', async ({browser, page})=>
{
//npx playwright codegen https://rahulshettyacademy.com/client  ---for xpath generation
const email = 'manishsdhobale2@gmail.com'
const products = page.locator(".card-body");
const productName = 'ZARA COAT 3';
await page.goto("https://rahulshettyacademy.com/client/#/auth/login");
await page.locator("#userEmail").fill("manishsdhobale2@gmail.com");
await page.locator("#userPassword").fill("Manish@12345");
await page.locator("[value='Login']").click();
//  await page.waitForLoadState("networkidle");   //method is discourage the result due to flakyness
// await page.locator("card-body").first().waitFor();
  // await page.getByText('ADIDAS ORIGINAL').click();
await expect(page.locator(".card-body b").first()).toBeVisible();
const titles =  await page.locator(".card-body b").allTextContents();
console.log(titles);
const count = await products.count();
for(let i = 0 ; i<count ; i++){
  if (await products.nth(i).locator("b").textContent() == productName){
    await products.nth(i).locator("text = Add To Cart").click();
    break;
  }
}
// await page.pause();
await page.locator("[routerlink*='cart']").click();
await page.locator("div li").first().waitFor();
// await page.pause();
const bool =  await page.locator("h3:has-text('ZARA COAT 3')").isVisible() ;       //PSEUDO CLASS
expect(bool).toBeTruthy();
// await page.pause();
await page.locator("text=Checkout").click();
// await page.locator("[placeholder*='Country']").type("ind",{delay:100});
await page.locator("[placeholder*='Country']").pressSequentially("ind",{delay:100});
const dropdown = page.locator(".ta-results");

await dropdown.waitFor();

const optionCount = await dropdown.locator("button").count();

for(let i = 0 ; i<optionCount; ++i)
{
    const text = await dropdown.locator("button").nth(i).textContent();
    if(text === " India")
    {
      await dropdown.locator("button").nth(i).click();
      break;
    }
}
expect(page.locator(".user__name [type='text']").first()).toHaveText(email);
await page.locator(".action__submit").click();
await expect(page.locator(".hero-primary")).toHaveText(" Thankyou for the order. ");
const orderid = await page.locator(".em-spacer-1 .ng-star-inserted").textContent();
console.log(orderid)
// await page.pause();
await page.locator("button[routerlink*='myorders']").click();
await page.locator("tbody").waitFor();
const rows = await page.locator("tbody tr");
for (let i = 0; i < await rows.count(); ++i) 
  {
    const rowOrderId = await rows.nth(i).locator("th").textContent();
    if (orderid.includes(rowOrderId)) 
      {
         await rows.nth(i).locator("button").first().click();
         break;
      }
   }
const orderIdDetails = await page.locator(".col-text").textContent();
expect(orderid.includes(orderIdDetails)).toBeTruthy();
});














//UI control -- dropdown , radio button , popup

test("UI control", async({page})=>
{

await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

const username = page. locator("#username");
const signin  = page.locator("signInBtn");

const dropdown = page.locator("select.form-control")
await dropdown.selectOption("consult")

await page.locator(".radiotextsty").last().click();
await page.pause();

await page. locator("#okayBtn").click();

console.log(await page.locator(".radiotextsty").last().isChecked());
expect (await page.locator(".radiotextsty").last()).toBeChecked();
// await page.pause();

await page.locator("#terms").click()
await expect(page.locator("#terms")).toBeChecked()
 await page.pause();
await page.locator("#terms").uncheck();
expect (await page.locator("#terms").isChecked()).toBeFalsy();
 await page.pause();



});