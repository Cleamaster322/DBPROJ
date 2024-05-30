import os
import requests
from bs4 import BeautifulSoup
import re

def save_html_to_file(url, filename):
    """
    Сохраняет HTML-код страницы в файл.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно
        with open(filename, "w", encoding='utf-8') as file:
            file.write(response.text)
    except requests.RequestException as e:
        print(f"Ошибка при попытке получить страницу {url}: {e}")

def parse_anime_page(page_url, output_dir,place):
    """
    Парсит страницу аниме и извлекает информацию.
    """
    page_filename = os.path.join(output_dir, f"{page_url.split('/')[-1]}")
    save_html_to_file(page_url, page_filename)

    with open(page_filename, "r", encoding='utf-8') as file:
        page_content = file.read()

    soup = BeautifulSoup(page_content, "lxml")
    return extract_info(soup,place)

def extract_info(soup,place):
    """
    Извлекает информацию о аниме из BeautifulSoup объекта.
    """
    data = dict()

    value = soup.select_one('.inner-page__title')
    data["name_ru"] = value.text.strip()

    value = soup.select_one('.inner-page__subtitle')
    data["name_eng"] = value.text.strip()

    values = soup.select('.inner-page__list li')


    keys = ["year_of_release","time","director","rating","genres","views","status","licensed","translation"]
    for i,value in enumerate(values):
        value = value.text.strip().split(": ")
        # Вытаскивает из строки только текущий рейтинг аниме
        if keys[i] == "rating":
            value[1] = value[1].split(' / ')
            value[1] = float(value[1][0])
        
        if keys[i] == "genres":
            value[1] = value[1].split(r' •  ',)
        
        if keys[i] == "views":
            value[1] = int(value[1].replace(" ", ""))
            print(value[1])
        if keys[i] == "licensed":
            value[1] = value[1].split(", ")
        
        if keys[i] == "translation":
            value[1] = value[1].split(", ")
        
        data[keys[i]] = value[1]

    data["description"] = soup.select_one('.inner-page__text.text.clearfix').text.strip()
    data["place"] = place
    return data
    

def get_data(url):
    """
    Основная функция для получения данных о топ-100 аниме.
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
    base_url = "https://yummyanime.tv"

    # Получаем список ссылок на аниме
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")
    movie_items = soup.find_all('div', class_='movie-item')
    links = [base_url + item.find('a')['href'] for item in movie_items[0:1]]

    # Проходим по каждой ссылке и сохраняем информацию
    data = list()
    for i,link in enumerate(links):
        data.append(parse_anime_page(link, "Data/s1",i+1))
    
    return data
