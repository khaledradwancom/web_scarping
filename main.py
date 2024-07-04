from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://soundcloud.com/rplaylisting/sets/series'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

movies = driver.find_elements(By.CSS_SELECTOR, value='li.trackList__item')
print(movies)
movie_links = []
for movie in movies:
     movie_links.append(movie.text)

for movie in movie_links:
    movie.replace('\n', '')
    movie.translate({ord('b'): None})

    with open('songs_trend.txt', "a", encoding="utf-8") as f:
        f.write(f'{movie}\n')
driver.quit()
