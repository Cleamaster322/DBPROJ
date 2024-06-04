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
    print(page_filename,"*******************")
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

    # Название Аниме
    header = soup.find("div", class_="page__header-one d-flex ai-center p-relative")
    data["name_ru"] = header.find("h1").get_text()
    data["name_eng"] = None
    
    # Название Категории
    header = soup.find("div", class_="page__meta flex-grow-1")
    data["genres"] = [a.get_text() for a in header.find_all("a")]
    
    # Статус
    status = soup.find("div", class_="card__meta2")
    data["status"] = status.get_text().replace("\n","")

    # Год, Страна, Режиссер, Дата, Просмотров
    page_list = soup.find("ul", class_="page__list")
    for value in page_list.find_all("li"):
        value = value.text.strip().split(":")

        if value[0] == "Год":
            key = "year_of_release"
        elif value[0] == "Режиссер":
            key = "director"
        elif value[0] == "Просмотров":
            key = "views"
            value[1] = value[1].replace(" ","")
        else:
            continue
        data[key] = value[1]
    
    # Описание
    descriptions = soup.find("div", class_ ="full-text p-relative")
    data["description"] = ""

    for desc in descriptions.find_all("p"):
        data["description"] += desc.text.strip()
    
    # Номер сайта, и место аниме 
    data["site"] = 3
    data["place"] = place

    # рейтинг
    like = soup.find("div", class_="page__rating").text.strip().split("\n")
    like = list(map(int,like))
    data["rating"] = round((like[0] / (like[0] + like[1]) * 10), 1)


    # Извлекаем картинку если ее нет
    new_filename = f"{data["name_ru"].replace("/","_").replace("?","")}.jpg"
    target_dir ="img"
    file_path = join(target_dir, new_filename)


    if not exists(file_path):
        img_div = soup.select_one('.page__poster')
        img_tag = img_div.find('img', {'src': True})
        image_url = img_tag['src']

        base_url = "https://animestars.tv"
        full_image_url = base_url + image_url

        image_response = requests.get(full_image_url)

        with open(file_path, 'wb') as file:
            file.write(image_response.content)
    else:
    # Если файл существует, выводим сообщение
        print(f"Файл {new_filename} уже существует")

    data["img"] = file_path


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
    sect_content = soup.find("div", class_="sect__content d-grid-items d-grid-items--main")

    # Находим все article элементы внутри этого div
    articles = sect_content.find_all("article", class_="card has-expanded-link p-relative grid-item")

    # Извлекаем ссылки из тегов <a> внутри каждого article
    links = [article.find("a", class_="card__link has-expanded-link__trg")['href'] for article in articles[0:1]]
    
    # Печатаем ссылки
    # Проходим по каждой ссылке и сохраняем информацию
    data = list()
    for i,link in enumerate(links):
        data.append(parse_anime_page(link, "Data/s3",i+1))
    return data
        