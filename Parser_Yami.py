import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from os.path import join, exists

headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
proxies = {
    'https':'http://45.4.197.204:8000'
    }

def save_html_to_file(url, filename):
    """
    Сохраняет HTML-код страницы в файл.
    """
    try:
        response = requests.get(url,headers=headers,proxies=proxies)
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
    try:
        with open(page_filename, "r", encoding='utf-8') as file:
            page_content = file.read()
    except:
        return

    soup = BeautifulSoup(page_content, "lxml")
    return extract_info(soup,place)

def extract_info(soup,place):
    """
    Извлекает информацию о аниме из BeautifulSoup объекта.
    """
    data = dict()

    value = soup.select_one('.inner-page__title')
    data["name_ru"] = value.text.strip().replace(":",".")

    value = soup.select_one('.inner-page__subtitle')
    data["name_eng"] = value.text.strip().replace(":",".")

    values = soup.select('.inner-page__list li')

    #  keys = ["year_of_release","time","director","rating","genres","views","status","licensed","translation"]
    check = set(["Год выхода","Время","Режиссер","Рейтинг аниме","Жанр","Просмотров","Статус","Лицензировано","Перевод"])
    cur_tag =[value.text.strip().split(": ")[0] for value in values]
    for i,value in enumerate(values):
        value = value.text.strip().split(": ")
        if cur_tag[i] == "Год выхода":
            key = "year_of_release"

        elif cur_tag[i] == "Время":
            key = "time"

        elif cur_tag[i] == "Режиссер":
            key = "director"

        elif cur_tag[i] == "Рейтинг аниме":
            key = "rating"
            value[1] = value[1].split(' / ')
            value[1] = float(value[1][0])

        elif cur_tag[i] == "Жанр":
            key = "genres"
            value[1] = value[1].split(r' •  ',)

        elif cur_tag[i] == "Просмотров":
            key = "views"
            value[1] = int(value[1].replace(" ", ""))

        elif cur_tag[i] == "Статус":
            key = "status"

        elif cur_tag[i] == "Лицензировано":
            key = "licensed"
            value[1] = value[1].split(", ")

        elif cur_tag[i] == "Перевод":
            key = "translation"
            value[1] = value[1].split(", ")

        data[key] = value[1]

    data["description"] = soup.select_one('.inner-page__text.text.clearfix').text.strip()
    data["place"] = place


    new_filename = f"{data["name_ru"].replace("/","_")}.jpg"
    target_dir ="static/img"
    file_path = join(target_dir, new_filename)
    if not exists(file_path):
        img_tag = soup.find('img', {'src': True})
        image_url = img_tag['src']
        base_url = "https://yummyanime.tv"
        full_image_url = base_url + image_url
        image_response = requests.get(full_image_url)

        with open(file_path, 'wb') as file:
            file.write(image_response.content)

    data["img"] = file_path
    data["site"] = 1
    print(data["name_ru"],file_path)
    return data
    

def get_data(url):
    """
    Основная функция для получения данных о топ-100 аниме.
    """
    base_url = "https://yummyanime.tv"

    # Получаем список ссылок на аниме
    soup = BeautifulSoup(requests.get(url, headers=headers,proxies=proxies).text, "lxml")
    movie_items = soup.find_all('div', class_='movie-item')
    links = [base_url + item.find('a')['href'] for item in movie_items]

    # Проходим по каждой ссылке и сохраняем информацию
    data = list()
    for i,link in enumerate(links):
        data.append(parse_anime_page(link, "Data/s1",i+1))
    
    return data
