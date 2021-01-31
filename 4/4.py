guestlist = []

class NewGuest:
    def __init__(self, user_name, city, status):
        self.user_name = user_name
        self.city = city
        self.status = status

class Guest(NewGuest):
    def user_info(self):
        return f'«{self.user_name}, г. {self.city}, статус "{self.status}"»'

    def add_to_list(self):
        guestlist.append(self)

guest1 = Guest('Иван Петров', 'Москва', 'Наставник')
guest1.add_to_list()

guest2 = Guest('Людмила Людмиловна', 'Омск', 'Наставник')
guest2.add_to_list()

for guest in guestlist:
    print(f'{guestlist.index(guest) + 1} {guest.user_info()}')