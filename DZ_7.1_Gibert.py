data_lst = ['1', '2', '3', '4d', 5]
new_lst = []
for elem in data_lst:
    try:
        int(elem)
        new_lst.append(elem)
    except ValueError:
        print(f'Данные {elem} невалидны!')
print(new_lst)