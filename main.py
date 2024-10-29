from pprint import pprint


import requests
import bs4



# ключевые слова в статьях
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# создаем переменную с основным доменом (попадаем на сайт для работы с ним и получения с него информации)
respons_dom = requests.get('https://habr.com/ru/articles/')

# получаем всю информацию с сайта для дальнейшей обработки
soup = bs4.BeautifulSoup(respons_dom.text, features='lxml')
# pprint(soup)

# из всего полученного файла получаем только статьи целиком
search = soup.find_all('article', 'tm-articles-list__item')

for article in search:
    article_tex = article.find('div', 'article-formatted-body article-formatted-body article-formatted-body_version-2') # получаем текст статьи с превью страницы (однако не всегда работает)
    # pprint(article_tex)

    for key in KEYWORDS:
        current_article = article.find('a', 'tm-title__link')
        title = current_article.span.text  # получаем заголовок
        link = f"https://habr.com{current_article['href']}"  # получаем ссылку
        article_time = article.find('time')['datetime']  # получаем дату и время
        if key in title or article_tex:
            pprint(f"{article_time}-{title}-{link}")






