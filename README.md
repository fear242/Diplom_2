# Diplom_2

Second task of diploma on "Python QA automation" course

Structure:
Diplom_2/
├-tests
│  ├-auth - Наборы проверок, связанных с пользователями
│  │  ├-test_user_change.py - Проверки изменения данных пользователя
│  │  ├-test_user_creation.py - Проверки создания пользователя
│  │  └-test_user_login.py - Проверка логина пользователя
│  └-orders - Наборы проверок, связанных с заказами
│     ├-test_order_create.py - Проверки создания заказа
│     └-test_order_receivement.py - Проверки получения списка заказов
├-allure_results - Отчёты о тестах
├-conftest.py - Фикстуры
├-README.md - Этот файл
└-requirements.txt - Внешние зависимости

Для запуска проекта понадобятся IDE для Python и библиотеки, перечисленные в файле requirements.txt
