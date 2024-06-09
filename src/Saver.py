import requests
import json
from abc import ABC, abstractmethod
from Vacanсy import Vacancy
from pathlib import Path

class Saver(ABC):

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def delete_from_file(self):
        pass

class JSONsaver(Saver):
    """
    Класс для сохранения
    """

    def __init__(self, filename):
        self.filename = filename
        self.filepath = Path(self.filename)
        if not self.filepath.exists(): # Проверяем существование файла, если False, то создаем пустой
            self.filepath.write_text('[]', encoding='utf-8')


    def read_from_file(self):
        """
        Загружает вакансии из файла в формате Json
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_vacancies(self, vacancies):
        """
        Сохраняет список словарей с вакансиями в файл Json
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def save_to_file(self, vacancy):
        """
        Загружает список вакансий, добавляет в него новую вакансию, сохраняет обновленный список
        """
        vacancies = self.read_from_file() # загружаем вакансии из файла с вакансиями и присваивам их к переменной
        vacancies.append(vacancy.__dict__) # добавляем новую вакансию к загруженному списку вакансий
        self.save_vacancies(vacancies)


    def criteria_check(self, vacancy, criteria):
        """
        Проверяет наличие запрашиваемых критериев по ключам списка вакансий
        """
        for key, value in criteria.items():
            if vacancy.get(key) != value:
                return False
        return True

    def get_by_criteria(self, criteria):
        """
        Возвращает список вакансий в соответствии с заданными критериями
        """
        criteria = {'citi': criteria.title()}
        vacancies = self.read_from_file()
        new_vacancies = [vac for vac in vacancies if self.criteria_check(vac, criteria)]
        return new_vacancies

    def vac_compression(self, vac1, vac2):
        """
        Метод сравнения двух вакансий, возвращает булевое значаение
        является вспомогательным методом к delete_from_file
        """
        return vac1['name'] == vac2.name and vac1['url'] == vac2.url # сравнение значения словаря по ключю vac1['name'] и атрибута экземпляра vac2.name

    def delete_from_file(self, vacancy):
        """
        Загружает вакансии из файла, генериует новый список вакансий без полученной вакансии
        """
        vacancies = self.read_from_file()
        new_vacancies = [vac for vac in vacancies if not self.vac_compression(vac, vacancy)] # используем генератор списка с условием
        self.save_vacancies(new_vacancies)




# s1 = JSONsaver('vacs3.json')
# #v1 = Vacancy("Python Developer", "https://example.com", 100000, "Москва", "2-3 года")
# a = s1.read_from_file()
# print(a)






















