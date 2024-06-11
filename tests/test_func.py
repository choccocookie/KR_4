import pytest

@pytest.fixture
def vacancies():
    return [
        {"name": "Engineer", "url": "url1", "salary": 50000, "citi": "Москва", "exp": "3 года"},
        {"name": "Developer", "url": "url2", "salary": 60000, "citi": "Тула", "exp": "2 года"},
        {"name": "Manager", "url": "url3", "salary": 70000, "citi": "Калуга", "exp": "5 лет"},
        {"name": "Analyst", "url": "url4", "salary": 80000, "citi": "Москва", "exp": "1 год"},
        {"name": "Designer", "url": "url5", "salary": 55000, "citi": "Тула", "exp": "4 года"}
    ]

def get_area_filter(vacancies, filter_words):
    """
    Фильтрует список вакансий по указанным городам.
    Принимает список вакансий и строку с названиями городов,
    разделенными пробелами. Возвращает список вакансий, которые находятся
    в указанных городах.
    """
    filter_words_list = filter_words.split()
    filtered_area = []
    for vacancy in vacancies:
        if vacancy['citi'] in filter_words_list: # произвели замену vavancy.citi на ['citi'], для тестов со словарями
            filtered_area.append(vacancy)
    return filtered_area


def test_single_city(vacancies):
    """
    Тестируем при запросе из 1 города
    """
    filter_words = "Москва"
    expected_result = [
        vacancies[0],
        vacancies[3]
    ]
    result = get_area_filter(vacancies, filter_words)
    assert result == expected_result

def test_multiple_cities(vacancies):
    """
    Тестируем при запросе из 2 городов
    """
    filter_words = "Москва Тула"
    expected_result = [
        vacancies[0],
        vacancies[1],
        vacancies[3],
        vacancies[4]
    ]
    result = get_area_filter(vacancies, filter_words)
    assert result == expected_result

def test_no_matching_city(vacancies):
    """
    Тестируем при запросе из 3 городов
    """
    filter_words = "Самара"
    expected_result = []
    result = get_area_filter(vacancies, filter_words)
    assert result == expected_result

def test_empty_filter_words(vacancies):
    """
    Тестируем пустой запрос
    """
    filter_words = ""
    expected_result = []
    result = get_area_filter(vacancies, filter_words)
    assert result == expected_result


def filter_by_salary(vacancies, min_salary):
    """
        Фильтрует список вакансий по минимальной заработной плате.

        :param vacancies: Список словарей, где каждый словарь представляет вакансию'.
        :param min_salary: Целое число, минимальная заработная плата для фильтрации.
        :return: Список словарей с вакансиями, чья заработная плата не ниже min_salary.
    """
    return [vacancy for vacancy in vacancies if vacancy['salary'] >= min_salary] # произвели замену vavancy.salary на ['salary'], для тестов со словарями

def test_filter_by_salary(vacancies):
    min_salary = 65000
    expected_result = [
        vacancies[2],
        vacancies[3]
    ]
    result = filter_by_salary(vacancies, min_salary)
    assert result == expected_result


