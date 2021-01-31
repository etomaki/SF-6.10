class WebPocketReg:
    def __init__(self, email, user_name, password, balance=0):
        self.email = email
        self.user_name = user_name
        self.password = password
        self.balance = balance

class WebPocket(WebPocketReg):
    def plus(self, money):
        self.balance += money
        print(f"Ваш баланс был пополнен на {money}р")
        print(f'Ваш текущий счет - {self.balance}р')

    def minus(self, money):
        if self.balance < 0 or money > self.balance:
            print('На кошельке недостаточно средств')
            print(f'Ваш текущий счет - {self.balance}р')
        else:
            self.balance -= money
            print(f'С вашего счета снято {money}р')
            print(f'Ваш текущий счет - {self.balance}р')
            
    def user_info(self):
        return f'Клиент «{self.user_name}». Баланс: {self.balance}руб.'

    def user_account_info(self):
        return f'Почта - {self.email}, Имя Фамилия - {self.user_name}, Пароль - {self.password}, Баланс - {self.balance}р'

user_1 = WebPocket('dryjok@ro.ru', 'Иван Петров', '12345')

print(user_1.user_info())

user_1.plus(100)
user_1.minus(50)

print(user_1.user_info())
print(user_1.user_account_info())

# UserList = {
#     'admin': 'admin'
# }

# def registration():
#     choice = input('Если вы хотите войти - L, хотите зарегистрироваться - R: ')
#     if choice == 'L':
#         login = input('Введите ваш Email: ')
#         if login in UserList.keys():
#             passw = input('Введите пароль: ')
#             if passw == UserList[login]:
#                 print('Вы успешно вошли')
#             else:
#                 print('Пароль введен неверно, попробуйте позже')
#         else:
#             print('Такого пользователя не существует')
#     elif choice == 'R':
#         login = input('Введите ваш Email: ')
#         name = input('Введите ваше имя и фамилию (Иван Петров): ')
#         passw = input('Введите ваш пароль: ')
#         UserList.update({login: passw})

# registration()


