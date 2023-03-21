import pytest
from utils import get_data, get_filtered_data, get_last_data, get_formatted_data

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

