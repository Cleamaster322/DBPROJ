import mysql.connector

import Parser_Yami as PY
import Parser_AnimeGo as PAG
import Parser_AnimeStars as PAS
import DatabaseManager as DB

def add_data_to_dataBase(db_manager, table_name, column_names, values):
    try:
        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(values))})"
        db_manager.execute_query(query, tuple(values))
        db_manager.commit()
        # print(f"{len(values)} записей успешно добавлено в таблицу {table_name}.")
    except Exception as err:
        print(f"Ошибка при добавлении данных: {err}")
        db_manager.rollback()


def exists_anime_indataBase(db_manager,table_name,column_name,data):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE ({column_name} like %s and year_of_release = %s) or (name_eng like %s and year_of_release = %s)"
    value = (data["name_ru"],data["year_of_release"],data["name_eng"],data["year_of_release"],)
    result = db_manager.execute_query(query, value)
    return bool(result[0][0])
#Проверка есть ли данные в таблице
def exists_in_dataBase(db_manager,table_name,column_name,value,data):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} like %s"
    value = (value,)
    result = db_manager.execute_query(query, value)
    return bool(result[0][0])


#Проверка есть ли данные связи в таблице
def exists_relation_in_dataBase(db_manager,table_name,column_name,value1,value2):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE anime_id = %s and {column_name} = %s"
    result = db_manager.execute_query(query, (value1,value2,))
    return bool(result[0][0])

# Добавить данные в таблицу anime
def add_to_anime(db_manager,data):
    column_names = set(["name_ru","name_eng","year_of_release","description","director","rating","views","status","img","studio"]) & set(data)
    values = [data[name] for name in column_names]
    if exists_anime_indataBase(db_manager,"anime","name_ru",data) !=0:
        update_exists_data(db_manager,data)
        update_tier_list(db_manager,data)
        # print("Такое аниме уже есть", data["name_ru"])
        return
    add_data_to_dataBase(db_manager,"anime",column_names,values)
    add_data_to_tierList(db_manager,data)


# Добавить данные в таблицы genre, licensed, translation (только 1 column в таблице)
def add_generic_data(db_manager, table_name, column_names, data_key, data_values,data):
    for value in data_values:
        if exists_in_dataBase(db_manager, table_name, column_names[0], value, data):
            # print(f"Такой {data_key} уже есть: {value}")
            pass
        else:
            add_data_to_dataBase(db_manager, table_name, column_names, [value])

        add_data_to_anime_genres(db_manager,table_name,data,value)

#Добавить данные в таблицы связи anime_genre, anime_licensed,anime_translation
def add_data_to_anime_genres(db_manager,table_name,data,generic_data_name):
    anime_id = get_anime_id(db_manager,data)

    query = f"SELECT id FROM {table_name} WHERE name = %s"
    generic_data_id = db_manager.execute_query(query, (generic_data_name,))[0][0]
    values = [anime_id,generic_data_id]

    if table_name == "genre":
        column_names = ["anime_id","genre_id"]
        table_name2 = "anime_genre"
        
    if table_name == "licensed":
        column_names = ["anime_id","licensed_id"]
        table_name2 = "anime_licensed"
    
    if table_name == "translation":
        column_names = ["anime_id","translation_id"]
        table_name2 = "anime_translation"
    
    if exists_relation_in_dataBase(db_manager,table_name2,column_names[1],anime_id,generic_data_id):
        # print("Такая свзяь уже есть",anime_id,generic_data_id)
        pass

    else:
        add_data_to_dataBase(db_manager,table_name2,column_names,values)
        
def add_data_to_tierList(db_manager,data):
    if data["site"] == 1:
        numSite = "ratingSiteOne"
    if data["site"] == 2:
        numSite = "ratingSiteTwo"
    if data["site"] == 3:
        numSite = "ratingSiteThree"
    column_names = ["anime_id",numSite]
    anime_id = get_anime_id(db_manager,data)
    values = [anime_id,data["place"]]
    add_data_to_dataBase(db_manager,"anime_tierlist",column_names,values)

def update_exists_data(db_manager,data):
    anime_id = get_anime_id(db_manager,data)

    column_names = set(["name_ru","name_eng","year_of_release","description","director","rating","views","status","img","studio"]) & set(data)
    update_statements =[]
    for key in column_names:    
        if data[key] == None:
            value = "NULL"
        elif type(data[key]) == str:
            value = f"'{data[key]}'"
        else:
            value = data[key]
    
        update_statements.append(f"{key} = COALESCE({key}, {value})")
    update_query = f"UPDATE anime SET {', '.join(update_statements)} WHERE id = {anime_id} AND ({' OR '.join([f'{key} IS NULL' for key in column_names])});"
    db_manager.execute_update_query(update_query)
    db_manager.commit()

def update_tier_list(db_manager,data):
    anime_id = get_anime_id(db_manager,data)

    if data["site"] == 1:
        numSite = "ratingSiteOne"
    if data["site"] == 2:
        numSite = "ratingSiteTwo"
    if data["site"] == 3:
        numSite = "ratingSiteThree"
    anime_id = get_anime_id(db_manager,data)
    
    update_query = f"UPDATE anime_tierlist SET {numSite} = COALESCE({numSite},{data['place']}) WHERE id = {anime_id} AND ({f'{numSite} IS NULL'});"
    db_manager.execute_update_query(update_query)
    db_manager.commit()

def get_anime_id(db_manager,data):
    query = f"SELECT id FROM anime WHERE (name_ru like %s and year_of_release = %s) or (name_eng like %s and year_of_release = %s)"
    anime_id = db_manager.execute_query(query, (data["name_ru"],data["year_of_release"],data["name_eng"],data["year_of_release"],))[0][0]
    return anime_id



if __name__ == "__main__":
    db_manager = DB.DatabaseManager()
    dataset = PY.get_data("https://yummyanime.tv/2top-100/")
    for data in dataset:
        if data == None:
            continue
        add_to_anime(db_manager,data)
        add_generic_data(db_manager, "genre", ["name"], "genres", data["genres"],data)
        try:
            add_generic_data(db_manager, "translation", ["name"], "translation", data["translation"],data)
        except:
            pass
        try:
            add_generic_data(db_manager, "licensed", ["name"], "licensed", data["licensed"],data)
        except:
            pass



    dataset2 = PAG.get_data("https://animego.vip/top-100.html")
    # print(dataset2[0])

    for data in dataset2:
        if data == None:
            continue
        add_to_anime(db_manager,data)
        add_generic_data(db_manager, "genre", ["name"], "genres", data["genres"],data)
        try:
            add_generic_data(db_manager, "translation", ["name"], "translation", data["translation"],data)
        except:
            pass
        try:
            add_generic_data(db_manager, "licensed", ["name"], "licensed", data["licensed"],data)
        except:
            pass

    dataset3 = PAS.get_data("https://animestars.tv/top100.html")
    for data in dataset3:
        if data == None:
            continue
        add_to_anime(db_manager,data)
        add_generic_data(db_manager, "genre", ["name"], "genres", data["genres"],data)
        try:
            add_generic_data(db_manager, "translation", ["name"], "translation", data["translation"],data)
        except:
            pass
        try:
            add_generic_data(db_manager, "licensed", ["name"], "licensed", data["licensed"],data)
        except:
            pass
    db_manager.close_connection()



