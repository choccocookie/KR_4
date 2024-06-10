import config
import requests
import json
from abc import ABC, abstractmethod
from vacanсy import Vacancy

class Parser(ABC):
    """
    Абстрактный класс для работы с API
    """


    @abstractmethod
    def load_vacancies(self, keyword):
        pass



class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = config.HH_API_URL
        self.headers = config.HH_USER_AGENT
        self.params = config.DEFAULT_PARAMS
        self.vacancies = []


    def load_vacancies(self, keyword):
        """Получает слово, по которому будет производится поиск по ссылке, и количество выводимых вакансий.
        циклично ищет данные по ключевому слову и добвляет их в словарь Vacancies"""
        self.params['text'] = keyword
        while self.params.get('page') != config.MAX_PAGES:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(Vacancy.new_vacancy(vacancies)) # Формирует список словарей с вакансиями, используя метод класса Vacancy
            self.params['page'] += 1
            return self.vacancies

    def print_vacancies(self):
        """Выводит все загруженные вакансии на экран"""
        for vacancy in self.vacancies:
            print(vacancy)








# hh_parser = HH()
# hh_parser.load_vacancies("python")
# hh_parser.print_vacancies()
#
# search_text = 'Python developer'
# hh_parser.load_vacancies(search_text)
# print(hh_parser.vacancies)
# a = [vac.__dict__ for vac in hh_parser.vacancies]
# print(a)