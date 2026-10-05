from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class portfolios:
    def __init__(self,page):
        self.page = page

        # our projects
        self.portpage = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')

        self.ICSHomework = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wingFarma = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena = page.locator('//a[@href="https://arenasonipat.com/"]')
        self. home = page.locator('//a[@href="https://home360stores.com/"]')
        self.club = page.locator('(//a[text()="View More"])[5]')
        self.cordcable = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        # social portfolio page follow us

        self.facebook  = page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin = page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.instagram = page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pinterest = page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.trankX = page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.utube = page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora = page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')

    def portfolio_our_projects(self):
        self.portpage.click()
        # self.page.wait_for_load_state("load")
        # self.ICSHomework.click()
        # self.wingFarma.click()
        # self.arena.click()
        # self.home.click()
        # self.club.click()
        # self.cordcable.click()

        self.page.wait_for_load_state("load")
        portfolio_url = self.page.url
        self.ourprojectslist = [self.ICSHomework,self.wingFarma,self.arena,self.home, self.club,self.cordcable]

        for viewmorelink in self.ourprojectslist:
            target = viewmorelink.get_attribute("target")

            if target == "_blank":
                with self.page.context.expect_page() as new_page_info:
                    viewmorelink.click(no_wait_after=True)
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()
            else:
                viewmorelink.click(no_wait_after=True)
                self.page.wait_for_load_state("load")
                self.page.goto(portfolio_url)
                self.page.wait_for_load_state("load")


    def socialmediapageclick(self):
        social_media_hrefs = [
            "https://www.facebook.com/TrankTechnologies",
            "https://in.linkedin.com/company/trank-technologies-official",
            "https://www.instagram.com/tranktechnologies/",
            "https://in.pinterest.com/tranktechnologies12/",
            "https://twitter.com/tranktechno",
            "https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg",
            "https://www.quora.com/profile/Trank-Technologies-1",
        ]
        portfolio_url = self.portpage.get_attribute("href")
        self.page.goto(portfolio_url, wait_until="domcontentloaded")
        for social_media_href in social_media_hrefs:
            self.page.goto(portfolio_url, wait_until="domcontentloaded")
            social_media_link = self.page.locator(f'//a[@href="{social_media_href}"]').first
            try:
                with self.page.context.expect_page(timeout=5000) as new_page_info:
                    social_media_link.click(no_wait_after=True)
            except PlaywrightTimeoutError:
                continue

            new_tab = new_page_info.value
            new_tab.wait_for_load_state("domcontentloaded", timeout=15000)
            new_tab.close()