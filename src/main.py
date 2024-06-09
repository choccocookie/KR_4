from hhAPI import HH
from Vacanсy import Vacancy
from func import filter_by_salary, get_area_filter, one_object_str, print_menu, save_choice_vacancies
from Saver import JSONsaver

def main():
    print("Введите искомую вакансию:")
    user_vacancy_name = input()
    a = HH()
    vacancies = a.load_vacancies(user_vacancy_name) # создаем экземпляр класса HH

    while True: # цикл, который будет продолжаться до тех пор, пока пользователь не решит выйти
        print_menu()
        choice = int(input("Ввод:"))
        if choice == 1: # выборка по ЗП
            min_salary = int(input('Введите минимальный порог заработной платы:\n'))
            choice_vacancies = one_object_str(filter_by_salary(vacancies, min_salary)) # Список вакансий с фильтрами
            print(choice_vacancies)
            save_choice_vacancies(choice_vacancies)

        elif choice == 2: # выборка по городу
            citi = input('Введите город:\n').title()
            choice_vacancies = one_object_str(get_area_filter(vacancies, citi))
            print(choice_vacancies)
            save_choice_vacancies(choice_vacancies)

        elif choice == 3: # вывод всех вакансий
            choice_vacancies = sorted(vacancies, reverse=True)
            print(one_object_str(choice_vacancies))
            save_choice_vacancies(sorted(vacancies, reverse=True))

        elif choice == 4: # топ N по зарплате
            top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
            choice_vacancies = one_object_str(sorted(vacancies, reverse=True)[:top_n])
            print(choice_vacancies)
            save_choice_vacancies(choice_vacancies)

        elif choice == 5: # Загрузить из файла
            user_file_name = input('Введите наименование файла c форматом:\n')
            user_citi = input('Введите город, в котором ищите вакансии:\n')
            user_vacancies = JSONsaver(user_file_name)
            result = user_vacancies.get_by_criteria(user_citi)
            for vacancy in result:
                print(f"Название: {vacancy['name']}, URL: {vacancy['url']}, Зарплата: {vacancy['salary']}, "
                      f"Город: {vacancy['citi']}, Опыт: {vacancy['exp']}"
                      )
        elif choice == 0: # Завершение работы программы
            break
    print('Программа завершена')




main()