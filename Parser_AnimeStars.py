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
    print(page_filename,"*******************")
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

    # Название Аниме
    header = soup.find("div", class_="page__header-one d-flex ai-center p-relative")
    data["Name_ru"] = header.find("h1").get_text()
    
    # Название Категории
    header = soup.find("div", class_="page__meta flex-grow-1")
    data["Category"] = [a.get_text() for a in header.find_all("a")]

    #Год, Страна, Режиссер, Дата, Просмотров
    page_list = soup.find("ul", class_="page__list")
    items = []
    for li in page_list.find_all("li"):
        if "Из серии" not in li.text and "Сезон" not in li.text :
            value = (li.text.strip().split(":"))
            data[value[0]] = value[1]
            # print(data[value[0]])

    descriptions = soup.find("div", class_ ="full-text p-relative")
    data["Description"] = ""
    
    for desc in descriptions.find_all("p"):
        data["Description"] += desc.text.strip()
    # print(data["Name_ru"])
    # print(data["Description"])

    for i in data.keys():
        print(i)
    
    # print(description.text.strip())
    # values = soup.select('.inner-page__list li')
    # print(data["Category"])
    # print(data["Name_eng"])

    # for value in values:
    #     value = value.text.strip().split(": ")
    #     data[value[0]] = value[1]
    #     print(value[0],value[1])

    # data["Описание"] = soup.select_one('.inner-page__text.text.clearfix').text.strip()
    # data["Место"] = place
    # print(data["Описание"])
    # print(data["Место"])    

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
    links = [article.find("a", class_="card__link has-expanded-link__trg")['href'] for article in articles[4:5]]
    
    # Печатаем ссылки
    print(links)
    # Проходим по каждой ссылке и сохраняем информацию
    for i,link in enumerate(links):
        parse_anime_page(link, "Data/s3",i+1)
        

if __name__ == "__main__":
    get_data("https://animestars.tv/top100.html")
    # extract_info()