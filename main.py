from scraper import scrape_urls

START_URL = "https://www.sesisp.org.br/"

if __name__ == "__main__":
    urls = scrape_urls(START_URL)

    with open("urls_encontradas.txt", "w", encoding="utf-8") as file:
        for url in urls:
            file.write(url + "\n")

    print(f"{len(urls)} URLs únicas encontradas e salvas em 'urls_encontradas.txt'.")
