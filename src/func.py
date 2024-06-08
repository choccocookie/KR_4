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
    return [vacancy for vacancy in vacancies if vacancy['salary'] < min_salary]



