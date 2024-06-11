import pytest
from src.vacanсy import Vacancy

def test_vacancy_initialization():
    """
    Проверяем на возможность ошибки инициализации
    """
    vac = Vacancy("Vacancy", "www.vac.com", 50000, "Москва", "От 1 года")
    assert vac.name == "Vacancy"
    assert vac.url == "www.vac.com"
    assert vac.salary == 50000
    assert vac.citi == "Москва"
    assert vac.exp == "От 1 года"


def test_validate():
    """
    Проверяем на возможность ошибки при валидации
    """
    vac = Vacancy(None, "http://example.com", None, None, "1-3 года")
    assert vac.name == "Не указано"
    assert vac.salary == 0
    assert vac.citi == "Не указано"

def test_new_vacancy():
    data = [
        {
            "name": "Test Vac 1",
            "alternate_url": "www.example.com/1",
            "salary": {"from": 1000},
            "area": {"name": "Москва"},
            "experience": {"name": "1-3 года"}
        },
        {
            "name": "Test Vac 2",
            "alternate_url": "www.example.com/2",
            "salary": {"from": 2000},
            "area": {"name": "Воркута"},
            "experience": {"name": "3-5 лет"}
        }
    ]
    instances = Vacancy.new_vacancy(data)
    assert instances[0].name == "Test Vac 1"
    assert instances[1].name == "Test Vac 2"


@pytest.fixture
def vacancy_for_test():
    return Vacancy("Vacancy", "www.vac.com", 50000, "Москва", "От 1 года")


def test_str(vacancy_for_test):
    """ Тестируем метод __str__"""
    assert str(vacancy_for_test) == "Vacancy, www.vac.com, 50000, Москва, От 1 года"


def test_repr(vacancy_for_test):
    """ Тестируем метод __repr__"""
    assert repr(vacancy_for_test) == "Vacancy, www.vac.com, 50000, Москва, От 1 года"

def test_lt(vacancy_for_test):
    """ Тестируем метод __lt__"""
    vac2 = Vacancy("Vacancy2", "www.vac.com", 70000, "Москва", "От 2 лет")
    assert vacancy_for_test < vac2


def test_to_dict(vacancy_for_test):
    """ Тестируем метод to_dict"""
    assert vacancy_for_test.to_dict() == {'name': "Vacancy", 'url': "www.vac.com", 'salary': 50000, 'citi': "Москва", 'experience': "От 1 года"}



