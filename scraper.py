from playwright.sync_api import sync_playwright

def fetch_and_screenshot():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="chapter_1.png")
        text = page.inner_text("body")
        browser.close()

    return text.strip()