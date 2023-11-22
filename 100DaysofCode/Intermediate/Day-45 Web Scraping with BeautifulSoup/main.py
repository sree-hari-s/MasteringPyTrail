from bs4 import BeautifulSoup

with open('website.html',encoding="utf-8") as f:
    data = f.read()

soup = BeautifulSoup(data,'html.parser')
# print(soup.prettify())

all_a_tags = soup.find_all(name='a')
#print(all_a_tags)

for tag in all_a_tags:
    print(tag.get("href"))

heading = soup.find(name='h1',id='name')
print(heading)