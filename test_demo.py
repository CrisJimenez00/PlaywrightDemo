from playwright.sync_api import sync_playwright, expect
import re, time


def test_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        expect(page).to_have_title(re.compile("Swag Labs"))
        #Change time value (seconds) for debugging purposes.
        time.sleep(500)
   
#This is for use without problems the comand "python3 test_demo.py"
#It's optional because "pytest" thats fine without this lines.
if __name__=="__main__":
    test_demo()
