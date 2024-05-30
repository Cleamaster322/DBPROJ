import mysql.connector

import Parser_Yami as PY
import DatabaseManager as DB

def add_data_to_dataBase(db_manager, table_name, column_names, values):
    """
    Функция для добавления данных в таблицу.

    :param db_manager: Экземпляр класса DatabaseManager.
    :param table_name: Имя таблицы, в которую будут добавлены данные.
    :param column_names: Список имен столбцов, в которые будут добавлены данные.
    :param values: Список значений, соответствующих столбцам.
    """

    try:
        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(values))})"
        print(query)
        db_manager.execute_query(query, tuple(values))
        db_manager.commit()
        print(f"{len(values)} записей успешно добавлено в таблицу {table_name}.")
    except Exception as err:
        print(f"Ошибка при добавлении данных: {err}")
        db_manager.rollback()

def exists_in_dataBase(db_manager,table_name,column_name,value):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s"
    result = db_manager.execute_query(query, (value,))
    return bool(result[0][0])

# Добавить данные в таблицу anime
def add_to_anime(db_manager,data):
    column_names = ["name_ru","name_eng","year_of_release","description","director","rating","views","status"]
    values = [data[name] for name in column_names]
    if exists_in_dataBase(db_manager,"anime","name_ru",data["name_ru"]):
        print("Такое аниме уже есть")
        return
    add_data_to_dataBase(db_manager,"anime",column_names,values)

def add_to_genre(db_manager,data):
    column_names = ["name"]
    values = data["genres"]
    for value in values:

        if exists_in_dataBase(db_manager,"genre","name",value):
            print("Такой жанр уже есть")
            continue
        add_data_to_dataBase(db_manager,"genre",column_names,[value])


if __name__ == "__main__":
    db_manager = DB.DatabaseManager()

    # Пример использования функции
    column_names = ['name']
    values = ['aboba5']

    # add_data_to_anime(db_manager, 'genre', column_names, values)
    a = PY.get_data("https://yummyanime.tv/2top-100/")
    for datum in a:
        # add_to_anime(db_manager,datum)
        add_to_genre(db_manager,datum)
    db_manager.close_connection()

