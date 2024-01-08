import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text,'html.parser')

titles = soup.find_all('h3',class_='title')

"""
movie_names = []
for title in titles:
    movie_name = title.getText()
    movie_names.append(movie_name)
"""

all_year = soup.find_all('strong')

years = [year.getText() for year in all_year]

movie_names = [title.getText() for title in titles] 
movies = movie_names[::-1]

with open('movie_list.txt', 'w', encoding='utf-16') as file:
    file.write(f"Index Movie-Name Year\n")
    for movie, year in zip(movies, years):
        file.write(f"{movie} {year}\n")