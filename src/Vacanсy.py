

class Vacancy:

    name: str  # Название вакансии
    url: str  # URL страницы вакансии
    salary: int  # Зарплата предложенная за работу
    area: str # Город

    instances = []

    def __init__(self, name, url, salary, citi, exp):
        self.name = name
        self.url = url
        self.salary = salary
        self.citi = citi
        self.exp = exp
        #self.skills = skills
        self.validate()

    def validate(self):
        if self.name == None:
            self.name = 'Не указано'
        if self.salary == None:
            self.salary = 0
        if self.citi == None:
            self.citi = 'Не указано'



    @classmethod

    def new_vacancy(cls, data):
        """
            Получает список словарей, итерируя его, формирует новый словарь по ключам(name, url ...)
            и добавляет каждый новый словарь в список instances
        """
        instances = []
        for vac in data:
            name = vac.get('name')
            url = vac.get('alternate_url')
            salary = (vac.get('salary').get('from')) if vac['salary'] != None else vac.get('salary')
            citi = vac.get('area').get('name')
            exp = vac.get('experience').get('name') if vac['experience'] != None else vac.get('experience')
            #skills = vac.get('key_skills').get('name') if vac['key_skills'] != list else vac.get('key_skills')
            instance = cls(name, url, salary, citi, exp)
            instances.append(instance)
            #cls.instances = instances
        return instances

    def __lt__(self, other):
        return self.salary < other.salary


    def __str__(self):
        return f"{self.name}, {self.url}, {self.salary}, {self.citi}, {self.exp}"

    def __repr__(self):
        return f"{self.name}, {self.url}, {self.salary}, {self.citi}, {self.exp}"

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'citi': self.citi,
            'experience': self.exp
        }



# v1 = Vacancy('1', '1', 10, '1', '1')
# v2 = Vacancy('1', '1', 20, '1', '1')
# v3 = Vacancy('1', '1', 5, '1', '1')
#
# vacancies = [v1, v2, v3]
# result = sorted(vacancies)
# print(result)


