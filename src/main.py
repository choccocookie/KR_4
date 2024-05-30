"""import requests

from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass
        """
import requests
import json
from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def save_to_file(self, data, filename):
        pass





class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """Получает слово, по которому будет производится поиск по ссылке,
        циклично ищет данные по ключевому слову и добвляет их в словарь Vacancies"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return vacancies

    def save_to_file(self, data, filename):
        pass



file_worker = None  # Инициализация file_worker, в зависимости от вашей реализации
hh_parser = HH(file_worker)
hh_parser.load_vacancies("python")
print(hh_parser.vacancies)

search_text = 'Python developer'
hh_parser.load_vacancies(search_text)
#hh_parser.save_vacancies('vacancies.json')