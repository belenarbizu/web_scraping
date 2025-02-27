import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = "https://www.filmaffinity.com/es/ranking.php?rn=ranking_fa_movies"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find(id="top-movies")

movies_list = movies.find_all("li", class_="content")

for i, movie in enumerate(movies_list, start=1):
    movie_container = movie.find("div", class_="mc-title")
    movie_title = movie_container.find("a").text.strip()

    print(f"{i}.{movie_title}")
