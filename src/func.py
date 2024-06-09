from Saver import JSONsaver

def get_area_filter(vacancies, filter_words):
    "Возвращает список, фильтрованный по городам"
    filter_words_list = filter_words.split()
    filtered_area = []
    for vacancy in vacancies:
        if vacancy.citi in filter_words_list:
            filtered_area.append(vacancy)
    return filtered_area


def filter_by_salary(vacancies, min_salary):
    """
        Фильтрует список вакансий по минимальной заработной плате.

        :param vacancies: Список словарей, где каждый словарь представляет вакансию'.
        :param min_salary: Целое число, минимальная заработная плата для фильтрации.
        :return: Список словарей с вакансиями, чья заработная плата не ниже min_salary.
    """
    return [vacancy for vacancy in vacancies if vacancy.salary >= min_salary]

def one_object_str(vacancies):
    """
    :param vacancies: список словарей с вакансиями
    :return: вакансии построчно
    """
    for vacancy in vacancies:
        print(f"Название: {vacancy.name}, URL: {vacancy.url}, Зарплата: {vacancy.salary}, "
              f"Город: {vacancy.citi}, Опыт: {vacancy.exp}"
              )
def print_menu():
    """
    return: меню выбора действий
    """
    print("1 - выборка по зарплате\n"
          "2 - выборка по городам\n"
          "3 - вывод всех вакансий\n"
          "4 - топ N вакансий по зарплате\n"
          "5 - Загрузить из файла\n"
          "0 - выход")


def save_choice_vacancies(choice_vacancies):
    """
    Сохраняет вакансии в файл JSON
    :param choice_vacancies: список словарей с фильтрованными вакансиями
    :return:
    """
    save = int(input('1 - сохранить запрос в файл\n2 - вернутся в меню\n'))
    if save == 1:
        choice_vacancies = [vac.__dict__ for vac in choice_vacancies]
        filename = input('Введите название файла:\n')
        save_file = JSONsaver(filename + '.json')
        save_file.save_vacancies(choice_vacancies)
        print('Файл сохранен')
    else:
        return

