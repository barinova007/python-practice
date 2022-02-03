# Create, Read/доделать Update, Delete.
#
#  1. Сделать функционал для проверки уникальности Email (существует ли такой пользователь) перед добавлением нового пользователя.
#  2. Добавить возможность обновления информации о существующем пользователе.
#  3. Добавить возможность удалить существующего пользователя
#  4. Сделать -- Help для просмотра списка возможных команд с комментариями к ним
#
# Постарайтесь всё сделать через функции.




from crud_1. create_1 import create_user
from crud_1. read_1 import user_info, all_users_info

user_emails = []
users_storage = {}

while True:

    action = input('Please enter create or read, or update, or delete actions: ')

    if action == 'create':
        print('action =', action)

        email = input('Email:')
        name = input('name: ')
        password = input('password: ')
        phone = input('phone: ')

        user_emails = create_user(email,
                                  name,
                                  password,
                                  phone,
                                  user_emails,
                                  users_storage)
        print('user_emails',user_emails)
        print('users_storage', users_storage)

    elif action == 'read_all':
        print('action =', action)
        all_users_info(users_storage)

    elif action == 'read_user':

        user_e == input ('Enter user email')
        user_info(user_e, user_emails, users_storage)

        print('action =', action)
        print('User =', message)

    elif action == 'update':
        print('action =', action)

    elif action == 'delete':
        print('action =', action)
    else:
        print("Please enter create or read, or update, or delete actions: ")

