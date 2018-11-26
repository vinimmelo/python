import datetime

def print_header():
    print('-----------------------------------')
    print('           BIRTHDAY APP')
    print('-----------------------------------')


def get_birthday_for_user():
    print('When were you born? ')
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original, target):
    this_year = datetime.date(target.year, original.month, original.day)
    dt = this_year - target
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year!".format(days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy Birthday!!!")


def main():
    print_header()
    birthday = get_birthday_for_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(birthday, today)
    print_birthday_information(number_of_days)


if __name__ == '__main__':
    main()
