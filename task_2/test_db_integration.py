import requests
import pyodbc
import pytest
from faker import Faker

fake = Faker()


class TestDbIntegration:

    # Конфигурация для подключения к БД и АПИ
    API_URL = "http://localhost:8000/register"
    connection_string = (
        "DRIVER={PostgreSQL};"
        "DATABASE=mydatabase;"
        "UID=myuser;"
        "PWD=mypassword;"
        "SERVER=localhost;"
        "PORT=5432;"
    )
    # Генерация пользователя
    def setup(self):
        self.test_user = {
            "username": fake.name(),
            "email": fake.email()
        }

    @pytest.mark.user
    def test_create_user(self):
        # API запрос на регистрацию
        response = requests.post(
            url=self.API_URL,
            json=self.test_user
        )
        assert response.status_code == 200

        # Подключение и запрос к БД
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", \
                       (self.test_user["email"]))
        user = cursor.fetchone()
        print(user)
        connection.close()

        # Проверка на наличие пользователя в БД и валидности его данных
        assert user is not None
        assert user[1] == self.test_user["username"]
        assert user[2] == self.test_user["email"]












