user_input = input('Напишите слово, а я проверю, является ли оно палиндромом ').lower()
if user_input == user_input[::-1]:
    print(f'Обнаружен Палиндром: {user_input}')
else:
    print(f'Слово "{user_input}" не является палиндромом!')
