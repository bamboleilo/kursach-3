from datetime import datetime
import json


def get_data(filename):
    '''
    Функция получает список словарей из нужного файла
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data, "INFO: Данные получены успешно!"


def get_filtered_data(data, filtered_empty_from=False):
    '''
    Функция отфильтровывает словари по состоянию опрации - EXECUTED
    '''
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):
    '''
    Функция сортирует словари по дате и отбирает последние
    в зависимости от параметра count_last_values
    '''
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    '''
    Функция производит форматирование словарей
    в заданный для вывода формат
    '''
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", "[СКРЫТО]"

        recipient = f"**{row['to'][-4:]}"

        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")
    return formatted_data