from playwright.sync_api import sync_playwright

def main():
    url = "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open webpage
        page.goto(url)

        # Wait for content to load
        page.wait_for_selector("div.mw-parser-output")

        # Get all paragraph texts
        paragraphs = page.locator("div.mw-parser-output > p").all_text_contents()

        # Combine text
        article_text = "\n\n".join([p.strip() for p in paragraphs if p.strip()])

        # Save to file
        with open("generative_ai_wikipedia.txt", "w", encoding="utf-8") as f:
            f.write(article_text)

        print("Content saved to generative_ai_wikipedia.txt")

        browser.close()

if __name__ == "__main__":
    main()