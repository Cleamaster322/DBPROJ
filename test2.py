table_name = "anime"
column_name = "name_ru"

query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = like (%s%) and year_of_release = %s"
value = ("Семь смертных грехов",)

print(query)