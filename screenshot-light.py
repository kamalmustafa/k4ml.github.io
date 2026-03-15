from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})

    # Add localStorage to enable light mode
    page.goto("http://localhost:8080")
    page.evaluate("localStorage.setItem('theme', 'light')")
    page.reload()

    page.wait_for_load_state("networkidle")
    page.screenshot(path="/tmp/site-screenshot-light.png", full_page=True)
    print("Light mode screenshot saved")
    browser.close()
