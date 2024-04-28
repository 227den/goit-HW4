def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_id, cat_name, cat_age = cat_data
                    cat_info = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age
                    }
                    cats_info.append(cat_info)
                else:
                    print(f"Некоректні дані в рядку: '{line.strip()}'")

            return cats_info

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка при роботі з файлом: {e}")
        return []