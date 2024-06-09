from hhAPI import HH
from Vacanсy import Vacancy
from func import filter_by_salary, get_area_filter, one_object_str, print_menu
from Saver import JSONsaver

def main():
    print("Введите искомую вакансию:")
    user_vacancy = input()
    a = HH()
    vacancies = a.load_vacancies(user_vacancy) # создаем экземпляр класса HH
    while True: # цикл, который будет продолжаться до тех пор, пока пользователь не решит выйти
        print_menu()
        choice = int(input("Ввод:"))
        if choice == 1:
            min_salary = int(input('Введите минимальный порог заработной платы:\n'))
            choice_vacancies = one_object_str(filter_by_salary(vacancies, min_salary)) # Список вакансий с фильтрами
            print(choice_vacancies)

            def save_choice_vacancies(choice_vacancies):
                """
                Сохраняет вакансии в файл по
                :param choice_vacancies: список словарей с фильтрованными вакансиями
                :return:
                """
                save = int(input('1 - сохранить запрос в файл\n2 - вернутся в меню\n'))
                if save == 1:
                        name_file = input('Введите название файла:\n')
                        save_file = JSONsaver(name_file+'.json')
                        save_file.save_vacancies(choice_vacancies)
                        print('Файл сохранен')
                else:
                    return

        elif choice == 2:
            citi = input('Введите город:\n').title()
            user_vacancies = one_object_str(get_area_filter(vacancies, citi))
            print(user_vacancies)

        elif choice == 3:
            print(one_object_str(sorted(vacancies, reverse=True)))
        elif choice == 4:
            top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
            print(one_object_str(sorted(vacancies, reverse=True)[:top_n]))
        elif choice == 5:
            print("1 - сохранить в файл\n"
                  "2 - загрузить из файла\n"
                  "3 - удалить вакансию из файла\n")
        elif choice == 0:
            break
    print('Программа завершена')




main()