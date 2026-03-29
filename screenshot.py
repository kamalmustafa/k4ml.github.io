from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto("http://localhost:8080", wait_until="networkidle")
    page.screenshot(path="/tmp/site-screenshot.png", full_page=True)
    print("Screenshot saved to /tmp/site-screenshot.png")
    browser.close()
