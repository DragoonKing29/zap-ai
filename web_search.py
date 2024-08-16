import requests
from bs4 import BeautifulSoup

class WebSearchAI:
    def __init__(self):
        self.knowledge_base = {}

    def search(self, query: str):
        url = f"https://www.google.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = [link.get('href') for link in soup.find_all('a', href=True) if 'http' in link.get('href')]

        self.learn_from_results(links)
        return links

    def learn_from_results(self, links):
        for link in links:
            page_content = self.fetch_page_content(link)
            if page_content:
                self.update_knowledge(query=link, content=page_content)

    def fetch_page_content(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
        return None

    def update_knowledge(self, query, content):
        self.knowledge_base[query] = content

    def recall_knowledge(self, query):
        return self.knowledge_base.get(query, "No knowledge found.")
