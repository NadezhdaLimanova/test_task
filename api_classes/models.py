#api_classes/models

from faker import Faker

fake = Faker()


class RegisterUser:
    """Класс для создания рандомной информации о пользователе"""
    @staticmethod
    def random():
        name = fake.name()
        job = fake.job()
        return {"name": name, "job": job}