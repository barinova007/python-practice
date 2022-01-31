from crud_1. create_1 import create_user

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

    elif action == 'read':
        print('action =', action)

    elif action == 'update':
        print('action =', action)

    elif action == 'delete':
        print('action =', action)
    else:
        print("Please enter create or read, or update, or delete actions: ")

