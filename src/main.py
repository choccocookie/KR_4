from hhAPI import HH
from Vacanсy import Vacancy
from func import filter_by_salary, get_area_filter

def main():
    print("Введите искомую вакансию")
    user_vacancy = input()
    a = HH()
    vacancies = a.load_vacancies(user_vacancy) # создаем экземпляр класса HH
    print("1 - выборка по зарплате"
          "2 - выборка по городам"
          "3 - вывод всех вакансий"
          "4 - топ N вакансий по зарплате"
          "5 - редактор файла")
    choice = input("Ввод:\n")
    if choice == 1:
        min_salary = int(input('Введите минимальный порог заработной платы:\n'))
        print(filter_by_salary(vacancies, min_salary))
    elif choice == 2:
        citi = input('Введите город'.title())
        print(get_area_filter(vacancies, citi))
    elif choice == 3:
        print(sorted(vacancies, reverse=True))
    elif choice == 4:
        top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
        print(sorted(vacancies, reverse=True)[:top_n])
    elif choice == 5:
        print("1 - сохранить в файл Json"
              "2 - загрузить из файла Json"
              "3 - ")

        pass


main()