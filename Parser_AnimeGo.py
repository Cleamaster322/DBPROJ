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
    print(page_filename)
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

    value = soup.select_one('.page__header')
    data["Name_ru"] = value.text.strip()
    print(data['Name_ru'])

    values = soup.select('.pmovie__header-list li')
    # print(values[0])
    for value in values:
        value = value.text.strip().replace('\n', '').replace('\t', '').split(":")
        data[value[0]] = value[1]
        print(value[0],value[1])

    value = soup.select_one('.page__text')
    data["Description"] = value.text.strip()
    print(data["Description"])

    rating = soup.select_one('.card__rating-ext-count').text.strip()

# Извлекаем количество голосов
    votes_span = soup.select_one('.card__rating-ext span:contains("Голосов:")')
    votes = votes_span.find('span').text.strip()

    # Формируем строку с рейтингом и количеством голосов
    result = f"{rating} / 10 ({votes} голосов)"
    print(result)

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
    links = [link['href'] for link in anime_links]
    # Печатаем ссылки
    print(links)
    # Проходим по каждой ссылке и сохраняем информацию
    for i,link in enumerate(links):
        parse_anime_page(link, "Data/s2",i+1)
        

if __name__ == "__main__":
    get_data("https://animego.vip/top-100.html")
