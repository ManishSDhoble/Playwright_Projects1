const {test, expect}  = require('@playwright/test')

// test('First Playwright test', async function()
// test('First Playwright test', async ()=>

// {

// playwrigh code -
// step 1
// step 2
// await
// step 3

// });


// test('First Playwright test', async ({browser})=>

// {
// //chrome  -- plugins / cookies
//   const context = await browser.newContext();
//   const page =  await context.newPage();
//   await page.goto("https//ww.google.com");


// });

/////

test('Browser context Playwright test', async ({browser, page})=>

{
//chrome  -- plugins / cookies
//   const context = await browser.newContext();
//   const page =  await context.newPage();
const username = await page.locator("#username")
const signin = await page.locator("#signInBtn")
const cardtitle = await page.locator(".card-body a")
  await page.goto("https://rahulshettyacademy.com/loginpagePractise/");
  await console.log(await page.title());
//   await expect(page).toHaveTitle();\\

//css , xpath

/*
if Id is present
css -> tagname#id  (or)  #id

if class attribute is present
css -> tagname.class (or) .class

write css based on any attribute
css -->tagname[attribute = 'value']    tagname is optional 

write css with traversing from parent to child
css -> parenttagname childtagname

if need to write the locator based on text
text = ''

*/

await username.fill("rahulshetty")
await page.locator("[type='password']").fill("Learning@830$3mK2")
await signin.click();
// wait untill this locator shown on page
//webdriverwait
console.log(await page.locator("[style*='block']").textContent());     //textcontent()--- inputvalue()

// assertion -- expect , tocontenttext
await expect(page.locator("[style*='block']")).toContainText("Incorrect");
await username.fill("");
await username.fill("rahulshettyacademy");
// await signin.click();
// console.log(await cardtitle.nth(0).textContent());
// console.log(await cardtitle.first().textContent());
// // iphone X
// // iphone X
// console.log(await cardtitle.nth(1).textContent());
// // Samsung Note 8
// console.log(await cardtitle.last().textContent());
//Blackberry
const alltitles = await cardtitle.allTextContents(); 
//alltextcontent method will not wait for elment to display but textcontent will wait.
console.log(alltitles); //[]



});



test("UI control", async({page})=>
{

await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

const username = page. locator("#username");
const signin  = page.locator("signInBtn");
const document_link = page.locator("[href*= 'documents-request']")
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
//  await page.pause();
await page.locator("#terms").uncheck();
expect (await page.locator("#terms").isChecked()).toBeFalsy();
//  await page.pause();

 await expect(document_link).toHaveAttribute('class','blinkingText')


});

test('child windows handle' , async({browser})=>
{
const context = await browser.newContext();
const page = await context.newPage();
await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

const document_link = page.locator("[href*= 'documents-request']");


const [newPage] = await Promise.all(
    [ 
      context.waitForEvent('page'),
      document_link.click(),
    ])

 const text = await newPage.locator(".red").textContent();
  const arrayText = text.split("@")
  const domain = arrayText[1].split(" ")[0]
  console.log(domain);
await page.locator("#username").fill(domain);
await page.pause();

console.log(await page.locator("#username").inputValue());     //textContent()) will work only when page is attached to dom dinamically.;





  }
)

















//////

// test('page Playwright test', async ({ page})=>

// {
//   await page.goto("https://google.com");

//   //get the title - --assertion
//   console.log(await page.title());
// await expect(page).toHaveTitle("Google")


// });