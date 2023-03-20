import pytest
import requests.exceptions

from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def test_get_data():
    '''
    Тест на проверку соединения:
        - успешно;
        - синтаксическая ошибка;
        - ошибка соединения.
    '''
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679361416440&signature=9nd2eY3JRxxqr2v_h4xNYfZ7gClYMdteQr23vZzRNb0&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679361416440&signature=9nd2eY3JRxxqr2v_h4xNYfZ7gClYMdteQr23vZzRNb0&downloadName=operation.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 400"
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679361416440&signature=9nd2eY3JRxxqr2v_h4xNYfZ7gClYMdteQr23vZzRNb0&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    '''
    Тест на проверку функции get_filtered_data на количество значений EXECUTED
    '''
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_data(test_data):
    '''
    Тест на проверку функции get_last_data и вывода
    нужного количества элементов из списка по дате
    '''
    data = get_last_data(test_data, count_last_values=3)
    assert data[0]['date'] == '2019-07-15T11:47:40.496961'
    assert len(data) == 3


def test_get_formatted_data(test_data):
    '''
    Тест проверки на нахождение отправителя и замены на [СКРЫТО] если нет
    '''
    data = get_formatted_data(test_data[:1])
    assert data == ['24.12.2018 Перевод со счета на счет\nСчет 7168 74** **** 5290 -> Счет **9781\n991.49 руб.\n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['09.03.2018 Перевод организации\n[СКРЫТО]  -> Счет **1315\n25780.71 руб.\n']

