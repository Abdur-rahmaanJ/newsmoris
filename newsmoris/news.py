
try:
    import requests
    from bs4 import BeautifulSoup
    from random import randint, choice
except Exception as e:
    pass

class PageNumberTooLow(Exception):
    def __init__(self, page_num, message="Page number should be 0 or greater"):
        self.page_num = page_num
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.page_num}: {self.message}'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip',
    'DNT' : '1', # Do Not Track Request Header
    'Connection' : 'close',
    'Sec-GPC': '1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


class DefiMedia:
    BASE_URL = 'https://defimedia.info'

    @classmethod
    def top_news(cls): # front page
        links = []
        summary = {'news':[]}
        front_page = cls.BASE_URL + '/'
        titles = requests.get(front_page, headers=headers).content
        soup = BeautifulSoup(titles, 'html.parser')
        ts = soup.find_all(class_='news')
        for news in ts:
            title = news.find(class_='sup-title').text
            link = news.find('a')['href']
            if link not in links:
                summary['news'].append({
                    'title': title,
                    'link': cls.BASE_URL + link
                    })
                links.append(link)
        return summary['news']

    @classmethod
    def page(cls, category, page_num):
        if page_num < 0:
            raise PageNumberTooLow(page_num)

        links = []
        summary = {'news': []}
        page_num_ = page_num
        payload = {'page': page_num_}
        actualites_url = cls.BASE_URL + '/categorie/{}'.format(category)
        session = requests.Session()
        source = session.get(actualites_url, params=payload, headers=headers).content
        # with open('actualites_1.html', 'wb') as f:
        #     f.write(source)
        soup = BeautifulSoup(source, 'html.parser')
        all_news = soup.find_all(role='article')
        for news in all_news:
            title = news.find(class_='sup-title').text.strip().replace('\n', '')
            link = news.find('a')['href']
            if link not in links:
                summary['news'].append({
                    'title': title,
                    'link': cls.BASE_URL + link
                    })
                links.append(link)
        return summary['news']

    @classmethod
    def article(cls, article_url):
        source = requests.get(article_url, headers=headers).content
        soup = BeautifulSoup(source, 'html.parser')
        author = soup.find(itemprop="author").find(itemprop='name').text
        article = soup.find(class_='content').text.strip().strip('\n').strip()
        paragraphs = [p for p in article.split('\n') if p]
        return {
            'author': author,
            'paragraphs': paragraphs,
        }

    @classmethod
    def random_article(cls):
        random_sitemap_nb = randint(1, 3)
        sitemap_url = cls.BASE_URL + f"/sitemaps/{random_sitemap_nb}/sitemap.xml"

        source = requests.get(sitemap_url, headers=headers).content
        soup = BeautifulSoup(source, 'html.parser')
        random_article_url: str = choice(soup.find_all('loc')).text

        random_article_title = random_article_url.replace("http://defimedia.info/", "").replace("-", " ").title()

        return {
            'title': random_article_title,
            'link': random_article_url
        }
