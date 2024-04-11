def filter_dicts_by_state(dict_list: str, state='EXECUTED') -> str:
    return [dict_ for dict_ in dict_list if dict_.get('state') == state]

# Пример использования функции
dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filtered_list_executed = filter_dicts_by_state(dict_list)
filtered_list_canceled = filter_dicts_by_state(dict_list, state='CANCELED')

print(filtered_list_executed)
print(filtered_list_canceled)

