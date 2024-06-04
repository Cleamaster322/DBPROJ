import os
import requests
from bs4 import BeautifulSoup
from os.path import join, exists

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
    print(page_filename)
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

    value = soup.select_one('.page__header').text.strip().split("\n")
    data["name_ru"] = value[0].replace(":",".")
    data["name_eng"] = value[1].replace(":",".")
    check = set(["Жанр","Эпизоды","Студия","Доступны","Переводы","Статус"])
    values = soup.select('.pmovie__header-list li')
    for value in values:
        value = value.text.strip().replace('\n', '').replace('\t', '').split(":")

        if value[0] == "Жанр":
            key = "genres"
            value[1] = value[1].split(",  ")
            print(value[1])
        elif value[0] == "Эпизоды":
            continue
        elif value[0] == "Студия":
            key = "studio"
        elif value[0] == "Доступны":
            continue
        elif value[0] == "Переводы":
            key = "translation"
            value[1] = value[1].split(", ")
        elif value[0] == "Статус":
            key = "status"

        data[key] = value[1]

    value = soup.select_one('.page__text')
    data["description"] = value.text.strip()
    # print(data["description"])

    data["rating"] = soup.select_one('.card__rating-ext-count').text.strip()
    
# Извлекаем количество голосов
    value = soup.select_one('.card__meta').text.strip()
    data["views"] = int(value.replace(" ",""))
# Извлекаем обложку

    new_filename = f"{data["name_ru"].replace("/","_").replace("?","")}.jpg"
    target_dir ="img/s2"
    file_path = join(target_dir, new_filename)


    if not exists(file_path):
        img_div = soup.select_one('.pmovie__poster')
        img_tag = img_div.find('img', {'src': True})
        image_url = img_tag['src']

        base_url = "https://animego.vip"
        full_image_url = base_url + image_url

        image_response = requests.get(full_image_url)

        with open(file_path, 'wb') as file:
            file.write(image_response.content)
    else:
    # Если файл существует, выводим сообщение
        print(f"Файл {new_filename} уже существует")

    data["img"] = file_path
    data["site"] = 2
    data["place"] = place

    # print(result)
    return data

def get_data(url):
    """
    Основная функция для получения данных о топ-100 аниме.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }

    # Получаем HTML-код страницы
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    # Ищем все ссылки на аниме
    # anime_links = soup.find_all('a', class_='updli fx-row fx-middle')
    main_element = soup.find("main")
    anime_links = main_element.find_all("a", class_="updli")
    # Извлекаем href из каждой ссылки
    links = [link['href'] for link in anime_links[10:]]
    # Печатаем ссылки
    # Проходим по каждой ссылке и сохраняем информацию
    data = list()
    for i,link in enumerate(links):
        data.append(parse_anime_page(link, "Data/s2",i+1))
    return data
        

