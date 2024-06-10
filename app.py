from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "789789456qweQ$"
app.config['MYSQL_DB'] = "anime"

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def home():
    sort_by = request.form.get('sort') if request.method == 'POST' else None
    order = 'ASC' if sort_by in ['name_asc', 'rating_asc', 'views_asc'] else 'DESC'
    cur = mysql.connection.cursor()
    query = "SELECT * FROM anime.anime"
    if sort_by:
        if sort_by.startswith('name'):
            query += f" ORDER BY name_ru {order}"
        elif sort_by.startswith('rating'):
            query += f" ORDER BY rating {order}"
        elif sort_by.startswith('views'):
            query += f" ORDER BY views {order}"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()

    # Преобразование результатов в словари
    data = [
        {
            'id': row[0],
            'name_ru': row[1],
            'name_eng': row[2],
            'year_of_release': row[3],
            'description': row[4],
            'director': row[5],
            'rating': row[6],
            'views': row[7],
            'status': row[8],
            'studio': row[9],
            'img': row[10]
        } for row in rows
    ]
    return render_template('home.html', data=data)
@app.route("/details")
def deteils():
    id = request.args.get('id')
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM anime.anime WHERE id = {id};")
    row = cur.fetchone()
    data = {
            'id': row[0],
            'name_ru': row[1],
            'name_eng': row[2],
            'year_of_release': row[3],
            'description': row[4],
            'director': row[5],
            'rating': row[6],
            'views': row[7],
            'status': row[8],
            'studio': row[9],
            'img': row[10]
        }
    
    cur.execute(f"SELECT name FROM anime.anime_genre JOIN genre ON anime_genre.genre_id = genre.id WHERE anime_genre.anime_id = {id};")
    genres = [genre[0] for genre in cur.fetchall()]
    genres = ', '.join([str(genre) for genre in genres])

    cur.execute(f"SELECT name FROM anime.anime_translation JOIN translation ON anime_translation.translation_id = translation.id WHERE anime_translation.anime_id = {id};")
    translations = [translation[0] for translation in cur.fetchall()]
    translations = ', '.join([str(translation) for translation in translations])
    
    cur.execute(f"SELECT name FROM anime.anime_licensed join licensed on anime_licensed.licensed_id = licensed.id where anime_licensed.anime_id = {id};")
    licenses = [licensed[0] for licensed in cur.fetchall()]
    licenses = ', '.join([str(licensed) for licensed in licenses])

    return render_template('details.html', data = data, genres = genres, translations = translations, licenses = licenses)


@app.route("/tierlist", methods=["POST", "GET"])
def tierlist():
    sort_by = request.form.get('sort') if request.method == 'POST' else None
    order = 'ASC'  # Всегда устанавливаем порядок сортировки на возрастающий
    
    cur = mysql.connection.cursor()
    query = """
        SELECT 
            anime.id,
            anime.name_ru, 
            COALESCE(anime_tierlist.ratingSiteOne, 1000) AS ratingSiteOne, 
            COALESCE(anime_tierlist.ratingSiteTwo, 1000) AS ratingSiteTwo, 
            COALESCE(anime_tierlist.ratingSiteThree, 1000) AS ratingSiteThree, 
            anime.img 
        FROM anime_tierlist
        JOIN anime ON anime_tierlist.anime_id = anime.id
    """
    if sort_by:
        if sort_by.startswith('ratingSiteOne'):
            query += f" ORDER BY ratingSiteOne {order}"
        elif sort_by.startswith('ratingSiteTwo'):
            query += f" ORDER BY ratingSiteTwo {order}"
        elif sort_by.startswith('ratingSiteThree'):
            query += f" ORDER BY ratingSiteThree {order}"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()

    # Преобразование результатов в список словарей
    data = [
        {
            'id': row[0],
            'name_ru': row[1],
            'ratingSiteOne': row[2],
            'ratingSiteTwo': row[3],
            'ratingSiteThree': row[4],
            'img': row[5],
            'sort': sort_by
        } for row in rows
    ]
    return render_template('tierlist.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)