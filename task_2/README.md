1. Установите зависимости ```pip3 install -r requirements.txt```
2. Запустите контейнер с базой данных ```docker-compose up```
3. Запустите сервер с нашим API: ```uvicorn main:app --reload```
4. Запустите тест: ```pytest -sv -m user```