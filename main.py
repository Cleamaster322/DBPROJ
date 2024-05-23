import os
import requests
from bs4 import BeautifulSoup

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
    extract_info(soup,place)

def extract_info(soup,place):
    """
    Извлекает информацию о аниме из BeautifulSoup объекта.
    """
    data = dict()

    value = soup.select_one('.inner-page__title')
    data["Name_ru"] = value.text.strip()

    value = soup.select_one('.inner-page__subtitle')
    data["Name_eng"] = value.text.strip()

    values = soup.select('.inner-page__list li')
    print(data["Name_ru"])
    print(data["Name_eng"])

    for value in values:
        value = value.text.strip().split(": ")
        data[value[0]] = value[1]
        print(value[0],value[1])

    data["Описание"] = soup.select_one('.inner-page__text.text.clearfix').text.strip()
    data["Место"] = place
    print(data["Описание"])
    print(data["Место"])
    

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
    links = [base_url + item.find('a')['href'] for item in movie_items[:2]]

    # Проходим по каждой ссылке и сохраняем информацию
    for i,link in enumerate(links):
        parse_anime_page(link, "data",i+1)
        

if __name__ == "__main__":
    get_data("https://yummyanime.tv/2top-100/")
