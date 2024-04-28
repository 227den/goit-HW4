def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Некоректні дані в рядку: '{line.strip()}'")

            if salaries:
                total_salary = sum(salaries)
                average_salary = total_salary / len(salaries)
                return total_salary, average_salary
            else:
                print("Файл не містить жодних даних про заробітні плати.")
                return 0, 0

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка при роботі з файлом: {e}")
        return 0, 0