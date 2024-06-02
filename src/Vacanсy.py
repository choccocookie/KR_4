

class Vacancy:

    name: str  # Название вакансии
    url: str  # URL страницы вакансии
    salary: int  # Зарплата предложенная за работу
    area: str
    schedule: str  # требования по графику
    snippet: str # обязанности
    instances = []

    def __init__(self, name, url, salary, citi, exp):
        self.name = name
        self.url = url
        self.salary = salary
        #self.salary_to = salary_to
        self.citi = citi
        self.exp = exp
        self.validate()

    def validate(self):
        if self.name == None:
            self.name = 'Не указано'
        if self.salary == None:
            self.salary = 0
        if self.citi == None:
            self.siti = 'Не указано'



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
            instance = cls(name, url, salary, citi, exp)
            instances.append(instance)
            #cls.instances = instances
        return instances



    def __str__(self):
        return f"{self.name}, {self.url}, {self.salary}, {self.citi}, {self.exp}"



