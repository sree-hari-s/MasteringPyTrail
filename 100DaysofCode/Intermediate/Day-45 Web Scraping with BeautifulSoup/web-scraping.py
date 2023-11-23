import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
page = requests.get(URL)

# Get the source code of the page to an index.html file that
with open('index.html','w') as file:
    file.write(page.text)

soup = BeautifulSoup(page.text , 'html.parser')

"""
Finding a single item

article = soup.find('span', class_='titleline')
link_tag = article.find('a')
subtexts = soup.find(name="td", class_="subtext")

title = article.getText()
link = link_tag.get('href')
upvote = subtexts.getText().split()[0]
"""

articles = soup.find_all('span',class_='titleline')
subtexts = soup.find_all(name="td", class_="subtext")

article_titles = []
article_links = []
article_upvotes = []

for article in articles:
    title = article.getText()
    link = article.find('span',class_='sitestr').getText()
    article_titles.append(title)
    article_links.append(link)

for sub in subtexts:
    upvote = sub.find('span',class_='score')
    if upvote is None:
        upvote = 0
    else:
        upvote = upvote.getText().split()[0]
    article_upvotes.append(int(upvote))

# print(article_titles)
# print(article_links)
# print(article_upvotes)

"""
Article with highest Upvotes
"""
highest_upvotes = max(article_upvotes)
index = article_upvotes.index(highest_upvotes)
print(article_titles[index])