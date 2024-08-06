import re
from playwright.sync_api import sync_playwright, Page, expect


from playwright.sync_api import sync_playwright

from time import sleep

def run_tests():
    with sync_playwright() as p:
        # Launch a Chromium browser instance
        browser = p.chromium.launch()
        # browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the target URL
        page.goto("https://time.is/")  # Replace with your URL
        page.screenshot(path="timeweb.png")

        sleep(20) # to keep the sleep because page may take time to load
        
        # # Wait for the <h1> element with ID zxc123 to be visible
        page.locator("#syncH").wait_for(state="visible")
         
        sleep(10)
        
        # Locate the <h1> element by its ID
        element = page.locator("#syncH")
        page.screenshot(path="timeweb.png")
        
        # Print the text content of the <h1> element
        print(element.text_content())
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    run_tests()






